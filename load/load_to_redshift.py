import psycopg2
from config.redshift_config import REDSHIFT_CONFIG

def load_to_redshift(s3_key):
    conn = psycopg2.connect(
        host=REDSHIFT_CONFIG['host'],
        port=REDSHIFT_CONFIG['port'],
        user=REDSHIFT_CONFIG['user'],
        password=REDSHIFT_CONFIG['password'],
        database=REDSHIFT_CONFIG['database']
        

    )
    cursor = conn.cursor()

    # create table if not exists

    create_table_sql = """
    CREATE TABLE IF NOT EXISTS sales (
        order_id INT,
        order_date DATE,
        product_id INT,
        product_name VARCHAR(255),
        category_id INT,
        unit_price NUMERIC(10,2),
        quantity INT,
        total_sale NUMERIC(10,2),
        weekday VARCHAR(15),
        is_weekend BOOLEAN,
        order_month VARCHAR(10),
        order_quarter VARCHAR(5),
        order_year VARCHAR(4),
        high_value_order BOOLEAN,
        discount_flag BOOLEAN,
        product_type VARCHAR(100)
    );

"""
    cursor.execute(create_table_sql)


    # copy data from S3 (lakehouse)

    copy_sql = f"""
    COPY sales
    FROM 's3://{REDSHIFT_CONFIG["s3_bucket"]}/{s3_key}'
    IAM_ROLE '{REDSHIFT_CONFIG["iam_role"]}'
    IGNOREHEADER 1
    DELIMITER ','
    CSV;
    """
    cursor.execute(copy_sql)

    conn.commit()
    cursor.close()
    conn.close()

    print(f"Data loaded into Redshift table 'sales' from S3: {s3_key}")


