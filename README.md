# 📊 Global E-Commerce Sales Analytics Dashboard

> **End-to-end data analytics project** — from raw CSV to interactive Power BI dashboard — using Python, MySQL, SQL, and Power BI.

---

## 🔍 Business Problem

An e-commerce company needed to understand why profits were lagging despite growing sales. This project identifies the root causes of profit leakage and surfaces data-driven recommendations to recover lost revenue.

---

## 💡 Key Findings

| # | Finding |
|---|---------|
| 1 | **Technology** drives the highest revenue ($836K, 36.4% share), but **Office Supplies** has a healthier profit margin |
| 2 | The **West region** leads all regions with **$108K profit**; the Central region is the weakest performer |
| 3 | Products with discounts above **40% are consistently loss-making** — 10 products alone caused **$46K in total losses** |
| 4 | Average discount on loss-making products is a staggering **62.67%** — far above the safe threshold |
| 5 | **Consumer segment** generates 55% of total revenue ($1.16M) but also requires the highest support costs |
| 6 | **Home Office segment** has the highest average order value ($473) — an underutilised premium opportunity |
| 7 | **Q4 (September–December)** consistently drives 35–40% of annual revenue across all years |

---

## 📈 Dashboard Overview

### Page 1 — Executive Summary
<img width="1579" height="891" alt="E commerce sales analytics dashboard" src="https://github.com/user-attachments/assets/ca09475d-042b-4a87-a188-86a4b26f1b13" />


**KPIs at a glance:**
- Total Revenue: **$2.30M**
- Total Profit: **$286K**
- Total Orders: **5,009**
- Avg Profit Margin: **12%**
- Total Customers: **793**

---

### Page 2 — Sales & Profit Trends Over Time
<img width="1571" height="885" alt="Sales and profit trends over time" src="https://github.com/user-attachments/assets/7dfd262f-83bc-4fa6-b7c0-cdb28eb0a240" />


Q4 peaks are visible every year. July consistently shows profit dips across all years — worth investigating seasonal demand and staffing patterns.

---

### Page 3 — Top Products & Loss-Making Items
<img width="1576" height="886" alt="Top Products   Loss Making Items" src="https://github.com/user-attachments/assets/5fb4604f-289d-4eea-b3a0-eee4a5ff7fc2" />

**Canon imageCLASS** is the top revenue product at $62K. Loss-making products average **62.67% discount rates** — the primary driver of margin erosion.

---

### Page 4 — Customer Segment Analysis
<img width="1576" height="886" alt="Customer Segment Analysis" src="https://github.com/user-attachments/assets/e108baf7-210f-40b5-90d4-7f5047733087" />

Consumer is the largest segment ($1.16M), Corporate is the most stable (lowest churn risk), and Home Office has the highest per-order value ($473).

---

## 🔗 Live Dashboard

👉 **[View on Power BI](https://app.powerbi.com/groups/me/reports/940725a3-01db-4b10-b2a6-36fcd470cafc/5820341f07f505455fdb?experience=power-bi)**

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python (Pandas) | Data cleaning & feature engineering |
| MySQL | Relational data storage |
| SQL | Business analysis queries |
| Power BI | Interactive 4-page dashboard |
| Excel | Initial data exploration |

---

## 📁 Project Structure

```
ecommerce-sales-analytics/
│
├── clean_data.py              ← Cleans raw CSV, adds calculated columns
├── load_data.py               ← Loads cleaned data into MySQL
│
├── queries/
│   ├── kpi_summary.csv        ← Overall business KPIs
│   ├── category_performance.csv
│   ├── monthly_trend.csv
│   ├── regional_performance.csv
│   ├── top_products.csv
│   ├── loss_products.csv
│   └── segment_analysis.csv
│
├── dashboard/
│   ├── executive_summary.jpg
│   ├── sales_trends.jpg
│   ├── product_performance.jpg
│   └── customer_segments.jpg
│
├── data/
│   └── superstore_clean.csv   ← Cleaned dataset (9,994 rows)
│
└── README.md
```

---

## 🔄 How to Reproduce

1. Download the **Superstore Sales Dataset** from [Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
2. Run `python clean_data.py` to produce `superstore_clean.csv`
3. Create the MySQL database and run `python load_data.py` to load 9,994 rows
4. Open Power BI Desktop and connect to the 7 CSV files in `/queries/`
5. View the live dashboard: [Power BI Link](https://app.powerbi.com/groups/me/reports/940725a3-01db-4b10-b2a6-36fcd470cafc/5820341f07f505455fdb?experience=power-bi)

---

## ⚡ Recommendations

1. **Cap discounts at 25% maximum** — estimated recovery of $40K–$50K annually
2. **Implement a discount approval process** for anything above 20%
3. **Double down on Q4 marketing** — scale inventory and budget for September–December
4. **Upsell premium features to Home Office segment** — highest order value, lowest churn risk
5. **Retain Corporate contracts with service bundles** — most stable revenue stream

---

## 📌 Dataset

**Superstore Sales Dataset** — [Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)  
9,994 orders | 2014–2017 | US e-commerce data

---

## 👤 Author

**Muhammed Ammar Khan**  
Built as part of an end-to-end data analytics portfolio project.
