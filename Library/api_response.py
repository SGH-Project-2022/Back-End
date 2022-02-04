from rest_framework.response import Response


class ApiResponse:
    def __init__(self):
        self.__reponse = {}

    def set_status_code(self, code: int) -> 'ApiResponse':
        self.__reponse['status_code'] = code
        return self

    def set_data(self, key: str, value) -> 'ApiResponse':
        self.__reponse[key] = value
        return self

    def set_token(self, token: str) -> 'ApiResponse':
        self.__reponse["token"] = token
        return self

    def response(self) -> Response:
        return Response(self.__reponse)

    def get(self) -> dict:
        return self.__reponse
