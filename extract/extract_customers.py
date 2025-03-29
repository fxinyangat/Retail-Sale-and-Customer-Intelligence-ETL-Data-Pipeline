from sqlalchemy import create_engine
import pandas as pd
from config.db_config import DB_URI

def extract_customer_data():
    engine = create_engine(DB_URI)

    query = """
        SELECT 
            c.CustomerID AS customer_id,
            c.CompanyName AS company_name,
            c.Country AS country,
            o.OrderID AS order_id,
            o.OrderDate AS order_date,
            od.UnitPrice AS unit_price,
            od.Quantity AS quantity,
            (od.UnitPrice * od.Quantity) AS line_total
        FROM Customers c
        JOIN Orders o ON c.CustomerID = o.CustomerID
        JOIN OrderDetails od ON o.OrderID = od.OrderID
    """

    df = pd.read_sql(query, engine)
    print(f"Extracted {len(df)} customer transaction records")
    return df