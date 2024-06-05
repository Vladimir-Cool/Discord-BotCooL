from typing import Dict, Optional
from httpx import Response

from .base_api import APIClient


class EmbedAPIClient(APIClient):
    """
    API клиент для работы с Embed
    """

    url = f"http://127.0.0.1:8000/api/v1/"

    async def render_embed(self, data):
        response: Response = await self.post(url=f"{self.url}renderembed/", json=data)
        return response.json()
