from rest_framework.response import Response


class CustomResponse(Response):
    def __init__(self, data=None, message=None, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        response_data = {
            'code': status,
            'data': data,
            'message': message or self._get_default_message(status)
        }

        super().__init__(
            data=response_data,
            status=status,
            template_name=template_name,
            headers=headers,
            exception=exception,
            content_type=content_type
        )

    @staticmethod
    def _get_default_message(status_code):
        messages = {
            200: 'Success',
            201: 'Created',
            204: 'Deleted',
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            404: 'Not Found',
            500: 'Internal Server Error',
        }
        return messages.get(status_code, '')