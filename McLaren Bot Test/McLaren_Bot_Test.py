import asyncio
import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행 준비가 되었을 때 행동할 것
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message): # 입력되는 메세지에서 찾기
    if message.content.startswith('!ping'): # 만약 메세지가 '!ping'으로 시작된다면
        await message.channel.send('pong') # 클라이언트는 메세지가 올라온 채널에 'pong'을 보냅니다.

    if message.content.startswith('!pong'):
        await message.channel.send('ping!')

    if message.content.startswith('!콩자반'):
        await message.channel.send('병신새끼')

    if message.content.startswith('dw'):
        await message.channel.send('fdzz')

    if message.content.startswith('ㅇㅈ'):
        await message.channel.send('ㄹㅇㅋㅋ')

    if message.content.startswith('자반콩'):
        await ctx.channel.purge(1)

    
    #if message.content.startswith("!cal"):
        #global calcResult

        #if message.content[5:].startswith("plus"):
            #calcResult = int(message.content[10:14])+int(message.content[15:19])
            #await message.channel.send("Result : "+str(calcResult))
    


    '''
    on_message에서 또다른 명령어 추가를 위해
    if message.content.startswith를 추가해야하는데, elif가 아닌 개별 if를 사용하는 것을 추천합니다.
    '''
client.run('NzU3NDA2ODcyNzYzNDk4NTY2.X2f8Hg.ZedsCKAIGafdFbC4Pnj_g03zkGs')
