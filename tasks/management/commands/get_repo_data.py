from django.core.management.base import BaseCommand
from tasks.celery_tasks import getDataFromRepository
from celery.result import AsyncResult


class Command(BaseCommand):
    help = 'Get User data from Github using API'  
    def add_arguments(self, parser):
        parser.add_argument('username',  help='Github username is required')
    def handle(self, *args, **kwargs):
        username = kwargs['username']
        result=getDataFromRepository.delay(username)
        print(result.task_id)
        res = AsyncResult(result.task_id)
        print(res.get())
