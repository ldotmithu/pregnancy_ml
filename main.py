from mlProject.pipeline.stage_01_data_ingestion import *
from mlProject.pipeline.stage_02_data_validation import *
from mlProject.pipeline.stage_03_data_transfomation import *
from mlProject.pipeline.stage_04_model_train import *
from mlProject.pipeline.stage_05_model_evaluation import *
from mlProject import logging

Stage_Name='Data Ingestion'
try:
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
    logging.info(f'{Stage_Name} Completed')
    
except Exception as e:
    logging.exception(e)
    raise e    


Stage_Name='Data Validation'
try:
    data_validation=DataValidationPipeline()
    data_validation.main()
    logging.info(f'{Stage_Name} Completed')
    
except Exception as e:
    logging.exception(e)
    raise e 

Stage_Name='Data Transfomation'
try:
    data_transfomation=DataTransfomationPipeline()
    data_transfomation.main()
    logging.info(f'{Stage_Name} Completed')
    
except Exception as e:
    logging.exception(e)
    raise e 

Stage_Name='Model Train'
try:
    model_train=ModelTrainPipeline()
    model_train.main()
    logging.info(f'{Stage_Name} Completed')
    
except Exception as e:
    logging.exception(e)
    raise e 

Stage_Name='Model Evaluation'
try:
    model_evaluation=ModelEvaluationPipeline()
    model_evaluation.main()
    logging.info(f'{Stage_Name} Completed')
    
except Exception as e:
    logging.exception(e)
    raise e 