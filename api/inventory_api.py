from httpx import Response

from .base_api import APIClient


class InventoryAPIClient(APIClient):
    """
    API клиент для работы с Embed
    """


    async def get_inventory_for_user(self, discord_id: int):
        response: Response = await self.get(url=f"{self.url}inventory/{discord_id}")
        return response.json()[0]

