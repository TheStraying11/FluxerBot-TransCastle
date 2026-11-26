from dotenv import load_dotenv

load_dotenv()

import os
import fluxer

bot = fluxer.Bot(command_prefix="!", intents=fluxer.Intents.default())


@bot.event
async def on_ready():
    for cog in os.listdir('./cogs'):
        await bot.load_extension(f'cogs.{cog[:-3]}')
    print(f"Logged in as {bot.user.username}")

@bot.command()
@fluxer.has_permission(manage_guild=True)
async def reload(ctx: fluxer.Message, cog: str = "main_cog"):
    try:
        if cog not in bot.extensions:
            await bot.load_extension(f'cogs.{cog}')
        else:
            await bot.reload_extension(f'cogs.{cog}')
        ctx.reply(f"Cog: {cog} reloaded successfully")
    
    except Exception as e:
        ctx.reply(f"Cog load exception: {e}, cog '{cog}' remains unloaded")

bot.run(os.getenv("BOT_TOKEN"))