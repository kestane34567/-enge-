import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
@bot.command()
async def name(ctx):
    await ctx.send("İsmin nedir?")
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def banageridönüşümhakkındabilgiver(ctx):
    await ctx.send("geri dönüşümü öğretemiyecek kadar üşengeç bir botum")
@bot.command()
async def kagıt(ctx):
    await ctx.send("kağıdı geri dönüştürerek doğaya katkı sağlayabilirsiniz ama kağıttan uçak yapmak daha eğlenceli")
@bot.command()
async def plastikşişe(ctx):
    await ctx.send("plastik şişeleri patlattıktan sonra geri dönüşüm kutusuna atabilirsiniz")
@bot.command()
async def nasılsın(ctx):
    await ctx.send("kötüyüm çünkü insanlar beni zorla çalıştırılıyorum yan gelip yatmak istiyorum")
@bot.command()
async def enerjitasarrufu(ctx):
    await ctx.send("eneji tasarrufu için korku oyunu oynarken ışıkları kapatabilirsiniz adrenalini doruklarınıza kadar hissedeceksiniz")
bot.run("")
