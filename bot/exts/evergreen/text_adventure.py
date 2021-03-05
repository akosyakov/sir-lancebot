import logging

import discord
from discord.ext import commands

from bot.constants import Colours

log = logging.getLogger(__name__)


class TextAdventure(commands.Cog):
    """This is the cog for the text adventure command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(name="text_adventure", aliases=("adventure", "adv"))
    async def text_adv_group(self, ctx: commands.Context) -> None:
        """Group containing text_adventure commands."""
        if not ctx.invoked_subcommand:
            await ctx.send_help(ctx.command)

    @text_adv_group.command(name="make")
    async def make(self, ctx: commands.Context) -> None:
        """Returns a link to help make your own campaign."""
        embed = discord.Embed(
            title="Making a Campaign",
            color=Colours.python_blue
        )
        embed.add_field(
            name="Wanting to make a campaign?",
            value="Go to [this link](http://bit.ly/3rnhGqN) for a guide!"
        )
        await ctx.send(embed=embed)


def setup(bot: commands.Bot) -> None:
    """Loads the adventure cog."""
    bot.add_cog(TextAdventure(bot))
