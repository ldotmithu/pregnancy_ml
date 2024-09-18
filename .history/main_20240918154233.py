from mlProject.pipeline.stage_01_data_ingestion import *
from mlProject import logging

Stage_Name='Data Ingestion'
try:
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
    logging.info(f'{Stage_Name} Completed')
    
except Exception as e:
    logging.exception(e)
    raise e    