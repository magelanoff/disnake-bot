
# -*- coding: utf-8 -*-
import disnake
from disnake.ext import commands
import config

bot = commands.Bot(
    command_prefix = config.prefix,
    intents = disnake.Intents.all()
)

@bot.event
async def on_ready():
    print("Бот запущен!")

@bot.slash_command(
    name = "пинг",
    description = "Пинг-понг..."
)
async def _ping(interaction):
    await interaction.response.send_message("Pong!")


@bot.slash_command(
    name = "пушкин",
    description = "Биография А. С. Пушкина"
)
async def pushkin(interaction):
    embed = disnake.Embed(title = "Биография А. С. Пушкина", description = "Один из самых авторитетных литературных деятелей первой трети XIX века. Ещё при жизни Пушкина сложилась eго репутация величайшего национального русского поэта. Пушкин рассматривается как основоположник современного русского литературного языка", url = "https://ru.wikipedia.org/wiki/%D0%9F%D1%83%D1%88%D0%BA%D0%B8%D0%BD,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%A1%D0%B5%D1%80%D0%B3%D0%B5%D0%B5%D0%B2%D0%B8%D1%87", timestamp = interaction.created_at, color = 0xFFFFFF)
    embed.add_field(name = "Годы жизни", value = "`26, май 1799 г.` - `29, январь 1837 г.`", inline = False)
    embed.add_field(name = "Детство", value = "Летом родители увезли сына в Михайловское, а затем до весны 1801 года семья жила в Петербурге, у тёщи — Марии Алексеевны Ганнибал (1745—1818, урождённой Пушкиной, из другой ветви рода). В этот период вполне могла состояться часто упоминаемая встреча c Павлом I, о которой Пушкин пишет в строках «Видел я трёх царей….", inline = False)
    embed.set_image(url = "https://images-ext-1.discordapp.net/external/-qx5lAhPAUgJHe849X5vR3DNV8U_ihoDiav4Yj3LXFo/https/upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kiprensky_Pushkin.jpg/405px-Kiprensky_Pushkin.jpg?width=501&height=585")

    embed.set_footer(text = f"Запросил {interaction.author}", icon_url = interaction.author.display_avatar)

    await interaction.response.send_message(embed = embed)

bot.run(config.token)
