import time
from django.core.management.base import BaseCommand
from demo_app.models import Task
from celery import shared_task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def Command(request):
    if request.method == 'POST':
        def handle(self, *args, **options):
            while True:
                # Get the next unprocessed task
                task = Task.objects.filter(processed=False, status=0).order_by('id').first()
                if task:
                    print("Processing task:", task.data)
                    # Mark the task as processed
                    self.push_task_to_celery.delay(task)
                    time.sleep(1)

                    # Marking the task true after processing since the time limit is breached
                    if not task.processed:
                        task.status = 1
                        task.save()

                    print('Pushed task to celery queue')
                else:
                    # If no tasks are found, wait for a while before checking again
                    pass
        return JsonResponse({'message': 'System Invoked'})

    @shared_task(time_limit=1)
    def push_task_to_celery(self, task):
        # Task execution will take place here
        task.processed = True
        task.save()
