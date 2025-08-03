from ingest_api import run_ingest
from run_transfrom import run_transform

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
    

