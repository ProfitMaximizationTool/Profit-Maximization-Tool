# Profit Maximization Tool

This is a course requirements for CS191/192 Software Engineering Courses of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman under the guidance of Ma. Rowena C. Solamo for AY 2020-2021.

## Members

- Cayetano, Anthony Van
- De Castro, Hans Gabriel
- Diokno, Alyssa Beatrice
- Loristo, John Ivan

## Sprint 1

**start date:** February 21, 2022

**end date:** March 4, 2022

### Use cases accomplished:

- UC-1.0-S1: Business owner successfully signs up for an account
  
- UC-1.0-S2: Business owner successfully logs into account
  
- UC-1.0-S3: Invalid Username
  
- UC-1.0-S4: Invalid password
  
- UC-1.0-S5: Username not available
  

## Features so far

1. Users can sign up for an account and fill in asked information
  
2. Users can login using registered account
  
3. Upon successful sign up or login, users are redirected towards home page with logged in status
  
4. Users are prompted with an error if the password they used for logging in is incorrect
  
5. Users are prompted with an error if the username they input during sign up is already taken
  

# How to run this build

Note that this project was all created and tested on Windows 10 machines for now

## Pre-requisites

Install virtual env on your computer using the command below:

```bash
pip install virtualenv
```

## Setting up a virtual environment

Run the command below to create a virtual environment with python 3.10 installed

```bash
py -3.10 -m venv sample-venv
```

A folder will be created with the name *sample-venv*. Go inside sample-venv using the command below:

```bash
cd sample-venv
```

Now that you are inside *sample-venv*, to activate the virtual environment, run the command below:

```bash
Scripts\activate.bat
```

You will see that there is a *(sample-venv)* on the left side of your command prompt. It looks like this:

```bash
(sample-venv) C:\...\sample-venv
```

Now that you are inside the virutal environment, you must first install the dependencies of the project.

You can download the text file named *requirements.txt* from the assets dropdown on the project's releases and place it inside the *sample-venv* folder or you can create a text file named *requirements.txt* inside the *sample-venv* folder. Open the said text file using any text editor app and paste the lines below and save the file.

```
asgiref==3.5.0
Django==4.0.2
numpy==1.22.2
scipy==1.8.0
sqlparse==0.4.2
tzdata==2021.5
```

Then, install these dependencies using the command below (assuming you are inside the *sample-venv* folder and the virtual environment is activated)

```bash
pip install -r requirements.txt
```

If you want to deactivate the virtual environment, just run the command below:

```bash
Scripts\deactivate.bat
```

## Building the project

Note that you can obtain the project's files either by cloning the repo or by downloading the zip file named *Profit-Maximization-Tool-main-v1.zip* from the assets dropdown from Git release.

### Downloading the zip file from Git releases

Download the zip file named *Profit-Maximization-Tool-main-v1.zip* from the releases section of the project's repo. After downloading, extract the contents of the file inside the *sample-venv* folder. You should now be seeing a folder named *profitify*. If it is not named *profitify*, and it is named *Profit-Maximization-Tool-main*, just rename it to *profitify* for ease of navigation using the *cd* command.

### Cloning the project from the repository

Note that you must clone the repository inside the *sample-venv* folder.

```bash
cd sample-venv
```

Make sure that you are inside the *sample-venv* folder before proceeding to clone the repository.

The link to the project's repository is this: [ProfitMaximizationTool/Profit-Maximization-Tool (github.com)](https://github.com/ProfitMaximizationTool/Profit-Maximization-Tool)

In order to clone this git repo to your machine, run the command below:

```git
git clone https://github.com/ProfitMaximizationTool/Profit-Maximization-Tool.git profitify
```

A folder with the name profitify will be created. Inside it are the contents of the repository.

Activate the virtual environment first using the command below (Assuming you are inside *sample-venv* folder).

```bash
Scripts\activate.bat
```

## Running the web application

At this step, it i is assumed that you have already activated the virtual environment and you are inside the *sample-venv* folder. You must see this below in your command prompt:

```bash
(sample-venv) C:\...\sample-venv
```

Next, we need to start the development server using the commands below:

```bash
python profitify\ProfitMaximizationTool\manage.py migrate
```

```bash
python profitify\ProfitMaximizationTool\manage.py runserver
```

You will see in your a line saying

```bash
Starting development server at http://127.0.0.1:8000/
```

Paste the url into your browser and then you should be seeing the home page of the application now
