import os
import discord
from discord.ext import commands
import random

my_secret = os.environ['TOKEN']


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = ['!', '$'], case_insensitive= True, owner_id = 727569796048355328, intents = intents)


@client.event
async def on_ready():
  bot_channel = client.get_channel(881873243294793798)
  await bot_channel.send("Bot is online")
  print("Bot is ready")

@client.event
async def on_member_join(member):
  bot_channel = client.get_channel(881873243294793798)
  embed = discord.Embed(title="Welcome!",description=f"Welcome to the server {member.mention}!", color=discord.Color.dark_teal())
  thumbnail_url = member.avatar_url
  embed.set_thumbnail(url=thumbnail_url)
  await bot_channel.send(embed=embed)

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong!')
  await ctx.send(f"Hello {ctx.author.name}!")

@client.command(aliases =["8ball", "test"])
async def _8ball(ctx, questions):
  responses = ["Yes", "No", "Definitely", "Unsure" ]
  await ctx.send(f"Question: {questions}\nAnswer: {random.choice(responses)}")

@client.event
async def on_message(message):
   github_channel = client.get_channel(875719363649478666)
   if 'https://' in message.content and message.channel==github_channel:
      await message.delete()
      await message.channel.send(f"{message.author.mention} Don't send links!")
   else:
      await client.process_commands(message)
  


client.run(my_secret)