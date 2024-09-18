from mlProject.config.configuration import *
from mlProject import logging

class DataTransformation:
    def __init__(self,config:DataIngestionConfig) -> None:
        self.config=config
        
        