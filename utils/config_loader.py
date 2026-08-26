import yaml
from logger.custom_logger import CustomLogger

def load_config(config_path:str = "config\config.yaml") -> dict:
    with open(config_path,"r") as file:
        config = yaml.safe_load(file)
    return config 



logger = CustomLogger().get_logger(__file__)
logger.info(load_config())
