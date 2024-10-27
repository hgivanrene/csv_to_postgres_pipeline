# csv_to_postgres_pipeline

## Description
This repository is for developing a pipeline to create an ETL from CSV to PostgreSQL with Python.

The purpose of this challenge is to develop a Python script that reads a CSV file and loads the data into a postgreSQL database. Docker Compose is used to orchestrate the SQL database containers and its ETL Python application.

To solve the challenge I decided to create a function in the file main.py that is in charge of:
1. Define the variables for database connection settings.
2. Define the variables of CSV file name, schema name and table name in the database.
3. Create the connection to the database using SQLAlchemy and the database connection settings that I before define.
4. Create DDL of the table that will receive the data from the csv.
5. Read CSV file with pandas and keep it in a variable (data).
6. Finally, Load data into the postgresql table.

## Technologies
- **Language:** Python
- **Data Base:** PostgreSQL
- **Deployment tools:** Docker and Docker Compose

## Repo clonning
* git clone git@github.com:hgivanrene/csv_to_postgres_pipeline.git # This command is when you have your ssh key configured in the repo. This option is quite more safe.
* git clone https://github.com/hgivanrene/csv_to_postgres_pipeline.git # This option is to clone the repo using the web URL.

## Docker and Docker-compose installation on mac with colima

1. Homebrew installation.
Homebrew is the package manager for macOS and it will help us to install all kinds of things in the future.
To install homebrew we must open the terminal application that comes by default on the mac and perform the following command:

* /bin/bash -c “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)”

At the end of running the command it will ask you to run the following two commands which are to add the homebrew to your PATH:

* (echo; echo 'eval “$(/opt/homebrew/bin/brew shellenv)”') >> /Users/<user_name>/.zprofile.
    * Note: The <user_name> must be changed to the username assigned on your machine.

* eval “$(/opt/homebrew/bin/brew shellenv)”

2. Once the homebrew is installed we move on to install colima.

* brew install colima

3. Then we install the Docker client.

* brew install docker
* brew install docker-compose

4. Starting colima for the first time
Once we have completed the previous steps we proceed to start colima. The first time we will do it assigning CPU and
MEMORY with the following command.

* colima start --cpu 4 --memory 6

To start colima on future occasions we would simply pass the command as follows:
* colima start

To stop colima we do it in the following way:
* colima stop


## Usage with Docker-compose

Create the image for the DB and Python script on your local machine.
* docker-compose up --build -d
* We use the flag -d to execute the data base image in the Background.

Once your image is completely up yo can check the logs of the python container to review the correctly execution of the main.py file.
* Use this command to know your container_id or container_name
* docker ps -a

* Use this command to check the logs of your container
* docker logs <container_name>

After this you will see the message of successful extraction and loading of data from your csv.

If you already want to turn off your DB container you can do the next command.
* docker-compose down