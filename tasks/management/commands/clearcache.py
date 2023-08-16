from django.core.management.base import BaseCommand
from subprocess import call
import os.path
from django.conf import settings
class Command(BaseCommand):
    # python3 manage.py help welcome
    help = 'Clears App cache by deleting all .pyc files'  
    
    def handle(self, *args, **kwargs):
        SITE_ROOT = os.path.dirname(os.path.realpath(__name__))
        self.stdout.write("Deleting all .pyc files inside  "+SITE_ROOT)
        cmd = 'find '+SITE_ROOT+' -name "*.pyc" -exec rm -f {} \;'
        success = call(cmd, shell=True)
        if(success==0):
            self.stdout.write("Success ")
        else: 
            self.stdout.write("Cannot clear ")
            