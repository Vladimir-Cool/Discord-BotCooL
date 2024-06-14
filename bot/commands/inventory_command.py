from discord import Interaction

from .base import command_custom
from api.inventory_api import InventoryAPIClient

@command_custom
async def invent_info(interaction: Interaction):
    discord_id = interaction.user.id

    async with InventoryAPIClient() as api_inventory:
        inventory = await api_inventory.get_inventory_for_user(discord_id)

    return {
        "data_obj": inventory
    }
