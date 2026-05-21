import pandas as pd
import mysql.connector

print("Reading data...")
# 1. Use the exact absolute path to your cleaned dataset
input_path = r"C:\Users\ammar\Downloads\Sample - Superstore\superstore_clean.csv"
df = pd.read_csv(input_path)
print(f"Loading {len(df)} rows...")

# Safely handle any potential blank values to prevent MySQL crashes
df = df.where(pd.notnull(df), None)

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='ecommerce_analytics'
)
cursor = conn.cursor()

# Clear old data first
cursor.execute("DELETE FROM orders")

# 2. Convert Pandas dataframe to a list of native Python tuples 
# (This fixes the NumPy data type crash)
data_to_insert = [tuple(x) for x in df.values.tolist()]

# 3. Write the query once, then use executemany() for lightning speed
insert_query = """
    INSERT INTO orders (
        row_id, order_id, order_date, ship_date, ship_mode,
        customer_id, customer_name, segment, city, state,
        region, product_id, category, sub_category, product_name,
        sales, quantity, discount, profit, order_year,
        order_month, order_month_name, days_to_ship,
        profit_margin_pct, is_profitable
    ) VALUES (
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s
    )
"""

try:
    print("Inserting data into MySQL... (This should take just a few seconds!)")
    # executemany inserts the entire list at once instead of one by one
    cursor.executemany(insert_query, data_to_insert)
    conn.commit()
    print(f"✅ Done! {cursor.rowcount} rows loaded successfully.")
except Exception as e:
    print(f"❌ Error inserting data: {e}")
finally:
    cursor.close()
    conn.close()