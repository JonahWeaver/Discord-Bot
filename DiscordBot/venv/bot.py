import discord
import responses
import piechart
import count

async def send_message(message, user_message, is_private):
    try:
        response= responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN= 'ODQ2MTY2NTgyNzc4NjU4ODI2.GZ7KFQ.nWnGIRHlw8SCGVS0KJoZC7dTKw5RECa-L7MhRM'
    intents=discord.Intents.default()
    intents.message_content=True
    client = discord.Client(intents=intents)

    #server = client.get_server("526231258519437313")
    #for channel in server.channels:
        #if channel.name == "Channel name":
            #break


    @client.event
    async def on_ready():
        his = await get_result(1051302124522311710)
        count.retrieve_messages(his)
        piechart.makechart(count.numList, count.userList)
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.channel.id == 1051302124522311710:
            count.addCount(message)
            piechart.makechart(count.numList, count.userList)
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
            with open('C:/Users/Emily Rose/source/repos/DiscordBot/countingPie.png', 'rb') as f:
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