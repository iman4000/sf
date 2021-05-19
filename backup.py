
import os
from datetime import datetime
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


file_name = "database_backup_" + str(datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))
call_command('dumpdata', '--format=json', '--output=backups/' + file_name + '.json')
