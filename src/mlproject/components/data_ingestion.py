import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.mlproject.exception import CustomException
from src.mlproject.logger import logging


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Starting data ingestion process.")

            # ✅ Reading the data from a local CSV file (adjust path if needed)
            df = pd.read_csv(os.path.join('notebook', 'data', 'raw.csv'))
            logging.info("Successfully read dataset from CSV file.")

            # ✅ Create artifacts directory if not exists
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # ✅ Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Raw data saved.")

            # ✅ Split the data
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Train-test split completed and files saved.")

            logging.info("Data ingestion process completed successfully.")
            
            # ✅ Return the original DataFrame for preview in app.py
            return df

        except Exception as e:
            logging.error("Exception occurred during data ingestion", exc_info=True)
            raise CustomException(e, sys)
