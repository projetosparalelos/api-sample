from functools import wraps

import bugsnag
from celery.decorators import task as celery_task
from django.conf import settings


def exception_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if settings.DEBUG:
                raise e
            else:
                bugsnag.notify(e, meta_data=dict(args=args, **kwargs))
    return wrapper


def task(func):
    @celery_task
    @exception_handler
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
