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

    if message.content.startswith("?전투력"):
        global con1, con2, conr1, conr2
        if message.content[5:].startswith("측정"):
            con1 = message.content[12:14]
            con2 = message.content[40:42]
            if message.content[8:].startswith("FLT"):
                conr1 = int(message.content[15:19])*3+int(message.content[20:24])*4+int(message.content[25:29])+int(message.content[30:34])+int(message.content[35:39])*2.5
                conr2 = int(message.content[43:47])*3+int(message.content[48:52])*4+int(message.content[53:57])+int(message.content[58:62])+int(message.content[63:67])*2.5
                await message.channel.send("평지에서\n" + str(con1) + "의 전투력 측정 결과 : " + str(conr1) + "\n\n" + str(con2) + "의 전투력 측정 결과 : " + str(conr2))
            elif message.content[8:].startswith("CTR"):
                conr1 = int(message.content[15:19])*0.1+int(message.content[20:24])*4+int(message.content[25:29])*2+int(message.content[30:34])*0.1+int(message.content[35:39])*0.5
                conr2 = int(message.content[43:47])*0.1+int(message.content[48:52])*4+int(message.content[53:57])*2+int(message.content[58:62])*0.1+int(message.content[63:67])*0.5
                await message.channel.send("시가지에서\n" + str(con1) + "의 전투력 측정 결과 : " + str(conr1) + "\n\n" + str(con2) + "의 전투력 측정 결과 : " + str(conr2))

    if message.content.startswith(".도움"):
        await message.channel.send("```cpp\n명령어 리스트\n\n.전투력 측정 (기갑 [*3.0]) (포병[*4.0]) (보병 [*1.0]) (해상 [*1.0]) (공중 [*2.5])\n\n?전투력 측정 (CTR[City Area]/FLT[Flat]) (나라이름 1[2자리]) (기갑) (포병) (보병) (해상) (공중) (나라이름 2[2자리]) (기갑) (포병) (보병) (해상) (공중)\n\n- 이때 소괄호 안에 있는 수는 4자리에 맞춰저 있어야 합니다. (ex. 0001)```")



client.run('TOKEN HERE')
