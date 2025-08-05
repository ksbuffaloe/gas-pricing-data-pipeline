from ingest_api import run_ingest
from run_transfrom import run_transform
import logging
import os
from datetime import datetime

# Get the directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(current_dir, "pipeline.log")

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logging.info("Pipeline run started")

# This script runs the data pipeline by running both the ingestion and transformation steps.
def run_pipeline():
    # Start the data ingestion process 
    print("Starting data ingestion...")
    run_ingest()
    print("Data ingestion completed successfully!")
    
    # Start the data transformation process
    print("Starting data transformation...")
    run_transform()
    print("Data transformation completed successfully!")

#run the pipeline
if __name__ == "__main__":
    run_pipeline()
    print("Data pipeline completed successfully!")
    

