# Retail Sales & Customer Intelligence Data Pipeline

## Executive Summary

This project implements two enterprise-grade data pipelines for a retail company, ABX Retail Group (Not Real name), which operates across North America and Latin America. The pipelines automate the movement, transformation, and delivery of high-value business data from an operational MySQL data source into a secure cloud-based data lake on AWS.

The goal is to provide near-real-time visibility into sales performance and customer behavior, enabling executives, analysts, and data science teams to make informed decisions on marketing, inventory, and operations.


## Business Value

### 1. Daily Sales Reporting Pipeline
- **Purpose**: Track revenue, order volume, and product performance across categories and regions.
- **Stakeholders**: Sales leadership, finance teams, inventory planners.
- **Outcome**: Enables daily revenue visibility, demand forecasting, and inventory optimization.

### 2. Customer Segmentation Pipeline
- **Purpose**: Classify customers into behavioral segments (VIP, Loyal, At-Risk, etc.) using RFM (Recency, Frequency, Monetary) metrics.
- **Stakeholders**: Marketing, CRM teams, customer retention analysts.
- **Outcome**: Supports targeted campaigns, personalized offers, and churn reduction strategies.


## Data Architecture Overview

- **Source**: Relational MySQL database with operational data (orders, products, customers, shipping).
- **Transformation Engine**: Python with 'pandas' for in-memory data shaping, feature engineering, and enrichment.
- **Storage Layer**: Amazon S3 for durable, scalable cloud storage in analytics-ready formats.
- **Modular Design**: Extract, transform, and load (ETL) stages are fully decoupled for scalability and reuse.

---

## Pipeline Overview

### Daily Sales Reporting

| Metric              | Description                                |
|---------------------|--------------------------------------------|
| Total Sales         | Daily revenue aggregated by product/date   |
| Units Sold          | Quantity sold by product and category      |
| Average Order Value | Sales per order                            |
| Top Performing SKUs | Based on revenue or volume                 |

### Customer Segmentation

| Metric              | Description                                |
|---------------------|--------------------------------------------|
| RFM Score           | Customer recency, frequency, monetary value|
| Segment             | Classified into segments like VIP, At-Risk |
| Lifetime Value (LTV)| Aggregated spend per customer              |
| Region/Country      | Geographic distribution of segments        |

---

## Technologies Used

- **Python 3.12**
- **SQLAlchemy** and **pymysql** for secure DB access
- **Pandas** for data manipulation and feature engineering
- **Boto3** for AWS S3 file uploads
- **MySQL** as the source system of record
- **Amazon S3** as the cloud storage destination

---

## Setup Instructions

### 1. Clone the repository and set up environment

git clone https://github.com/fxinyangat/Retail-Sale-and-Customer-Intelligence-ETL-Data-Pipeline.git
cd sql_to_s3_etl
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt