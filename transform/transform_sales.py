import pandas as pd

def transform_sales_data(df):
    # Convert to datetime
    df["order_date"] = pd.to_datetime(df["order_date"])

    # Round price columns
    df["unit_price"] = df["unit_price"].round(2)
    df["total_sale"] = df["total_sale"].round(2)

    # New column: Add day of week and is_weekend
    df["weekday"] = df["order_date"].dt.day_name()
    df["is_weekend"] = df["order_date"].dt.weekday >= 5

    # New column: Add order month and quarter
    df["order_year"] = df["order_date"].dt.year.astype(str)      
    df["order_month"] = df["order_date"].dt.month.apply(lambda m: f"{m:02}")  
    df["order_quarter"] = df["order_date"].dt.quarter.apply(lambda q: f"Q{q}")

    # New col: High value flag
    df["high_value_order"] = df["total_sale"] > 500

    # New col: discount flag
    # unit_price < 20 = likely discounted
    df["discount_flag"] = df["unit_price"] < 20

    # New col: Product type based on category
    category_map = {
        1: "Beverages",
        2: "Condiments",
        3: "Confections",
        4: "Dairy Products",
        5: "Grains/Cereals",
        6: "Meat/Poultry",
        7: "Produce",
        8: "Seafood"
    }
    df["product_type"] = df["category_id"].map(category_map).fillna("Other")

    return df