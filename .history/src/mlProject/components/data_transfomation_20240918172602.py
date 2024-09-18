from mlProject.config.configuration import *
from mlProject import logging
import pandas as pd 
from sklearn.model_selection import train_test_split

class DataTransformation:
    def __init__(self,config:DataTransformationConfig) -> None:
        self.config=config
        
    def split_data(self):
        try:
            status=self.config.Status_file.value() 
            if status == True:
                data=pd.read_csv(self.config.data_path)
        
        except:
            pass        
                
                
            
                   