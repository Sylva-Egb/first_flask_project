## WELCOME TO MY FIRST FLASK PROJECT
### Goal of this project: My introduction to the Python framework Flask
#### Project Structure explanation

|static
    |css : The folder that contains all styling filed
|templates : contains all the views of the application
|app.py : the entry point of the application
|config.py : Contains all the config of the application
|forms.py : Contains all the formular classes used in the app
|models.py : Contains the model of our tables in database
|init_db.py : To initialize the database
|routes.py : contains the url of the app and the function that go with each ones

#### What you have to do to run the flask app

##### Step 1:
After cloning the project move in it and Install the dependencies
At Linux

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

At windows

```sh
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```

<b>If you want to desactivate the virtual environment tap ```desactivate```</b>

##### Step 2:
Initialize the database

```sh
python3 init_db.py #For Windows use python init_db.py
```

#### Step 3:
Run the application by typing

```sh
python3 app.py #For Windows use python app.py
```

Then you can open your browser and link to the localhost:5000