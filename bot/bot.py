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
    if message.author == client.user: # 만약 메시지를 보낸 사람과 봇이 서로 같을 때
        return
    if message.author.bot: # discord.User.bot 프로퍼티가 참일 때
        return

    if message.content.startswith(".전투력"):
        global calcResult
        if message.content[5:].startswith("측정"):
            calcResult = int(message.content[8:12])*3+int(message.content[13:17])*4+int(message.content[18:22])+int(message.content[23:27])+int(message.content[28:32])*2.5
            await message.channel.send("전투력 측정 결과 : "+str(calcResult))


    if message.content.startswith(".도움"):
        await message.channel.send("```cpp\n명령어 리스트\n\n.전투력 측정 (기갑 [*3.0]) (포병[*4.0]) (보병 [*1.0]) (해상 [*1.0]) (공중 [*2.5])\n\n- 이때 소괄호 안에 있는 수는 4자리에 맞춰저 있어야 합니다. (ex. 0001)```")


client.run('NzU3NDI1NDUzNjcyOTU1OTQ1.X2gNbA.CttTKiomVI-YWzjpfUuJJOE5Tnk')
