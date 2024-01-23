import mlflow 

if __name__=="__main__":
    #start a new mlflow run
    mlflow.start_run()

    # Your machine learning code goes here
    # logging parameters or hyperparameters
    mlflow.log_param("learning_rate",0.01)

    #end the mlflow run
    mlflow.end_run()