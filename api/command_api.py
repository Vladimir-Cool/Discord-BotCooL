from httpx import Response

from .base_api import APIClient


class CommandsAPIClient(APIClient):

    async def get_commands(self):
        resource: Response = await self.get(url=f"{self.url}command/")
        return resource.json()
