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
        
        create_directories([config.root_dir])    