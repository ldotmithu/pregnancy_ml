from mlProject.config.configuration import *
from mlProject import logging
import pandas as pd 


class DataValidation:
    def __init__(self,config:DataValidationConfig) -> None:
        self.config=config
        
    def validate_all(self):
        try:
            validation_status = None
            
            data=pd.read_csv(self.config.unzip_dir)
            
            all_col=list(data.columns)
            
            all_schema=self.config.all_schema.keys()
            
            for col in all_col:
                if col not in all_schema:
                    validation_status=False
                    with open(self.config.Status_file,'w') as f:
                        f.write(f'Validation_Status : {validation_status}')
                        logging.info(f'Validation_Status : {validation_status}')
                        
                else:
                    validation_status=True
                    with open(self.config.Status_file,'w') as f:
                        f.write(f'Validation_Status : {validation_status}')    
                        logging.info(f'Validation_Status : {validation_status}')
                        
        except Exception as e:
            logging.exception (e)
            raise e                                       
               