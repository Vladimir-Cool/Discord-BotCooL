import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.message import Message
from discord.member import Member

from bot.conf_bot import settings

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())


@bot.event
async def on_redy():
    pass


@bot.event
async def on_member_join(member: Member):
    print(type(member))
    await member.send("Я бот, а ты? ")

    for ch in bot.get_guild(member.guild.id).channels:
        if ch.name == "основной":
            await bot.get_channel(ch.id).send(
                f"{member}, привет путник добро пожаловать на увлекательный канал, будь как дома"
            )


@bot.event
async def on_member_remove(member: Member):
    # await member.send("Нам будет тебя не хватать, прощай, но мы всегда будем ждать твоего возвращения...")

    for ch in bot.get_guild(member.guild.id).channels:
        if ch.name == "основной":
            await bot.get_channel(ch.id).send(
                f"{member}, покинул наш увлекательный канал, но он может вернуться снова"
            )


@bot.command()
async def test(ctx):
    await ctx.send("Тест")


@bot.command()
async def cool(ctx: Context):
    await ctx.send(f"{ctx.message.author.mention}, Крут")


@bot.command()
async def word(ctx: Context, arg=None):
    if arg is None:
        await ctx.send(f"{ctx.message.author.mention}, Введите !word и одно слово")
    else:
        await ctx.send(f"{ctx.message.author.mention}, Ввел слово {arg}")


@bot.event
async def on_message(messages: Message):
    if "дела" in messages.content.lower():
        await messages.channel.send("Норм")
    else:
        await bot.process_commands(messages)


bot.run(settings.TOKEN)
