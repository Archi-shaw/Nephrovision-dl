from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_data_file: Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int

@dataclass(frozen=True)
class TrainingConig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    training_data: Path
    params_batch_size: int
    params_epochs: int
    params_is_argumentation: bool


@dataclass(frozen=True)
class EvaluateConfig:
    path_of_model: Path
    training_data: Path
    params_image_size: list
    all_params: dict
    params_batch_size: int
    mlfow_url: str  
