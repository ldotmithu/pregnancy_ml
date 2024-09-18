from mlProject.components.model_train import *
from mlProject.config.configuration import *



class ModelTrainPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=ConfigurationManager()
        model_train_config=config.get_model_train_config()
        model_train=ModelTrain(config=model_train_config)
        model_train.preprocess_method()
        model_train.train_model()