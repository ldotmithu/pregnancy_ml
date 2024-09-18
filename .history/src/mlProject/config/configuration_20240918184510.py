from src.mlProject.entity.config_entity import *
from mlProject.constants import *
from mlProject import logging
from mlProject.utils.common import *

class ConfigurationManager:
    def __init__(self):
        self.config=read_yaml(CONFIG_FILE_PATH)
        self.schema=read_yaml(SCHEMA_FILE_PATH)
        self.params=read_yaml(PARAMS_FILE_PATH)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self):
            config=self.config.data_ingestion
            
            create_directories([config.root_dir])
            
            data_ingestion_config=DataIngestionConfig(
                root_dir=config.root_dir,
                URL=config.URL,
                loacl_data_path=config.loacl_data_path,
                unzip_dir=config.unzip_dir
            )
            
            return data_ingestion_config
        
    def get_data_validation_config(self):
        config=self.config.data_validation
        schema=self.schema.Columns
        
        create_directories([config.root_dir])
        
        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            unzip_dir=config.unzip_dir,
            Status_file=config.Status_file,
            all_schema=schema
        )    
        
        return data_validation_config
    
    def get_data_transfomation_config(self):
        config=self.config.data_transfomation
        
        create_directories([config.root_dir])
        
        data_transfomation_config=DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            Status_file=config.Status_file
            
        )
        return data_transfomation_config
    
    def get_model_train_config(self):
        config=self.config.model_train
        params=self.params.RandomForestClassifier
        schema=self.schema.Target_column
        
        create_directories([config.root_dir])
        
        model_train_config=ModelTrainConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_file=config.model_file,
            preprocess_file=config.preprocess_file,
            n_estimators=params.n_estimators,
            criterion=params.criterion,
            Target_column=schema.name
        )
        return model_train_config
    
    def get_model_evaluation_config(self):
        config=self.config.model_evaluation
        schema=self.schema.Target_column
        
        create_directories([config.root_dir])
        
        
        