from django.core.management.base import BaseCommand
from tasks.celery_tasks import sayHello

class Command(BaseCommand):
    # python3 manage.py help say_hello <name>
    help = 'Say hello'  
    def add_arguments(self, parser):
        parser.add_argument('name',  help='Your name')
    def handle(self, *args, **kwargs):
        name = kwargs['name']
        sayHello.delay(name)
    