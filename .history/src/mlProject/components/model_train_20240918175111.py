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
        num_columns=['Age',
            'SystolicBP',
            'DiastolicBP',
            'BS',
            'BodyTemp',
            'HeartRate']    
        
        