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

## Backup/Restore

### Backup

1. enable virtual environment
2. execute backup.py in root directory `python backup.py`
3. backup will save is **/backups** folder

### Restore

1. enable virtual environment
2. execute restore.py followed by file name in root directory `python restore.py BACKUPFILE`
