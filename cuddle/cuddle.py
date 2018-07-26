from discord.ext import commands
import random
import discord

class Cuddle:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def cuddle(self, context, member: discord.Member):
        """Cuddle your senpai/waifu!"""
        author = context.message.author.mention
        mention = member.mention
        
        cuddle = "**{0} cuddles {1}!**"
        
        choices = ['https://i.imgur.com/ntqYLGl.gif', 'https://i.imgur.com/UMm95sV.gif']
        
        image = random.choice(choices)
        
        embed = discord.Embed(description=cuddle.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Cuddle(bot)
    bot.add_cog(n)
