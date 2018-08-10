from discord.ext import commands
import random
import discord

class Molest:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def molest(self, context, member: discord.Member):
        """Molest someone. Just do not involve the kids!"""
        author = context.message.author.mention
        mention = member.mention
        
        molest = "**{0} Molests {1}!**"
        
        choices = ['https://i.imgur.com/ggGUG8n.gifv', 'https://i.imgur.com/UZdI8r9.gifv', 'https://i.imgur.com/iQGR92x.gifv', 'https://i.imgur.com/YL1ppb3.gifv']
        
        image = random.choice(choices)
        
        embed = discord.Embed(description=molest.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Molest(bot)
    bot.add_cog(n)
