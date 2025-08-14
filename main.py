import pandas as pd
from sqlalchemy import create_engine, text  

USERNAME = 'postgres'
PASSWORD = 'admin123'
HOST = 'localhost'
PORT = '5432'   
DATABASE = 'sales'

engine = create_engine(f'postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')
con = engine.connect()
create_table_query = """
CREATE TABLE IF NOT EXISTS staging_sales (
    "InvoiceNo" TEXT,
    "StockCode" TEXT,
    "Description" TEXT,
    "Quantity" INTEGER,
    "InvoiceDate" TIMESTAMP,
    "UnitPrice" NUMERIC,
    "CustomerID" TEXT,
    "Country" TEXT,
    "TotalPrice" NUMERIC
);
"""

with engine.connect() as conn:
    conn.execute(text(create_table_query))
    conn.commit()
    print("Table 'staging_sales' created successfully.")

df = pd.read_csv("data/data.csv", encoding='latin1')

df = df.dropna(subset=['CustomerID'])
df = df[df['Quantity'] > 0]
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M')
df['Country'] = df['Country'].str.strip()
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

df.to_sql('staging_sales', engine, if_exists='replace', index=False)
print("Data loaded into 'staging_sales' table successfully.")