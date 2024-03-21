# ORA - Open REST API
![GitHub License](https://img.shields.io/github/license/Daniel3dartist/ORA)
The objective of ORA is to create data procedurally that can be used to create temporary databases or used directly in testing front-end and mobile applications, the ease comes from using Docker for this, the front-end and mobile developer will have a tool simulating the back-end without having to master a lot of knowledge to do so.

# About development
At the moment ORA is still in the prototyping and development phase, we are testing concepts and usability, but feel free to contribute and suggest improvements.

### Requirements:
- python3.10+

# How to use

### Install Docker
This application is being developed aimed at being used in a Docker container (you can install and use it directly on your machine if you want, we will leave a step-by-step guide below on how to do this), if you don't have installed on your machine, do you can [download docker here](https://docs.docker.com/get-docker/).

### Build docker image
This command will use the project's DockerFile to create a docker image of the project.
```
docker build -t ora:latest .
```
If you don't know about Docker images, you can learn more by clicking [here](https://docs.docker.com/engine/reference/commandline/images/#description).

### Run Docker container
With our project image created, we can create and run our container. Use the command below to do this.
```
docker run -d -p8080:8080 --name ora ora:latest
```
If you are not familiar with Docker containers, you can learn more by clicking [here](https://www.docker.com/resources/what-container/).

### Check if it's working
You can use the command "docker stats" in the terminal or directly open [localhost](http://localhost:8080/) on port 8080
```
docker stats
```
If everything went well, our application is up and running! ^^

### Accessing the Docker container prompt
It is a common case of having to access the application container prompt to configure some things or run tests, to do this simply execute the command below:
```
docker exec -it ora /bin/sh
```

# You can also use it directly on your machine. 
First you need to install python (we recommend use python3.10+). Do you can download and install by clicking [here](https://www.python.org/downloads/)

### Create a virtual environment
In the clone folder, create a python virtual environment with the following command:

**Linux**
```
python3 -m venv venv
```
**Windows**
```
pyton -m venv venv
```
### Activating the virtual environment
To activate our venv just write this command in the terminal:
```
cd venv/Scripts/
```
```
activate
```

Once you are in the virtual environment, run the following command to update pip:

**Linux**
```
python3 -m pip install --upgrade pip
```
**Windows**
```
python -m pip install --upgrade pip
```

### Installing project dependencies
After that, go back to the directory where the "manage.py" file is located and run the following commands:
```
pip install requirements.txt
```
### Running the application
If all the steps were followed correctly, we can now start our application.

- First let's do our migrate:
```
python manage.py mikemigrations
```
```
python manage.py migrate
```
- After migrations we can run the runserver command on port 8000:
```
python manage.py runserver 8000
```

# Note:
This project is still under development, instructions may be missing that will be added in the future.


