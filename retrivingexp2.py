import mlflow 
from mlflow_utils import get_mlflow_experiment

if __name__=="__main__":

    #retrieve the mlflow experiment
    ###### Please provide the experiment_id or experiment_name in the following line
    experiment = get_mlflow_experiment(experiment_id="302898995400525662")
    #printing the entire experiment object
    print("Complete Expiriment Object: {}".format(experiment))
    print("************************************************************************************************")
    print("Details of the expiriment object below: ")
    print("Name: {}".format(experiment.name))
    print("Experiment_id: {}".format(experiment.experiment_id))
    print("Artifact Location: {}".format(experiment.artifact_location))
    print("Tags: {}".format(experiment.tags))
    print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))
    print("Creation timestamp: {}".format(experiment.creation_time))