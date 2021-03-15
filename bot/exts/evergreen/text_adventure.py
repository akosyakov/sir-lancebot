import asyncio
import json
import logging

import discord
from discord.ext import commands

from bot.constants import Colours, Emojis

log = logging.getLogger(__name__)
emojilist = [Emojis.textadv_a, Emojis.textadv_b, Emojis.textadv_c]


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

    @text_adv_group.command(name="start")
    async def start(self, ctx: commands.Context, *, title: str = "monty python 1") -> None:
        """Starts a campaign."""
        with open(f"bot/resources/evergreen/adventure_campaigns/{title}.json", "r") as campaign:
            data = json.load(campaign)
            title = data["title"]
            msg = await ctx.send("Starting...")
            for element in data.values():
                embed = discord.Embed(
                    title=title,
                    color=Colours.python_blue
                )
                if type(element) == dict:
                    ei = element["ei"]
                    choicenum = 0
                    for _element in ei:
                        choicenum += 1
                        embed.add_field(
                            name="Choice " + ei["c" + str(choicenum)],
                            value=element["c" + str(choicenum)]
                        )
                    prompt = element["prompt"]
                    embed.description = prompt
                    await msg.edit(content=None, embed=embed)
                    if choicenum == 1:
                        await msg.add_reaction(Emojis.textadv_a)
                    elif choicenum == 2:
                        await msg.add_reaction(Emojis.textadv_a)
                        await msg.add_reaction(Emojis.textadv_b)
                    elif choicenum == 3:
                        await msg.add_reaction(Emojis.textadv_a)
                        await msg.add_reaction(Emojis.textadv_b)
                        await msg.add_reaction(Emojis.textadv_c)
                    else:
                        log.warning("Invalid amount of choices in campaign section. Raising error.")
                        await msg.edit(content="Uh oh! There is an error in the campaign.")

                    def check(reaction, user) -> None:
                        """Reaction check."""
                        return user == ctx.message.author and str(reaction.emoji) in emojilist
                    try:
                        reaction, user = await self.bot.wait_for('reaction_add', timeout=5, check=check)
                        if reaction.emoji == Emojis.textadv_a:
                            await msg.clear_reactions()
                            await msg.edit(content="pogchamp", embed=None)
                    except asyncio.TimeoutError:
                        await ctx.send("We timed out on our end.")


def setup(bot: commands.Bot) -> None:
    """Loads the adventure cog."""
    bot.add_cog(TextAdventure(bot))
