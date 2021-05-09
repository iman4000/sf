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

1. [X] date picker persian admin
2. [X] admin time picker by time
3. [ ] company change to class
4. [ ] description not required
5. [ ] show tables like Recived From Company, Delivery To Category, Recive From Company, Delivery To Category
6. [ ] delete delivery person name from Recived From Company
7. [ ] add Company person to Recive/Deliver From/To Company
9. [ ] delete deliver to company date from deliver to company
10. [ ] datetime match to +3:30 in view 
11. [ ] check for app logic and fix it
12. [ ] setting update