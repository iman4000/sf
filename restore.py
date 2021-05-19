
import os
import sys
import django

try:    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firewall.settings')
    try:
        from django.core.management import call_command 
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    django.setup()
except RuntimeError:
    print("Django can not be loaded") 

# get args
args = sys.argv
# check for one filename in args
if len(args) != 2:
    raise ValueError("program needs one file to restore\n\nusage: restore.py FILENAME")
# get file name
file = sys.argv[1]
# check for file existence
if os.path.isfile(file) is False:
    raise IOError("file not exist")
call_command('loaddata', '--format=json', file)
    
