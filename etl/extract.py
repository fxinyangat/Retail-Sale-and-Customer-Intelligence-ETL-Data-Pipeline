import pandas as pd
from sqlalchemy import create_engine
from config.db_config import DB_URI

# DB_URI = "mysql+pymysql://eda2025:msba@cis505-shi.cloud.wpcarey.asu.edu:3306/Northwind"



def extract_data(query):
    engine = create_engine(DB_URI)
    df = pd.read_sql(query, engine)
    print("Data extracted successfully.")
    print(df.head())
    print(df.columns)
    return df
