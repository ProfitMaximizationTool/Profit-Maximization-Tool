# Profit Maximization Tool

This is a course requirements for CS191/192 Software Engineering Courses of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman under the guidance of Ma. Rowena C. Solamo for AY 2021-2022.

## Members

- Cayetano, Anthony Van
- De Castro, Hans Gabriel
- Diokno, Alyssa Beatrice
- Loristo, John Ivan

## UAT Release
- Tested by **Group 4 (GoVLê)** on **June 8, 2022**
- New set of sample files

## Sprint 5

**start date:** May 2, 2022

**end date:** May 13, 2022

### Use cases accomplished in sprint 5

- UC7-S1: Business owner views the profit chart

### Changelog in sprint 5:

- Added search functionality for products, inventory, sales, and production table

- Changed font styles of new links

- New background for landing page

- Improved edit profile page

- Added ability to set profile picture

- Added chart in dashboard and profit tracker tab

- Inventory total and daily units is updated based on current day's production record

- New background

- Redesigned success and error prompts

- More UI changes

## Sprint 4

**start date:** April 18, 2022
**end date:** April 29, 2022

### Use cases accomplished in sprint 4

- UC6-S1: Business owner uses the profit optimizer tool

### Changelog in sprint 4:

- Optimize profit button works now
- Quantity of products that must be produced (and sold) to obtain Optimal profit for the day is computed and displayed
- The suggested result of Profit Optimizer can be added to Production table if the user wants to
- Suggested quantity of products to be produced takes into account the top selling products according to Sales Table

## Sprint 3

**start date:** March 21, 2022

**end date:** April 1, 2022

### Use cases accomplished in sprint 3

- UC3-S3: Business owner inputs existing sales database

- UC3-S4: Business owner inputs existing production database

- UC3-S7: Business owner tries to input existing sales database but uses the wrong file

- UC3-S8: Business owner tries to input existing production database but uses the wrong file

### Changelog in sprint 3:

- Added ability to upload csv file for Sales database

- Added ability to upload csv file for Production database

- Added prompt for invalid Sales database file upload

- Added prompt for invalid Production database file upload

- Added ability to manually add, edit, and delete Sales record

- Added ability to manually add, edit, and delete Production record

- Sales record revenue is automatically computed based on Production table

- Production record Expenses is automatically computed based on Products and Inventory tables

- Improved the interface for adding/editing new or existing ingredients and their costs for Product records by adding dropdown box for ingredient names

- UI Improvements
  
  - submit buttons
  
  - tables
  
  - overlays
  
  - scrolling

- Code refactoring (less messy code)

- Revamped the format for Products database csv file

## Sprint 2

**start date:** March 7, 2022

**end date:** March 18, 2022

### Use cases accomplished in sprint 2

- UC3-S1: Business owner inputs existing products database

- UC3-S2: Business owner inputs existing inventory database

- UC3-S5: Business owner tries to input existing products database but uses the wrong file

- UC3-S6: Business owner tries to input existing inventory database but uses the wrong file

### Changelog in sprint 2:

- New Dashboard with sidebar

- New Products Page

- New Inventory Page

- New Profile Page

- Ability to change Name and Business Name

- Ability to upload csv file for Products database

- Added prompt for successful uploading of file

- Added prompt for invalid type of file uploaded

- Ability to upload csv file for Ingredients database

- Contents of Products database are displayed in Products Page

- Contents of Ingredients database are displayed in Inventory page

- Added the ability to manually add, edit, or delete a Product record

- Added the ability to manually add, edit, or delete an Ingredient record

- A Product's cost to manufacture is automatically computed based on Ingredients database

## Sprint 1

**start date:** February 21, 2022

**end date:** March 4, 2022

### Use cases accomplished in sprint 1

- UC-1.0-S1: Business owner successfully signs up for an account

- UC-1.0-S2: Business owner successfully logs into account

- UC-1.0-S3: Invalid Username

- UC-1.0-S4: Invalid password

- UC-1.0-S5: Username not available

## Changelog in sprint 1:

- Users can sign up for an account and fill in asked information

- Users can login using registered account

- Upon successful sign up or login, users are redirected towards home page with logged in status

- Users are prompted with an error if the password they used for logging in is incorrect

- Users are prompted with an error if the username they input during sign up is already taken

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
Pillow==9.1.0
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

## Importing files order

1. inventory
2. products
3. production
4. sales

# Requirements

The dependencies included in requirements.txt are listed below plus other libraries that we used not installed through pip

- Python libraries
  
  - Django - https://www.djangoproject.com/
  
  - Numpy - https://numpy.org/ 
  
  - Scipy - https://scipy.org/

- Chart.js - https://www.chartjs.org/

- Ionicons - https://ionic.io/ionicons

# References

- no author. [Django documentation](https://docs.djangoproject.com/en/4.0/?fbclid=IwAR2dqnYI2Q_iRjttWoAFagmqd_ke_HnjRE7PHrCd-nApRYyxHAKQjhqGDks). Last accessed: March 15, 2022
