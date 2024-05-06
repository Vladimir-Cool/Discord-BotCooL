from httpx import Response
from typing import Dict

from .base_api import APIClient


class EmbedAPIClient(APIClient):
    async def get_embed(self, name_embed: str, data: Dict = None):
        response: Response = await self.get(url=f"{self.url}embed/{name_embed}/")

        return response.json()[0]
