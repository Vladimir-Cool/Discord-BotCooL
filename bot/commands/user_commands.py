from discord import Interaction, Member, Embed
from discord.app_commands import command


from api.user_api import UserAPIClient
from api.base_api import APIException
from api.embed_api import EmbedAPIClient
from bot.embeds.user_embed import UserEmbed
from bot.views.user_view import UserView
from .base import command_custom


# @command(name="регистрация", description="Регистрация нового пользователя в системе")
# async def registration(interaction: Interaction, name: str):
#     """Регистирует нового пользователя (UserModel) в системе по discord_id и name.
#     Если пользователь уже зарегистрирован то будет обработана ошибка
#     Если name кже занято то так же будет ошибка"""
#     try:
#         async with UserAPIClient() as api_client:
#             response = await api_client.post_reg(
#                 name=name, discord_id=interaction.user.id
#             )
#             await interaction.response.send_message(
#                 f"Регистрация успешна\ndata = {response}"
#             )
#
#     except APIException as e:
#         if "discord_id" in e.data.keys():
#             await interaction.response.send_message(
#                 f'Вы уже зарегистрировались просмотреть свой профиль можно командой "/профиль"'
#             )
#         elif "name" in e.data.keys():
#             await interaction.response.send_message(f'Имя "{name}" Уже используется')


@command_custom
async def user_reg(interaction: Interaction, name: str):
    """
    Регистирует нового пользователя (UserModel) в системе по discord_id и name.
    Если пользователь уже зарегистрирован то будет обработана ошибка
    Если name кже занято то так же будет ошибка
    """
    try:
        async with UserAPIClient() as api_client:
            response = await api_client.post_reg(
                name=name, discord_id=interaction.user.id
            )

        return {"content": f"Регистрация успешна\ndata = {response}"}

    except APIException as e:
        if "discord_id" in e.data.keys():
            return {
                "error": 'Вы уже зарегистрировались просмотреть свой профиль можно командой "/user_info"'
            }
        elif "name" in e.data.keys():
            return {"error": f'Имя "{name}" Уже используется'}


@command_custom
async def user_info(interaction: Interaction, member: Member = None):
    """Команда которая возврашает профиль пользователя и список персонажей"""
    # Ууууу тернарное выражение...
    discord_id = member.id if member else interaction.user.id

    # try:
    async with UserAPIClient() as api_client:
        user: list = await api_client.get_user(discord_id=discord_id)

    if not user:
        raise Exception("Такой пользователь не найден")

    if user["characters"]:
        view = UserView(user["characters"])
    else:
        view = UserView()

    return {
        "data_obj": user,
        "view": view,
    }

    # except APIException as e:
    #     return {"error": e}


@command_custom
async def user_del(interaction: Interaction):
    async with UserAPIClient() as api_client:
        resource = await api_client.del_user(interaction.user.id)

    return {"content": resource}

