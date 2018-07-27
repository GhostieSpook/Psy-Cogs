from discord.ext import commands
import random
import discord

class Hug:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def hug(self, context, member: discord.Member):
        """Hug your senpai/waifu!"""
        author = context.message.author.mention
        mention = member.mention
        
        hug = "**{0} gave {1} a hug!**"
        
        choices = ['http://i.imgur.com/sW3RvRN.gif', 'http://i.imgur.com/gdE2w1x.gif', 'http://i.imgur.com/zpbtWVE.gif', 'http://i.imgur.com/ZQivdm1.gif', 'http://i.imgur.com/MWZUMNX.gif']
        
        image = random.choice(choices)
        
        embed = discord.Embed(description=hug.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Hug(bot)
    bot.add_cog(n)
