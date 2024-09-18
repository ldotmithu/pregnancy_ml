from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir:Path
    URL:str
    loacl_data_path:Path
    unzip_dir:Path
    
@dataclass
class DataValidationConfig:
    root_dir:Path
    unzip_dir:Path
    Status_file: Path  
    all_schema: dict
    
@dataclass
class DataTransformationConfig:
    root_dir:Path
    data_path:Path
    Status_file:Path  
    
@dataclass
class ModelTrainConfig:
    root_dir:Path
    train_data_path:Path
    test_data_path:Path
    model_file:Path
    preprocess_file:Path
    
      