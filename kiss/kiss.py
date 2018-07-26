from discord.ext import commands
import random
import discord

class Kiss:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def kiss(self, context, member: discord.Member):
        """Kiss your senpai/waifu!"""
        author = context.message.author.mention
        mention = member.mention
        
        kiss = "**{0} gave {1} a kiss!**"
        
        choices = ['http://i.imgur.com/0D0Mijk.gif', 'http://i.imgur.com/TNhivqs.gif', 'http://i.imgur.com/3wv088f.gif', 'http://i.imgur.com/7mkRzr1.gif', 'http://i.imgur.com/8fEyFHe.gif', 'https://i.imgur.com/TBN5yWY.gif', 'https://i.imgur.com/UUuxJzq.gif', 'https://i.imgur.com/ivogXes.gif', 'https://i.imgur.com/YZAdekC.gif', 'https://i.imgur.com/ji6AZc2.gif', 'https://i.imgur.com/TEHAPd6.gif', 'https://i.imgur.com/iTD9whO.gif', 'https://i.imgur.com/GEWFMuu.gif', 'https://i.imgur.com/OhlN3e6.gif', 'https://i.imgur.com/anRd2nB.gif', 'https://i.imgur.com/fmuzqfg.gif', 'https://i.imgur.com/mQhGc3c.gif', 'https://i.imgur.com/IeWHXZ1.gif', 'https://i.imgur.com/gVo9B7b.gif', 'https://i.imgur.com/VjhcFXP.gif', 'https://i.imgur.com/KbY8A4c.gif', 'https://i.imgur.com/Uwpxpii.gif', 'https://i.imgur.com/mBZkGob.gif', 'https://i.imgur.com/fOqEnjX.gif', 'https://i.imgur.com/5xZySwF.gif', 'https://i.imgur.com/FcFHy6C.gif', 'https://i.imgur.com/H3L0eiR.gif', 'https://i.imgur.com/pU4DfAc.gif', 'https://i.imgur.com/RhZkqoH.gif', 'https://i.imgur.com/CNrADZg.gif', 'https://i.imgur.com/PEBfvGO.gif', 'https://i.imgur.com/Ac9x7bX.gif', 'https://i.imgur.com/EiTW8iL.gif', 'https://i.imgur.com/e0ep0v3.gif']
        
        image = random.choice(choices)
        
        embed = discord.Embed(description=kiss.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Kiss(bot)
    bot.add_cog(n)
