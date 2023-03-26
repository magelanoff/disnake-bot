import disnake
from disnake.ext import commands

bot = commands.InteractionBot(intents = disnake.Intents.all())

@bot.event
async def on_ready():
    print("Бот запущен")

@bot.slash_command(name = "пинг", description = "Пинг-понг")
async def ping(interaction):
    latenc = round(bot.latency * 1000)
    await interaction.response.send_message(f"**Pong!**\n`{latenc} ms`)

@bot.user_command()
async def hug(interaction, user):
    if user == interaction.author or user.bot:
        await interaction.response.send_message(":x: Вы не можете использовать команду на себя или на бота")
    else:
        await interaction.response.send_message(f"{interaction.author.mention} обнимает {user.mention}")

bot.run('token')
