import fluxer
from fluxer import Cog

class Main(Cog):
    def __init(self, bot: fluxer.bot):
        super().__init__(bot)

async def setup(bot: fluxer.Bot):
    await bot.add_cog(MainCog(bot))


async def teardown(bot: fluxer.Bot):
    await bot.remove_cog("MainCog")