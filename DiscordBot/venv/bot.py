import discord
import responses
import piechart
import count

filePath = 'C:/Users/Emily Rose/source/repos/DiscordBot/'

async def send_message(message, user_message, is_private):
    try:
        response= responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    file1 = open(filePath+ 'JobotID.txt', 'r')
    file2 = open(filePath+ 'ChannelID.txt', 'r')


    TOKEN= str(file1.readline())
    channelID = int(file2.readline())
    intents=discord.Intents.default()
    intents.message_content=True
    client = discord.Client(intents=intents)

    #server = client.get_server("526231258519437313")
    #for channel in server.channels:
        #if channel.name == "Channel name":
            #break


    @client.event
    async def on_ready():
        his = await get_result(channelID)
        count.retrieve_messages(his)
        piechart.makechart(count.numList, count.userList, filePath)
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.channel.id == channelID:
            count.addCount(message)
            piechart.makechart(count.numList, count.userList, filePath)
        username= str(message.author)
        user_message= str(message.content)
        channel= str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if len(user_message)==0:
            t=1#do nothing
        elif(user_message[0]=='?'):
            user_message=user_message[1:]
            await send_message(message, user_message, is_private=True)
        elif (user_message== '!chart'):
            with open(filePath + 'countingPie.png', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file=picture)
        else:
            await send_message(message, user_message, is_private=False)

    async def get_result(id):
        l = []
        channelName = client.get_channel(id)
        async for i in channelName.history(oldest_first=True, limit= 100000):
            l.append(i)
        return l

    client.run(TOKEN)