from django.core.management.base import BaseCommand
from tasks.celery_tasks import square,add
from celery import chain 
from celery.result import AsyncResult

class Command(BaseCommand):
    help = 'Chain Example'  
    def handle(self, *args, **kwargs):
        a = 3
        b = 4
        # step -1 : square(b) gives 16
        # step -2 : 16 is used as second argument of add
        # this 3 + 16 gives 19 (Note '|' operator)
        res =  chain(square.s(b)|add.s(a)).apply_async() 
        task_id = res.id
        #wait for async result
        response = AsyncResult(task_id)
        #get response
        print(response.get())

