from mlProject.components.data_transfomation import *
from mlProject.config.configuration import *
from mlProject import logging

class DataTransfomationPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=ConfigurationManager()
        data_transfomation_config=config.get_data_transfomation_config()
        data_transfomation=DataTransformation(config=data_transfomation_config)
        data_transfomation.read_status_file()
        data_transfomation.split_data()