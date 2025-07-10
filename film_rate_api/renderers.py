from rest_framework.renderers import JSONRenderer


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context['response']
        status_code = response.status_code

        formatted_data = {
            'code': status_code,
            'data': data,
            'message': getattr(response, 'message', None) or self._get_default_message(status_code)
        }

        return super().render(formatted_data, accepted_media_type, renderer_context)

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