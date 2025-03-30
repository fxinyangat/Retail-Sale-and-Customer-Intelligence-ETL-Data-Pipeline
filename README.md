# Retail Sales & Customer Intelligence Data Pipeline

## Executive Summary

This project implements two enterprise-grade data pipelines for a retail company, ABX Retail Group (Not a real name), which operates across North America and Latin America. The pipelines automate the secure movement, transformation, and delivery of high-value business data from a MySQL transactional database into a cloud-based data lake (Amazon S3), and further into a structured data warehouse (Amazon Redshift).


The architecture used reflects a real-world, end-to-end data engineering solution capable of supporting operational reporting, customer analytics, and future machine learning workloads. It demonstrates the ability to integrate disparate systems, apply business logic through code, and deliver high-quality data products in cloud environments.


These pipelines are designed to deliver near-real-time visibility into sales performance and customer behavior, empowering executives, analysts, and data science teams to make timely and informed decisions around marketing, inventory, financial forecasting, and customer lifecycle management.






## Business Value

### 1. Daily Sales Reporting Pipeline
- **Purpose**: Track revenue, order volume, and product performance across categories, regions, and time.
- **Stakeholders**: Sales leadership, finance teams, inventory planners.
- **Outcome**: Enables daily revenue tracking, product demand forecasting, and inventory optimization.

### 2. Customer Segmentation Pipeline
- **Purpose**: Classify customers into behavioral segments (e.g., VIP, Loyal, At-Risk) using RFM (Recency, Frequency, Monetary) scoring models.
- **Stakeholders**: Marketing, CRM teams, customer retention analysts.
- **Outcome**: Supports targeted marketing campaigns, personalized offers, and churn mitigation strategies.



## Data Architecture Overview

- **Source System**: Relational MySQL database storing transactional and customer data.
- **ETL Processing Engine**: Python using 'pandas' for fast, scalable in-memory transformations.
- **Data Lake**: Amazon S3 stores transformed datasets in analytics-ready '.csv' format.
- **Data Warehouse**: Amazon Redshift stores structured and query-optimized datasets for downstream BI/SQL consumption.
- **Modular Project Design**: Extraction, transformation, and loading stages are fully decoupled for maintainability and extensibility.



## Pipeline Overview

### Daily Sales Reporting

| Metric              | Description                                |
|---------------------|--------------------------------------------|
| Total Sales         | Daily revenue aggregated by product/date   |
| Units Sold          | Quantity sold by product and category      |
| High-Value Orders   | Orders flagged based on business thresholds |
| Time Features       | Derived fields like weekday, weekend flag, month, quarter |
| Product Type        | Enriched category mapping per sale record  |

### Customer Segmentation

| Metric              | Description                                |
|---------------------|--------------------------------------------|
| Recency             | Days since last order                      |
| Frequency           | Number of orders placed                    |
| Monetary Value      | Total spend across all orders              |
| RFM Score           | Combined score for segmentation            |
| Segment             | Rule-based labels (VIP, Loyal, At-Risk)    |
| Region/Country      | Geo-intelligence for customer targeting    |



## Technologies Used

- **Python 3.12**
- **SQLAlchemy** + **pymysql** – MySQL database connector
- **pandas** – Data transformations and enrichment
- **boto3** – AWS SDK for Python (upload to Amazon S3)
- **Amazon S3** – Raw and curated storage layer (data lake)
- **Amazon Redshift** – Scalable data warehouse for analytical workloads
- **psycopg2** – PostgreSQL-compatible Redshift loader (COPY from S3)
- **AWS IAM + Roles** – Secure S3 → Redshift copy permissions



## Architecture Overview

This project implements a modular, cloud-native data pipeline that extracts operational data from a MySQL relational database, transforms it using Python, and loads it into both Amazon S3 (serving as a data lake) and Amazon Redshift (serving as a structured data warehouse for analytics). The architecture is designed to support scalable, extensible, and production-ready data processing workflows.

**Data Flow and Components**

1. Source System – MySQL Relational Database
The pipeline ingests data from a normalized MySQL database containing transactional and customer-related tables including Orders, OrderDetails, Products, and Customers. These tables serve as the foundation for both the sales analytics and customer segmentation pipelines.

2. Extraction Layer – SQLAlchemy and PyMySQL
Data is extracted from the MySQL database using SQLAlchemy with PyMySQL as the database driver. Each dataset is pulled through dedicated extract modules, ensuring clarity and reusability. The connection configuration is securely externalized.

3. Transformation Layer - Python
Extracted data is transformed using pandas for efficient in-memory data manipulation. Key transformations include:
- Time-based feature engineering (e.g., order month, quarter, weekday)
- Business-rule-based flags (e.g., high-value orders, weekend transactions)
- RFM (Recency, Frequency, Monetary) scoring and segmentation logic for customer classification
Each pipeline has a dedicated transformation script to isolate business logic.

4. Data Lake Layer – Amazon S3
Transformed datasets are exported in CSV format and uploaded to Amazon S3 under designated prefixes (etl/sales/, etl/customers/). S3 acts as a centralized storage layer, enabling downstream integration with analytics tools, query engines, or data catalog services.

5. Data Warehouse Layer – Amazon Redshift
For sales data, the pipeline supports loading into Amazon Redshift. This is achieved via the Redshift COPY command, pulling directly from S3. This layer enables fast, SQL-based querying and compatibility with BI tools like Power BI, Alteryx or Tableau.

6. Configuration and Modularity
All connection details and runtime parameters are defined in external configuration files. The project follows a modular structure with separate folders for extraction, transformation, and loading stages. A centralized entrypoint (run_pipeline.py) enables execution of individual pipelines using command-line arguments, improving usability and maintainability.

Design Characteristics
- Modular and Decoupled: Each pipeline stage (extract, transform, load) is independently maintained and testable.
- Extensible: Additional pipelines or destinations (e.g., Snowflake, BigQuery, Athena) can be added with minimal refactoring.
- Cloud-Native: Utilizes AWS-native services (S3, Redshift, IAM) and follows best practices in credential and resource management.
- Production-Ready: Designed for automation and monitoring. Suitable for integration with orchestration tools such as Apache Airflow or AWS Step Functions.

