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

- [ ] make all date fields editable in admin exclude create_date
- [ ] make tables sortable by every field ()
- [X] remove all default='SOME STRING' from models
- [ ] change tables to boostrap table for sorting
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
