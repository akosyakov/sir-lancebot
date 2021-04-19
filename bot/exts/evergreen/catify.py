import random
from typing import Optional

from discord.ext import commands

from bot.constants import Cats


class Catify(commands.Cog):
    """Cog for the catify command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["ᓚᘏᗢify", "ᓚᘏᗢ"])
    async def catify(self, ctx: commands.Context, *string: Optional[str]) -> None:
        """Catifies a string or username."""
        if string == ():
            username = ctx.author.name
            if len(username) >= 28:
                return await ctx.send("Your username is too long to be catified! Please change it.")
            else:
                username += f" | {random.choice(Cats.cats)}"
                await ctx.send(f"Your catified username is: `{username}`")
                await ctx.author.edit(nick=username)
        else:
            string = " ".join(string)
            string_list = string.split()
            print(len(string_list))
            for index, name in enumerate(string_list):
                if "cat" in name:
                    string_list[index] = string_list[index].replace("cat", 'ᓚᘏᗢ')

            for _i in range(random.randint(1, len(string_list)//3)):
                # insert cat at random index
                string_list.insert(random.randint(0, len(string_list)-1), "ᓚᘏᗢ")

                string = " ".join(string_list)

                await ctx.channel.send(string)


def setup(bot: commands.Bot):
    """Loads the catify cog."""
    bot.add_cog(Catify(bot))
