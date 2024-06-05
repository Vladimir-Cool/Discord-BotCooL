from typing import Dict, Optional
from httpx import Response

from .base_api import APIClient


class UserAPIClient(APIClient):
    """
    API клиент для работы с пользователем
    Django - UserModel
    """

    url = f"http://127.0.0.1:8000/api/v1/"

    async def get_user(self, discord_id: int):
        response: Response = await self.get(
            url=f"{self.url}userswithchars/{discord_id}/"
        )
        if response.json():
            return response.json()[0]
        return

    async def post_reg(self, name: str, discord_id: int):
        data = {
            "discord_id": discord_id,
            "name": name,
        }
        response: Response = await self.post(url=f"{self.url}users/", json=data)
        return response.json()

    async def del_user(self, discord_id):
        response: Response = await self.delete(url=f"{self.url}users/{discord_id}/")
        if response.status_code == 204:
            return "Удалено Успешно"
        else:
            return "Что то не то"
