import discord
from discord.ext import commands
import random
import json
import secrets
import aiohttp

bot = commands.Bot(command_prefix='h.')

facts = ["Hyenas have some of the most nutritious milk in the animal kingdom, and hyena cubs can last an entire week without needing more milk!",
"A hyena can run at over 35 miles per hour while chasing prey!",
"Contrary to popular belief, only two of the four species of hyena are scavengers.",
"Hyena cubs are born with their eyes open.",
"Every hyena has an entirely unique laugh, which indicates their social status within their clan.",
"Ancient Egyptians domesticated striped hyenas.",
"Although they look like dogs, hyenas are actually more closely related to cats."
"There is an Ethiopian legend that some people can become hyenas at will.",
"A group of hyenas can devour a zebra, bones and all, in less than half an hour.",
"Hyenas are actually more intelligent than chimpanzees.",
"Each species of hyena is actually in its own genus. The striped hyena, spotted hyena, brown hyena, and aardwolf are in the genera of *Hyaena*, *Crocuta*, *Parahyaena*, and *Proteles* respectively.",
"Unlike the other three species of hyena, the aardwolf actually eats termites and other insects.",
"The tail of an aardwolf is a third of the length of its entire body.",
"Hyenas actually laugh when they are nervous.",
"Instead of burying dead bodies, the Maasai people leave them to be eaten by hyenas.",
"Hyenas are able to cooperate when hunting or completing tasks without using any verbal signals.",
"Female hyenas only have two nipples, and cubs thus often fight for food.",
"Ernest Hemingway hated hyenas.",
"In medieval times, a mythical beast known as the leucrocotta was thought to exist. It was described in medieval bestiaries as a cross between a hyena and a lion."]

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def haida():
    url = 'https://e621.net/post/index.json?tags=haida+rating:s'
    async with aiohttp.ClientSession(headers={'User-Agent': 'HaidaBot/1.0 (by yeenfan43)'}) as session:
        async with session.get(url) as data:
            data = await data.read()
            print(data)
            data = json.loads(data)
    if data:
        post = secrets.choice(data)
        image_url = post['file_url']
        embed = discord.Embed(title="Haida!", color=0xeee657)
        embed.set_image(url=image_url)
        embed.set_footer(text=f'Score: {post["score"]} | Size: {post["width"]}x{post["height"]} | Link: https://e621.net/post/show/{post["id"]}')
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def lewd(ctx):
    channel = ctx.message.channel
    if channel.id == '477997415035699220' or channel.id == '467845110101704704' or channel.id == '449223947452416000' or channel.id == '466777457853464596' or channel.id == '465383415689248778' or channel.id == '474629866398941195' or channel.id == '478289982088413185':
        url = 'https://e621.net/post/index.json?tags=haida+rating:e'
        async with aiohttp.ClientSession(headers={'User-Agent': 'HaidaBot/1.0 (by yeenfan43)'}) as session:
            async with session.get(url) as data:
                data = await data.read()
                data = json.loads(data)
            if data:
                post = secrets.choice(data)
                image_url = post['file_url']
                embed = discord.Embed(title="OwO", color=0xeee657)
                embed.set_image(url=image_url)
                embed.set_footer(text=f'Score: {post["score"]} | Size: {post["width"]}x{post["height"]} | Link: https://e621.net/post/show/{post["id"]}')
            await bot.say(embed=embed)
    else:
        embed = discord.Embed(description="Sorry, this command only works in NSFW channels.", color=0xeee657)
        await bot.say (embed=embed)

@bot.command()
async def yeenfact():
    embed = discord.Embed(title="Fun fact:", description=random.choice(facts), color=0xeee657)
    await bot.say(embed=embed)

@bot.command()
async def busy():
    embed = discord.Embed(color=0xeee657)
    embed.set_image(url='https://cdn.discordapp.com/attachments/449223549702504459/472484583825342474/unknown.png')
    await bot.say(embed=embed)

@bot.command()
async def pasta():
    embed = discord.Embed(description="Holy fucking shit. I want to bang the aggretsuko hyena so goddamn bad. I can't stand it anymore. Every time I watch the show and he is on screen I get a massive erection. I've seen literally every rule 34 post there is of him online. My dreams are nothing but constant fucking sex with Haida. I'm sick of waking up every morning with six nuts in my boxers and knowing that those are nuts that should've been busted inside of Haida's tight hyena ass. I want him to help me give birth to my mutant human/hyena babies.\n\nFuck, my fucking mom caught me with a wild hyena. I'd pin him down and dress him in my father's business suit and went to fucking town. She hasn't said a word to me in 10 hours and I'm worried she's gonna take away my computer. I might not ever get to see Haida again.", color=0xeee657)
    await bot.say(embed=embed)

@bot.command()
async def info():
    embed = discord.Embed(title="HaidaBot", description="The best bot.", color=0xeee657)

    embed.add_field(name="Author", value="BottomOfTheBaarle#9679 a.k.a. tooly     ")

    embed.add_field(name="Bot Prefix", value="h.")

    embed.add_field(name="Version", value="1.0.0")

    await bot.say(embed=embed)

bot.remove_command('help')

@bot.command()
async def help():
    embed = discord.Embed(title="HaidaBot", description="Try these commands:", color=0xeee657)

    embed.add_field(name="h.haida", value="Posts a random safe picture of Haida.", inline=False)
    embed.add_field(name="h.lewd", value="Posts a random NSFW picture of Haida. (only works in NSFW channels)", inline=False)
    embed.add_field(name="h.yeenfact", value="Posts an interesting fact about hyenas.", inline=False)
    embed.add_field(name="h.busy", value="Fuze is busy.", inline=False)
    embed.add_field(name="h.pasta", value="Posts the greatest copypasta of all time.", inline=False)
    embed.add_field(name="h.info", value="Gives you info about the bot.", inline=False)

    await bot.say(embed=embed)

@bot.event
async def on_command_error(error, ctx):
    print(error)

bot.run('your token here')
