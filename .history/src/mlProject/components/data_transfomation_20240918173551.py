from mlProject.config.configuration import DataTransformationConfig
from mlProject import logging
import pandas as pd
from sklearn.model_selection import train_test_split
import os

class DataTransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config
        
    def read_status_file(self):
        try:
            with open(self.config.Status_file, 'r') as file:
                content = file.read().strip()
                return content == 'True'
        except FileNotFoundError:
            logging.error(f"Status file not found: {self.config.Status_file}")
            raise
        except Exception as e:
            logging.exception(e)
            raise
    
    def split_data(self):
        try:
            # Read status from file
            status = self.read_status_file()
            
            if status:
                # Load data
                data = pd.read_csv(self.config.data_path)
                logging.info('Read the data through pandas read_csv')
                
                # Split data
                train_data, test_data = train_test_split(data, test_size=0.2)
                
                # Save data
                train_data.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
                test_data.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)
                
                logging.info('Split the Data into Train and Test')
                logging.info(f'Train Data Shape: {train_data.shape}')
                logging.info(f'Test Data Shape: {test_data.shape}')
                
            else:
                logging.info('Validation status is False. Check your status file.')
        
        except Exception as e:
            logging.exception(e)
            raise e

                    
                
                
            
                   