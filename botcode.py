import discord, random
from discord.ext import commands
client=commands.Bot(command_prefix='/')
@client.event
async def on_ready():
    activity = discord.Game(name="Netflix And Chill", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member=None):
    if not member:
        await ctx.send('Please mention a member')
        return
    await member.kick()
    await ctx.send(f'{member.display_name} was kicked from the server')
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member=None):
    if not member:
        await ctx.send('Please mention a member')
        return
    await member.ban()
    await ctx.send(f'{member.display_name} was banned from the server')
@client.command()
async def Latency(ctx):
    await ctx.send(f"Latency is {round(client.latency) * 1000}ms")
@client.command()
async def Yeet(ctx): 
    await ctx.send('Indeed yeet')
@client.command()
async def introduce(ctx): 
    await ctx.send('Hey My Name Is Corrupt Clan Bot Made By Loodie09')

client.run('Nzc4NjUwMjYyOTIzMTE2NTQ3.X7VEkQ.z33cMT_0fPgbhB6Tycve8m5V_dY')