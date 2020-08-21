#get started with Django3.0.3

# clone class codes:
```
git clone https://github.com/LinkedInLearning/learning-django-2825501.git
```
- no a programming language
# how to download
```
pip install django==3.0.3
```

# creat an django project:
- navigate in your terminal to the folder with cd and type
``` django-admin startproject wisdompets```

There will be a django project called *wisdompets* created in here and below this folder, there should be 5 files .

![screenshot](.\Annotation 2020-08-21 165634.png)

**manage.py**:
- Run command

**wisdompets/_ init _.py**
- Tell Python that the folder contains python code

**wsgi.py** & **asgi.py**
- provide hooks for web server such as __Apache__ or __Nginx__ when django running in a live website.

Finally, **setting.py** & **urls.py** routes requests
- based on the urls

# Part II generate build a
Firstly, cd into the "wisdompets" folder and then type:
```python manage.py startapp adoptions```

Secondly, Add 'adoptions' into INSTALLED_APPS in line 33 in the setting.py

---
Django use MVC architectue which is also called __Model-View-Controller__
