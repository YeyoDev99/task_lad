# Task Lad
Welcome to this humble repository, i'll explain the fundamental component of the project and how to manage them, the app consist in a task management app with user management, the backend uses django and the frontend uses the django template language and the css framework Bootstrap.
## Set Up
---
first we must install the project dependencies that are already stored in requirements.txt, so we just type:
``` 
pip install -r requirements.txt

```
the dependencies are just two:
- **django** for the backend
- **pillow** for the image management

now to set the **database**  we enter the django project folder where the manage.py file is located and type in our console:
``` 
py manage.py makemigrations

```
and then:
``` 
py manage.py migrate

```
and now the app is ready to run. 
## Local Server
---
to see the project we enter the django project folder where the manage.py file is located and we type in our terminal:
```
py manage.py runserver
```
and then we type the local server in our navbar.
## Time Zone Issue
---
django backend uses the timezone module to set date-times, so the performance depends on the timezone configuration, so to try the app properly go to settings.py and set:
```
TIME_ZONE = 'your_timezone'
```
you can find your timezone [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).