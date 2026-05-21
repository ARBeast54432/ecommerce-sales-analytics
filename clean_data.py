import pandas as pd

print("loading data..")
# 1. Provide the exact path to your dataset
# Make sure to add .csv to the end if Windows is hiding file extensions!
input_path = r"C:\Users\ammar\Downloads\Sample - Superstore\Sample - Superstore.csv"
df = pd.read_csv(input_path, encoding='latin1')

print(f"Original shape: {df.shape}")
print(f"\nColumn names:\n{df.columns.tolist()}")
print(f"\nMissing values:\n{df.isnull().sum()}")

# Clean column headers
df.columns = df.columns.str.strip().str.lower().str.replace(' ','_').str.replace('-', '_')
print(f"\nCleaned columns: {df.columns.tolist()}")

# 2. FIXED TYPO: Changed 'oreder_date' to 'order_date'
df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date']  = pd.to_datetime(df['ship_date'])

# Feature Engineering
df['order_year']          = df['order_date'].dt.year
df['order_month']         = df['order_date'].dt.month
df['order_month_name']    = df['order_date'].dt.strftime('%B')
df['days_to_ship']        = (df['ship_date'] - df['order_date']).dt.days
df['profit_margin_pct']   = round((df['profit'] / df['sales']) * 100, 2)
df['is_profitable']       = df['profit'] > 0

# 3. FIXED TYPO: Changed lem() to len()
before = len(df)
df = df.drop_duplicates()
after = len(df)

# 4. FIXED MISSING VARIABLE: Added logic to actually calculate loss_orders
loss_orders = df[df['profit'] < 0]
print(f"\nLoss-making orders: {len(loss_orders)}")

# Clean text data
df['segment']  = df['segment'].str.strip().str.title()
df['category'] = df['category'].str.strip().str.title()
df['region']   = df['region'].str.strip().str.title()

# Drop unnecessary columns
cols_to_drop = ['country', 'postal_code']
df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])

# Save and print results
output_path = r"C:\Users\ammar\Downloads\Sample - Superstore\superstore_clean.csv"
df.to_csv(output_path, index=False)
print(f"\n✅ Done! Clean file saved.")
print(f"Final shape: {df.shape}")
print(f"\nSample data:")
print(df.head(3))