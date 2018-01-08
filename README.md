# CEG_Database

Created by Tyler Meyer - June, 2nd 2017

The purpose of this was to create a more efficient means to hold and transfer data for Consulting Engineers Group and its clients.

This was created with the help of an online tutorials

Django + MariaDB
https://medium.com/code-zen/django-mariadb-85cc9daeeef8

Setting up Django
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website

Building a Django App
https://www.youtube.com/playlist?list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj

**The following dependencies are needed:**
* Ubuntu 16.10+ or Server (Haven't tested on the new Ubuntu 17)
* pip3 for Python 3.x and Ubuntu Trusty Tahr and newer
* Python 3.5.2+
* Virtualenv
* Django 1.10
* MariaDB (MySQL) 10.0.29

**Ubuntu**
* sudo apt-get update

**Pip3**
* sudo apt-get install python3-pip

**Python3**
* sudo apt-get install python3.x (if not already installed)

**Django**
* pip3 install django==1.10
* django-admin startproject project

In first project folder
* django-admin startapp ceg
* Python3 manage.py createsuperuser

This is isn't necessary to copy now since we will be replacing all the files. 
Just be sure later that they match with your info and the info in the settings.py file
 
In the settings.py under project/project
```
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME’: 'myproject',
    'USER':'yourusername',
    'PASSWORD':'yourpassword',
    'HOST':'localhost',
    'PORT':'',
    }
}
```

Still in Settings.py under INSTALLED_APPS add
* 'ceg.apps.CegConfig',

**MySQL/MariaDB**
* sudo apt install -y mariadb-server
* A prompt may appear to create user BE SURE TO REMEMBER THIS

Login is always root. Set password if not prompted with code below
* mysql_secure_installation

* sudo apt-get install python3-mysqldb
* mysql -u root -p

'''

CREATE DATABASE project;

CREATE USER 'root'@'localhost' IDENTIFIED BY 'yourpassword';

GRANT ALL PRIVILEGES ON webapp.* TO 'root'@'localhost' IDENTIFIED BY 'yourpassword' WITH GRANT OPTION;

FLUSH PRIVILEGES;

EXIT;

'''

If you made changes to the inputed information, be sure to change it in the settings.py file

**Final Step**
* Copy the current SECRET_KEY from the settings.py file
* Save it in a document.
* Copy all the contents of that are in CEG_database and replace all that are in the first project folder
* Go back to the now replaced settings.py file and paste the saved SECRET_KEY into the current one.
* Be sure to check that the settings.py match the INSTALLED_APPS and DATABASES sections.

See if it works!
* python3 manage.py migrate
* python3 manage.py runserver 



