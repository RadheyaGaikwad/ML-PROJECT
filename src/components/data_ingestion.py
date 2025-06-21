import os 
import sys
from src.exception import CustomException
from src.logger import logging    
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass



# ---------------------------------------------------------------
# DataIngestionConfig is a configuration class for managing file
# paths used during the data ingestion process. It stores default
# locations for:
# - raw_data_path: the original full dataset (before splitting)
# - train_data_path: the dataset used to train the model
# - test_data_path: the dataset used to evaluate the model
# These paths are automatically created using os.path.join to
# ensure compatibility across different operating systems.
# ---------------------------------------------------------------

@dataclass
class DataIngestionConfig:
    train_data_path: str= os.path.join('artifacts','train.csv')
    test_data_path: str= os.path.join('artifacts','test.csv')
    raw_data_path: str= os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config= DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv(os.path.join('notebook','data','stud.csv'))
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path 
            )
        
        except Exception as e:
         raise CustomException(e, sys) from e
        logging.info("Exiting the data ingestion method or component")

if __name__ == "__main__":
    obj= DataIngestion()
    obj.initiate_data_ingestion()
    print("Data Ingestion Completed")