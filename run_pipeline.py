from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_to_s3
import os

def main():
    query = "SELECT * FROM Customers"

    df = extract_data(query)
    transformed_df = transform_data(df)

    # Save to local CSV
    os.makedirs("output", exist_ok=True)
    output_file = "output/final_data_v2.csv"
    transformed_df.to_csv(output_file, index=False)

    # Upload to S3
    load_to_s3(output_file, "xavier-etl-bucket", "etl/final_data.csv")

if __name__ == "__main__":
    main()