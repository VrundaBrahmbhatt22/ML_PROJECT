import sys
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    print(">>> Data ingestion started")
    logging.info("The execution has started")

    try:
        data_ingestion = DataIngestion()
        df = data_ingestion.initiate_data_ingestion()  # ✅ Returns only df now

        print("\n>>> Sample data:")
        print(df.head())  # ✅ Show a preview of the data

    except Exception as e:
        logging.info("Custom exception occurred")
        raise CustomException(e, sys)
