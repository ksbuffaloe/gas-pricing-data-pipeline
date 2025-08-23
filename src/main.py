from ingest_api import run_ingest
from run_transform import run_transform
import logging
import os
import traceback

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

def run_pipeline():
    try:
        print("Starting data ingestion...")
        run_ingest()
        print("Data ingestion completed successfully!")
        logging.info("Data ingestion completed")

        print("Starting data transformation...")
        run_transform()
        print("Data transformation completed successfully!")
        logging.info("Data transformation completed")
    except Exception as e:
        logging.exception("Pipeline failed due to error:")
        print(f"Pipeline failed: {e}")
        # Optional: write to a fallback file if logging fails
        with open(os.path.join(current_dir, "pipeline_fallback.log"), "a") as f:
            f.write(traceback.format_exc())

if __name__ == "__main__":
    try:
        run_pipeline()
        print("Data pipeline completed successfully!")
    except Exception as e:
        print(f"Data pipeline failed: {e}")

