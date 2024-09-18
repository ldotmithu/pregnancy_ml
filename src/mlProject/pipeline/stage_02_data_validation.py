from mlProject.components.data_validation import *
from mlProject.config.configuration import *
from mlProject.entity.config_entity import *


class DataValidationPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all()