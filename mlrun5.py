import mlflow 

if __name__=="__main__":

# we use with in order to not write the mlflow.run_end() function
    with mlflow.start_run(run_name="mlflow_runs") as run:

        # Your machine learning code goes here
        # logging parameters or hyperparameters
        mlflow.log_param("learning_rate",0.01)
        print("RUN ID")
        print(run.info.run_id) # printing the current run id

        print(run.info) # printing the current run info