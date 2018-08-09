from discord.ext import commands
import random
import discord

class Rape:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def rape(self, context, member: discord.Member):
        """Rape someone. Just do not involve the kids!"""
        author = context.message.author.mention
        mention = member.mention
        
        rape = "**{0} RAPES {1}!**"
        
        choices = ['https://i.imgur.com/bSeA9GO.gif']
        
        image = random.choice(choices)
        
        embed = discord.Embed(description=rape.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Rape(bot)
    bot.add_cog(n)
