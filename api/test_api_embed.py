from httpx import Response
from typing import Dict, Optional

from .base_api import APIClient


class EmbedAPIClient(APIClient):
    async def get_embed(self, name_embed: str, data: Optional[Dict] = None):
        response: Response = await self.get(
            url=f"{self.url}embed/{name_embed}/", params=data
        )

        return response.json()[0]
