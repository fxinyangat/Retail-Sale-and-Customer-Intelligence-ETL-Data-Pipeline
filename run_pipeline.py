import argparse
from pipelines.daily_sales_pipeline import run_sales_pipeline
from pipelines.customer_segmentation_pipeline import run_customer_pipeline 

parser = argparse.ArgumentParser()
parser.add_argument('--pipeline', required=True, help="Which pipeline to run: 'sales' or 'customers'")
args = parser.parse_args()

if args.pipeline == "sales":
    run_sales_pipeline()
elif args.pipeline == "customers":
    run_customer_pipeline()
    
else:
    print("Invalid pipeline name. Use 'sales' or 'customers'")