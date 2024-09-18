from mlProject.config.configuration import *
from mlProject import logging
import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

class ModelTrain:
    def __init__(self,config:ModelTrainConfig):
        self.config=config
        
    def preprocess_method(self):
        try:
            num_columns=['Age',
                'SystolicBP',
                'DiastolicBP',
                'BS',
                'BodyTemp',
                'HeartRate']    
            
            num_pipeline=Pipeline([
                ('scale',StandardScaler())
            ])

            Preproess=ColumnTransformer([
                ('num_columns',num_pipeline,num_columns)
            ])
            return Preproess
        
        except Exception as e:
            logging.exception(e)
            raise e