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
        
    def train_model(self):
        train_data=pd.read_csv(self.config.train_data_path)
        test_data=pd.read_csv(self.config.test_data_path)
        
        target_col='RiskLevel'
        
        X_train=train_data.drop(columns=target_col,axis=1)
        X_test=test_data.drop(columns=target_col,axis=1)
        y_train=train_data[target_col]
        y_test=test_data[target_col]
        
        