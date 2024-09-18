from mlProject.config.configuration import *
from sklearn.metrics import accuracy_score
import pandas as pd 
from mlProject.utils.common import *
import numpy as np
from pathlib import Path

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config
        
    def eval_metrics(self,actual,pred):
        acc_score=accuracy_score(actual,pred)
        
        return acc_score
    
    def save_metrics(self):
        test_data=pd.read_csv(self.config.test_data_path)
        '''
        conditions = [
            (test_data['RiskLevel'] == 'high risk'),
            (test_data['RiskLevel'] == 'mid risk'),
            (test_data['RiskLevel'] == 'low risk')
        ]

        values = [2, 1, 0]

        test_data['RiskLevel'] = np.select(conditions, values)
        '''
        
        target_col='RiskLevel'
        X_test=test_data.drop(columns=target_col,axis=1) 
        y_test=test_data[target_col]
        
        preprocess_obj=joblib.load(self.config.preprocess_file)
        model=joblib.load(self.config.model_file)
       
        X_test=preprocess_obj.transform(X_test)
        pred=model.predict(X_test)
        
        acc_score=self.eval_metrics(y_test,pred)        
        
        score={'acc_score':acc_score}
        
        save_json(Path(self.config.metrics_file), data=score)
        