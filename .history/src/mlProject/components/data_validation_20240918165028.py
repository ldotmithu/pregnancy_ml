from mlProject.config.configuration import *
from mlProject import logging


class DataValidation:
    def __init__(self,config:DataValidationConfig) -> None:
        self.config=config
        