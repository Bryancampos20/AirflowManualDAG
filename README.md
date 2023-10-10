# Apache Airflow HelloWorld DAG

Hello, everyone! 👋

My name is Bryan Campos Castro, and I am a computer engineer currently working as a full-stack developer.

## About the Project

This project demonstrates how to create a simple workflow using Apache Airflow. The workflow consists of three tasks: a start task **(Start_task)**, a task that prints "Hello, world!" to the console **(Hello_task)**, and an end task **(End_task)**.

## Requirements

Before running this workflow, make sure you have the following requirements installed:

- **Docker**
- **Python**

## Question

Airflow can run jobs on a schedule but what if we need to do and an-hoc one time run with unique input parameters/variables? How do we do that?
e.g. if we have an Airflow job set up to sync data for all users but one day we want to just sync data for one specific user?

## Answer

In Apache Airflow, you can use "Manual DAGs" to run jobs ad hoc with unique parameters or variables. To do this, you can follow these steps:

1. Define a new manual DAG that represents the job you want to run ad hoc. In this DAG, you can define the unique parameters or variables as arguments. 
2. Use the Apache Airflow web interface or the command line to manually trigger the execution of that specific DAG. 
3. When activating the manual DAG, you can provide the necessary unique parameters or variables at that specific moment. 
4. The manual DAG will execute with the parameters or variables you have provided and complete the job ad hoc.

In this example: 
* We have created a DAG called 'ad_hoc_sync_job' that has no automatic scheduling interval (schedule_interval=None). 
* We defined a Dummy task called 'start' that acts as the starting point for the DAG. Then, we defined a PythonOperator task called 'sync_data' that will execute the ad hoc job.
* We pass the specific user's ID as an argument using op_args. 
* Finally, we set a dependency of type start_task >> sync_data_task so that the DAG begins with the Dummy task and then executes the data synchronization job for the specific user.

## Execution

1. Start the containers using the following command:
```bash
docker-compose -f docker-compose-LocalExecutor.yml up -d
```
2. This way, you will have Airflow running on port 8080.

## Results

![Screenshot (160)](https://github.com/Bryancampos20/ApacheAirflow/blob/main/results/result.png)

Happy coding! 🚀