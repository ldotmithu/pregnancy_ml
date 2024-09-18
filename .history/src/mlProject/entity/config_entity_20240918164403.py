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