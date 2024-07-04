import pandas as pd
import numpy as np
import logging
from exception.exceptiontests.unit.exception import customexception

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path
from utils.utils import read_data

parent_dir = os.path.dirname(os.getcwd())
data_path = "Gem-stone-price-prediction-End-to-End-MLpipeline\Gemstone-Price-Prediction-End-to-End-ML-pipeline\data"

@dataclass
class DataIngestionConfig():
    raw_data_path:str = os.path.join("artifacts","raw.csv")
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")

class DataIngestion():
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("data ingestion started")
        try:
            data= read_data(parent_dir+data_path+"\cubic_zirconia.csv")
            logging.info("read as df")

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info(" i have saved the raw dataset in artifact folder")

            logging.info("Here I have performed the train test split")

            train_data,test_data = train_test_split(data,test_size=0.25)
            logging.info("train test completed")

            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)

            logging.info("Data Ingestion completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.info("logging the exception")
            raise customexception(e,sys)
        


if __name__=="__main__":
    obj = DataIngestion()

    obj.initiate_data_ingestion()
 






