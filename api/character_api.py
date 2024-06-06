from httpx import Response

from .base_api import APIClient


class CharacterAPIClient(APIClient):
    """
    API клиент для работы с персонажем
    Django - UserModel
    """

    url = f"http://127.0.0.1:8000/api/v1/"

    async def get_chars(self, discord_id: int):
        """Вернет всех персонажей"""
        response: Response = await self.get(url=f"{self.url}characters/")
        return response.json()

    async def get_char(self, discord_id: int, name: str):
        """Вернет персонажа по id user и name"""
        response: Response = await self.get(
            url=f"{self.url}characters/{discord_id}/{name}/"
        )
        return response.json()[0]

    async def get_char_for_user(self, discord_id: int):
        """Вернет список персонажей по id user"""
        response: Response = await self.get(
            url=f"{self.url}usercharacters/{discord_id}/"
        )
        return response.json()

    async def post_char(self, discord_id: int, name: str):
        """Создание нового персонажа"""
        data = {
            "user": discord_id,
            "name": name,
        }
        response: Response = await self.post(url=f"{self.url}characters/", json=data)
        return response.json()

    async def delete_char(self, char_name: str):
        """Удаление персонажа"""
        response: Response = await self.delete(url=f"{self.url}characters/{char_name}/")
        return response
