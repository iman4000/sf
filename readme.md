# Firewall listing project
This project is for managing firewalls

## Installation 

1. make a virtual environment with python3 (e.g. python 3.6.9)
2. enable virtual environment 
3. execute `pip install -r requirements.txt`
4. copy firewall/settings.py.sample to settings.py and configure new setting file
5. make migrate with `python3 manage.py migrate`
6. create a super user by `python3 manage.py createsuperuser`
7. runserver `python3 manage.py runserver`

## TODO list

1. [X] export
2. [X] navare keshoii baraye category
3. [X] remove all default='SOME STRING' from models
4. [X] remove delivery row from recived 
5. [X] add sn to str firewall 
6. [X] add phone number to delivery person
7. [X] change date times auto to manual 
8. [X] same as 7
9. [X] search on 5 models
10. [X] sort on frontend js
11. [X] change "reciverd" to "recived from company" and "recived from category", "delivery" to "delivery from company" and "delivery from category"
12. [X] factory
