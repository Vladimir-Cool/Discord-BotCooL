from httpx import Response, AsyncClient, codes, Timeout


class APIException(Exception):
    def __init__(self, response: Response):
        self.status = response.status_code
        try:
            self.data = response.json()
        except:
            self.data = response.text
        super().__init__(self.data)


class CriticalException(Exception):
    def __init__(self, response: Response):
        self.status = 500
        super().__init__(response.request.method, response.request.url)


class APIClient(AsyncClient):
    url = "http://127.0.0.1:8000/api/v1/"

    def __init__(self, **kwargs):
        """Переопределяем конструктор для глобальной настроки клиентов"""
        if "timeout" not in kwargs:
            kwargs["timeout"] = Timeout(None, connect=5.0)
        if "follow_redirects" not in kwargs:
            kwargs["follow_redirects"] = True
        super().__init__(**kwargs)

    async def request(self, *args, **kwargs):
        """Переопределяет работу запросов, добавляя обработку ошибок"""
        response: Response = await super().request(*args, **kwargs)
        if codes.is_server_error(response.status_code):
            raise CriticalException(response)
        elif codes.is_client_error(response.status_code):
            raise APIException(response)
        return response
