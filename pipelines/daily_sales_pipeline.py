from extract.extract_orders import extract_order_data
from transform.transform_sales import transform_sales_data
from load.load_to_s3 import load_to_s3
from load.load_to_redshift import load_to_redshift
import os
from datetime import datetime

def run_sales_pipeline():
    # Extract
    df = extract_order_data()

    # Transform
    transformed_df = transform_sales_data(df)

    # Save locally
    os.makedirs("output", exist_ok=True)
    today = datetime.today().strftime("%Y-%m-%d")
    filename = f"daily_sales_{today}.csv"
    filepath = os.path.join("output", filename)

    transformed_df.to_csv(filepath, index=False)

    # Load to S3
    s3_key = f"etl/sales/{filename}"
    load_to_s3(filepath, bucket_name="xavier-etl-bucket", s3_key=s3_key)

    # Load from s3 (lakehouse) to REdshift (datawarehouse)
    load_to_redshift(s3_key)