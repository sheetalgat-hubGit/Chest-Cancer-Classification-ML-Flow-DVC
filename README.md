# Chest-Cancer-Classification-ML-Flow-DVC
## Workflows
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml


## dagshub
[dagshub]: (https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/sheetalgat-hubGit/Chest-Cancer-Classification-ML-Flow-DVC.mlflow
MLFLOW_TRACKING_USERNAME=sheetalgat-hubGit
MLFLOW_TRACKING_PASSWORD=ba0acb0afe77309e57b59eb42402a42d625db7a3
python script.py

Run this to export as env variables:

export MLFLOW_TRACKING_URI=https://dagshub.com/sheetalgat-hubGit/Chest-Cancer-Classification-ML-Flow-DVC.mlflow
export MLFLOW_TRACKING_USERNAME=sheetalgat-hubGit
export MLFLOW_TRACKING_PASSWORD=ba0acb0afe77309e57b59eb42402a42d625db7a3


About MLflow & DVC
MLflow

Its Production Grade
Trace all of your expriements
Logging & taging your model
DVC

Its very lite weight for POC only
lite weight expriements tracker
It can perform Orchestration (Creating Pipelines)