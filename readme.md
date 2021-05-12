# Firewall listing project

This project is for managing firewalls

## Installation

1. make a virtual environment with python3 (e.g. python 3.6.9)
2. enable virtual environment
3. execute `pip install -r requirements.txt`
4. copy firewall/settings.py.sample to settings.py and configure new setting file
5. make migrate with `python3 manage.py migrate`
6. create a super user by `python3 manage.py createsuperuser`
7. run server `python3 manage.py runserver`

## TODO list

1. [!] start.sh
2. [X] date picker persian admin
3. [X] admin time picker by time
4. [X] company change to class
5. [!] popup
6. [X] description not required
7. [X] delete delivery person name from Recived From Company
8. some changes to models:
   1. [X] delete category from delivery to company
   2. [X] add company to delivery to comany
   3. [X] delete delivery person name from delivery to company
   4. [X] add company person to delivery to company
9. [X] add Company person to Recived from Company
10. [X] show tables like Recived From Company, Delivery To Category, Recive From Company, Delivery To Category
11. [X] delete deliver to company date from deliver to company
12. [X] check for app logic and fix it
13. need to do:
    1. [X] delete replace from available 
    2. [X] datetime match to +3:30 in view
    3. [X] setting update
    4. [!] search by serial number
    5. [!] factory
    6. [X] view update, template update