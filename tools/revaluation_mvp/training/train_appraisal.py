"""Train the appraisal network — entrypoint for `python -m training.train_appraisal`"""
from models.appraisal_network import train_appraisal_layer

if __name__ == "__main__":
    train_appraisal_layer()
