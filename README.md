# The-Neighborhood

### By Monicah Maina & Jeff Owuor

<p> 20th June 2022 </p>

## Table of Content

+ [Description](#description)
+ [Setup/Installation Requirements](setup&installationrequirements)
+ [How To Access the Site](#howtoaccessthesite)
+ [TDD](#tdd)
+ [UserStory](#userstory)
+ [Technology & Tools](#technology&tools)
+ [Reference](#reference)
+ [Authors Info](#authors-info)

## Description

> This is a web application that allows users to be in the loop about everything happening in the neighborhood. From contact information of different handyman to meeting announcements or even alerts.

## Setup/Installation Requirements

### You need to have the following installed

#### Prerequisites

You must have git, django, postgres and python3.8+ installed in your pc.
To install django and Postgres, you can use the following commands:

```
#django
$ pip install django
#postgres
$ sudo apt-get install postgresql postgresql-contrib libpq-dev
```

```
 
 git clone https://github.com/Jeff-Owuor/The-Neighborhood.git
 virtualenv virtual
 source virtual/bin/activate
 pip freeze > requirements.txt
 psql CREATE DATABASE neighbor
 python3.8 manage.py runserver
 python manage.py migrate

```

## TDD

> To test the app, run this command in the terminal;
`$ python manage.py test`

## User Story

> As a user I would like to:

1. Sign in with the application to start using.
2. Set up a profile about me and a general location and my neighborhood name.
3. Find a list of different businesses in my neighborhood.
4. Find Contact Information for the health department and Police authorities near my neighborhood.
5. Create Posts that will be visible to everyone in my neighborhood.
6. Change My neighborhood when I decide to move out.
7. Only view details of a single neighborhood.

### Technology & Tools

* Python
* Django 
* HTML
* CSS
* Bootstrap
* Postgres (Database)
* Git

## Reference

* [Django documentation](https://docs.djangoproject.com/en/4.0/)
* [ Django REST Framework Tutorial](https://learndjango.com/tutorials/official-django-rest-framework-tutorial-beginners)

## Authors information

> Feel free to add your contribution to the code.
> If you have any questions,comments or advice,feel free to contact us

### Emails

* monicahjustus@gmail.com
* jeffowuor@gmail.com
