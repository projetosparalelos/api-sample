from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None and response.status_code == 400:
        for field, error_messages in response.data.items():
            response.data[field] = ' '.join(error_messages)
    return response
