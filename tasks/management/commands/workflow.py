from django.core.management.base import BaseCommand
from tasks.celery_tasks import mergeRepoData
from celery.result import AsyncResult
class Command(BaseCommand):
    help = 'Merge User Data'  
    def handle(self, *args, **kwargs):
       mergeRepoData.delay()
