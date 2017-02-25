# Django Rest Framework Task
Clone the repo and run pip install -r requirements.txt

First install virtualenv for this project

Run in terminal python manage.py migrate
and python manage.py runserver.

# Apis
Open postman and enter the following urls for API responses.
localhost:8000/api/v1/contact/
With this url you can see all the contacts in database and can also post a contact.
Parameter is 'name'.

localhost:8000/api/v1/contact/<id>
This url is for updating and deleting a contact
