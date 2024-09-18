from mlProject.config.configuration import *
from mlProject import logging
import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from imblearn.combine import SMOTETomek, SMOTEENN
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
from sklearn.metrics import accuracy_score

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
        y_train=train_data[self.config.Target_column]
        y_test=test_data[self.config.Target_column]
        
        import numpy as np

        conditions = [
            (y_train['RiskLevel'] == 'high risk'),
            (y_train['RiskLevel'] == 'mid risk'),
            (y_train['RiskLevel'] == 'low risk')
        ]

        values = [2, 1, 0]

        y_train['RiskLevel'] = np.select(conditions, values)
        
        conditions = [
            (y_test['RiskLevel'] == 'high risk'),
            (y_test['RiskLevel'] == 'mid risk'),
            (y_test['RiskLevel'] == 'low risk')
        ]

        values = [2, 1, 0]

        y_test['RiskLevel'] = np.select(conditions, values)
        
        preprocess_obj=self.preprocess_method()
        
        X_train=preprocess_obj.fit_transform(X_train)
        X_test=preprocess_obj.transform(X_test)
        
        #smt = SMOTEENN(random_state=42,sampling_strategy='minority' )
        # Fit the model to generate the data.
        #X_train, y_train = smt.fit_resample(X_train, y_train)
        
        rfc=RandomForestClassifier(n_estimators=self.config.n_estimators,criterion=self.config.criterion,random_state=42)
        rfc.fit(X_train,y_train)
        
        joblib.dump(rfc,os.path.join(self.config.root_dir,self.config.model_file))
        
        joblib.dump(preprocess_obj,os.path.join(self.config.root_dir,self.config.preprocess_file))
        
        pred=rfc.predict(X_test)
        logging.info(accuracy_score(y_test,pred))
        
        
        
        
        
        