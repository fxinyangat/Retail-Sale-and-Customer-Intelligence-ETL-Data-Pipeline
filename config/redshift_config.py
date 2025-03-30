REDSHIFT_CONFIG = {
    "host": "retail-etl-cluster.cqy7kya7yxbw.us-east-1.redshift.amazonaws.com",
    "port": 5439,
    "user": "admin",
    "password": "Admin12345678",
    "database": "dev",
    "table": "sales",
    "iam_role": "arn:aws:iam::390403886320:role/service-role/AmazonRedshift-CommandsAccessRole-20250329T151542",
    "s3_bucket":"xavier-etl-bucket",
    "s3_key": "etl/sales/daily_sales_2025-03-29.csv"


}