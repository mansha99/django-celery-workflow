from django.core.management.base import BaseCommand
from tasks.celery_tasks import calculateFactorial
from celery.result import AsyncResult

class Command(BaseCommand):
    help = 'Calculate Factorial of n '  
    def add_arguments(self, parser):
        parser.add_argument('n',  help='The number',type=int)
    def handle(self, *args, **kwargs):
        n = kwargs['n']
        res = calculateFactorial.delay(n)
        #get Task Id
        task_id = res.id
        #wait for async result
        response = AsyncResult(task_id)
        print(response.state) 
        #get response
        print(response.get()) 
        