from django.core.management.base import BaseCommand
from tasks.celery_tasks import square,add
from celery import group 
from celery.result import AsyncResult

class Command(BaseCommand):
    help = 'Group Example'  
    def handle(self, *args, **kwargs):       
        g =  group(square.s(1),square.s(2),square.s(3),square.s(4))
        res = g()
        print(res.get())

