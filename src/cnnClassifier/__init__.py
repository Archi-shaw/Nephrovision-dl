import os 
import sys
import logging 

logging_str = ['%(asctime)s' , '%(levelname)s' , '%(name)s']

log_dir = "logs"
log_file = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=' - '.join(logging_str),
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)


logger = logging.getLogger('cnnClassifier')
