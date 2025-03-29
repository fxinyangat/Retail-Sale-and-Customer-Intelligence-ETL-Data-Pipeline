from sqlalchemy import create_engine
import pandas as pd
from config.db_config import DB_URI

def extract_order_data():
    engine = create_engine(DB_URI)

    query = """
        SELECT
        o.OrderID AS order_id,
        o.OrderDate AS order_date,
        od.ProductID AS product_id,
        p.ProductName AS product_name,
        p.CategoryID AS category_id,
        od.UnitPrice AS unit_price,
        od.Quantity AS quantity,
        (od.UnitPrice * od.Quantity) AS total_sale 
        from Orders o 	
        JOIN OrderDetails od ON o.OrderID = od.OrderID 
        JOIN Products p ON od.ProductID = p.ProductID

        """

    df = pd.read_sql(query, engine)
    print(f"Extracted {len(df)} sales records")
    return df