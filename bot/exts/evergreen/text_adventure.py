import logging

import discord
from discord.ext import commands

from bot.constants import Colours

log = logging.getLogger(__name__)


class TextAdventure(commands.Cog):
    """This is the cog for the text adventure command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["adventure"])
    async def text_adventure(self, ctx: commands.Context, command: str = 'start') -> None:
        """Play a text based adventure in python."""
        embed = discord.Embed(
            name="Text Adventure",
            description="a WIP",
            color=Colours.python_blue
        )
        await ctx.send(embed=embed)
