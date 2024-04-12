import time
from django.core.management.base import BaseCommand
from demo_app.models import Task
from celery import shared_task


class Command(BaseCommand):
    help = 'Process queued tasks'

    def handle(self, *args, **options):
        while True:
            # Get the next unprocessed task
            task = Task.objects.filter(processed=False).order_by('id').first()
            if task:
                # Process the task (In this example, we'll just print the data)
                print("Processing task:", task.data)
                # Mark the task as processed
                # task.processed = True
                # task.save()
                self.push_task_to_celery.delay(task)
                print('Pushed task to celery queue')
            else:
                # If no tasks are found, wait for a while before checking again
                time.sleep(1)

    @shared_task
    def push_task_to_celery(self, task):
        task.processed = True
        #Task execution will take place here
        task.save()
