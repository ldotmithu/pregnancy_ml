from mlProject.config.configuration import *
from sklearn.metrics import accuracy_score
import pandas as pd 
from mlProject.utils.common import *

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config
        
    def eval_metrics(self,actual,pred):
        acc_score=accuracy_score(actual,pred)
        
        return acc_score
    
    def save_metrics(self):
        test_data=pd.read_csv(self.config.test_data_path)
        
        
        target_col='RiskLevel'
        X_test=test_data.drop(columns=target_col,axis=1) 
        y_test=test_data[target_col]
        