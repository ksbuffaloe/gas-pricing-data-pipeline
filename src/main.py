from ingest_api import run_ingest
from run_transfrom import run_transform

def run_pipeline():
    print("Starting data ingestion...")
    run_ingest()
    print("Data ingestion completed successfully!")

    print("Starting data transformation...")
    run_transform()
    print("Data transformation completed successfully!")

#run the pipeline
if __name__ == "__main__":
    run_pipeline()
    print("Data pipeline completed successfully!")
    

