from extract.extract_customers import extract_customer_data
from transform.transform_segments import transform_customer_data
from load.load_to_s3 import load_to_s3
import os
from datetime import datetime

def run_customer_pipeline():
    # Extract
    df = extract_customer_data()

    # Transform
    transformed_df = transform_customer_data(df)

    # Save to file
    os.makedirs("output", exist_ok=True)
    today = datetime.today().strftime("%Y-%m-%d")
    filename = f"customer_segments_{today}.csv"
    filepath = os.path.join("output", filename)

    transformed_df.to_csv(filepath, index=False)

    # Upload to S3
    s3_key = f"etl/customers/{filename}"
    load_to_s3(filepath, bucket_name="xavier-etl-bucket", s3_key=s3_key)