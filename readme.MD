# Customer Invitation Application

## About

This application reads user data from a text file and filters users based on comparing
their location and specific location constrains.It also outputs the result in a text file where the data is sorted by 
user_id in ascending order.

## Requires
* Python (version > 3)
* Virtual environment (Create and activate virtual environment by using conda or virtualenv or any other library)
* Follow the below steps if you have conda installed.
* To create the virtual environment:
```bash
   conda create -n myenv python=3.6
```
* To activate the virtual environment:
```bash
   conda activate myenv
```


## How to start

Once you have above requirements satisfied and virtual environment active, we can start the application. To do so execute following
steps :-

* Clone this repository and go to the root directory.

```bash
    git clone https://github.com/ranitdey/customer-invitation-application.git
    cd customer-invitation-application/
    
```

* Set project root directory as PYTHONPATH:
```bash
    export PYTHONPATH = <your system local path until the project root> /customer-invitation-application
    
```

    
* Install requirements from requirements.txt  

```bash
    pip install -r requirements.txt
```

* Run the application from project root folder. This will read the customer.txt file from /resource
 folder and generate the output in /output folder.In the output file it also attaches the 
 timestamp in the filename. 

```bash
    python src/app.py 
```

## How to test

* To run the unit test cases navigate to the project root folder and execute the following command: 

```bash
    pytest src/tests
```
