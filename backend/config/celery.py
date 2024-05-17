# import os
# from celery import Celery
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
#
# celery_app = Celery("config")
# # celery_app.config_from_object("django.conf:settings", namespace="CELERY")
#
# # Load all tasks
# celery_app.autodiscover_tasks()
#
# celery_app.conf.broker_url = "redis://localhost:6379/0"
# celery_app.conf.result_backend = "redis://localhost:6379/2"
# celery_app.conf.broker_backend = 'redis://localhost:6379/1'
# celery_app.conf.task_serializer = 'json'
# celery_app.conf.result_serializer = 'json'
# celery_app.conf.accept_content = ['json', ]
# # celery_app.conf.result_expires = timedelta(days=1)
# celery_app.conf.task_always_eager = False
# celery_app.conf.broker_connection_retry_on_startup = True
# celery_app.conf.worker_prefetch_multiplier = 4
