import os
import boto3
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_execution import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml

logger = get_logger(__name__)

# class for Data Ingestion
class DataIngestion:

    def __init__(self, config):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config['bucket_name']
        self.file_name = self.config['bucket_file_name']
        self.train_test_ratio = self.config['train_ratio']
        self.aws_config = config["aws"]

        os.makedirs(RAW_DIR, exist_ok=True)

        logger.info(f"Data Ingestion started with {self.bucket_name} and file is {self.file_name}")

    def download_csv_from_aws_s3(self):
        try:
            # Initialize boto3 S3 client with credentials from YAML
            s3_client = boto3.client(
                service_name='s3',
                region_name=self.aws_config['default_region'],
                aws_access_key_id=self.aws_config['access_key_id'],
                aws_secret_access_key=self.aws_config['secret_access_key']
            )

            # Download the file from S3
            s3_client.download_file(self.bucket_name, self.file_name, RAW_FILE_PATH)

            logger.info(f"CSV file is successfully downloaded to {RAW_FILE_PATH}")

        except Exception as e:
            logger.error("Error while downloading the csv file from S3")
            raise CustomException("Failed to download the csv file from S3", e)
        
    def split_data(self):
        try:
            logger.info("Starting the splitting process")
            data = pd.read_csv(RAW_FILE_PATH)

            # splitting the data
            train_data, test_data = train_test_split(data, test_size=1-self.train_test_ratio, random_state=42)

            # storing both dataset
            train_data.to_csv(TRAIN_FILE_PATH)
            test_data.to_csv(TEST_FILE_PATH)

            logger.info(f'Train data saved to {TRAIN_FILE_PATH}')
            logger.info(f'Test data saved to {TEST_FILE_PATH}')

        except Exception as e:
            logger.error('Error while splitting data')
            raise CustomException("Failed to Split data into Train and Test sets", e)
        
    def run(self):
        try:
            logger.info("Starting Data Ingestion Process")

            self.download_csv_from_aws_s3()
            self.split_data()

            logger.info("Data Ingestion completed successfully")

        except CustomException as ce:
            logger.error(f"CustomException: {str(ce)}")

        finally:
            logger.info("Data Ingestion Completed")


if __name__ == "__main__":

    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()