from discord import Interaction, Member, Embed
from discord.app_commands import command


from api.user_api import UserAPIClient
from api.base_api import APIException
from bot.embeds.user_embed import UserEmbed
from bot.views.user_view import UserView
from .base import command_custom


@command(name="регистрация", description="Регистрация нового пользователя в системе")
async def registration(interaction: Interaction, name: str):
    """Регистирует нового пользователя (UserModel) в системе по discord_id и name.
    Если пользователь уже зарегистрирован то будет обработана ошибка
    Если name кже занято то так же будет ошибка"""
    try:
        async with UserAPIClient() as api_client:
            response = await api_client.post_reg(
                name=name, discord_id=interaction.user.id
            )
            await interaction.response.send_message(
                f"Регистрация успешна\ndata = {response}"
            )

    except APIException as e:
        if "discord_id" in e.data.keys():
            await interaction.response.send_message(
                f'Вы уже зарегистрировались просмотреть свой профиль можно командой "/профиль"'
            )
        elif "name" in e.data.keys():
            await interaction.response.send_message(f'Имя "{name}" Уже используется')


# @command(name="профиль", description="Просмотр профиля")
# async def user_info(interaction: Interaction, member: Member = None):
#     """Команда которая возврашает профиль пользователя или список персонажей"""
#     # Ууууу тернарное выражение...
#     discord_id = member.id if member else interaction.user.id
#
#     try:
#         async with UserAPIClient() as api_client:
#             users: list = await api_client.get_user(discord_id=discord_id)
#             user = users[0]
#
#         if user["characters"]:
#             view = UserView(user["characters"])
#         else:
#             view = UserView()
#
#         embed = UserEmbed(user)
#
#         await interaction.response.send_message(embed=embed, view=view)
#
#     except APIException as e:
#         await interaction.response.send_message(e.data)


@command_custom
async def user_info(interaction: Interaction, member: Member = None):
    """Команда которая возврашает профиль пользователя или список персонажей"""
    # Ууууу тернарное выражение...
    discord_id = member.id if member else interaction.user.id
    embed = interaction.command.extras.get("embed")
    print(embed)
    try:
        async with UserAPIClient() as api_client:
            users: list = await api_client.get_user(
                discord_id=discord_id, data={"embed": embed}
            )
            if users:
                user = users[0]
            else:
                return {"error": "Такой пользователь не найден"}

        if user["characters"]:
            view = UserView(user["characters"])
        else:
            view = UserView()

        embed = UserEmbed(user)

        return {
            "embed": embed,
            "view": view,
        }

    except APIException as e:
        return {"content": e}


@command(name="удали", description="Удалит твой аккаунт насовсем, сильно на совсем")
async def user_del(interaction: Interaction):
    async with UserAPIClient() as api_client:
        resource = await api_client.del_user(interaction.user.id)

    await interaction.response.send_message(f"Результат {resource}")
