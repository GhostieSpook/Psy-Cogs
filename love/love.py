from discord.ext import commands
import random
import discord

class Love:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def love(self, context, member: discord.Member):
        """Love your senpai/waifu!"""
        author = context.message.author.mention
        mention = member.mention
        
        love = "**{0} loves {1} more then anyone!**"
        
        choices = ['https://i.imgur.com/bSeA9GO.gif']
        
        image = random.choice(choices)
        
        embed = discord.Embed(description=cuddle.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Love(bot)
    bot.add_cog(n)
