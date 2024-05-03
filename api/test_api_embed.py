from httpx import Response
from typing import Dict

from .base_api import APIClient


class EmbedAPIClient(APIClient):
    url = "new_url"

    async def get_embed(self, name_embed: str, data: Dict):
        response: Response = await self.get(url=self.url)
        return response.json()
