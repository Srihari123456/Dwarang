# Dwarang
A Web Based Python-Django Framework For Official Purposes

## Check out dwarang.herokuapp.com

## Installation:
Install pip and then install system-wide virtualenv PIP package.

### Linux:
    sudo apt-get install python-pip
    sudo pip install virtualenv

### Windows: 
    Install python3.8 
    pip install virtualenv

Create a virtual environment for our project in a folder named **env_dwarang**, and "activate" it,
so that all our subsequent PIP packages are installed in this virtual environment only, and not globally. 

```
cd Dwarang
virtualenv env_dwarang
```

### Linux:
    source env_dwarang/bin/activate   
    
### Windows:
    env_dwarang\scripts\activate

Install the dependencies using:

pip install -r requirements.txt
#### Note: Above command installs Django also.

## Running the Django app:

Create SQLite database, which is just a file db.sqlite3 being used as database for this app using:
```
python manage.py migrate
```

And then run the Django app by:
```
python manage.py runserver
```

Now you can go to your browser and type http://127.0.0.1:8000/ and you can see the Django app in action!
