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

    if message.content.startswith("!전투력"):
        global con1, con2, conr1, conr2
        if message.content[5:].startswith("측정"):
            if message.content[12:].startswith("도움"):
                if message.content[8:].startswith("FLT"):
                    await message.channel.send("```평지에서의 전투력을 측정합니다. 기갑은 3배, 포병은 4배, 보병과 해상은 1배 공중은 2.5배 후 더하여 전투력이 계산됩니다.```")
                elif message.content[8:].startswith("CTR"):
                    await message.channel.send("```도심에서의 전투력을 측정합니다. 기갑은 0.1배, 포병은 2배, 보병은 4배, 해상은 0.1배 공중은 0.5배 후 더하여 전투력이 계산됩니다.```")
            else:
                con1 = message.content[12:14]
                con2 = message.content[40:42]
                global con11, con12, con13, con14, con15, con21, con22, con23, con24, con25, result, nj, boost
                nj = 0
                if con1 == con2:
                    await message.channel.send("**경고 : 두 나라가 서로 같습니다. 이는 한 나라 안에서의 내전 취급을 받으며 첫 번째 나라가 정부군, 두 번째 나라가 반란군으로 간주됩니다.**\n\n\n")
                    nj = 1
                con11 = int(message.content[15:19])
                con12 = int(message.content[20:24])
                con13 = int(message.content[25:29])
                con14 = int(message.content[30:34])
                con15 = int(message.content[35:39])
                con21 = int(message.content[43:47])
                con22 = int(message.content[48:52])
                con23 = int(message.content[53:57])
                con24 = int(message.content[58:62])
                con25 = int(message.content[63:67])
                if message.content[8:].startswith("FLT"):
                    conr1 = con11*3 + con12*4 + con13 + con14 + con15*2.5
                    conr2 = con21*3 + con22*4 + con23 + con24 + con25*2.5
                    if nj == 1:
                        if conr1 == conr2:
                            await message.channel.send("```평지에서 " + str(con1) + " 내전은 비겼습니다.\n\n" + str(con1) + "의 전투력은 " + str(conr1) + ".\n\n" + str(con2) + "의 전투력은 " + str(conr2) + " 입니다.```")
                        elif conr1 > conr2:
                            result = conr1-conr2
                            await message.channel.send("```평지에서 " + str(con1) + " 내전은 " + str(con1) + "정부군의 승리로 끝이 났습니다.\n\n" + str(con1) + "정부군의 전투력은 " + str(conr1) + ".\n\n" + str(con2) + "반란군의 전투력은 " + str(conr2) + "이였으며\n\n두 세력간 전투력 격차는 " + str(result) + "입니다.```")
                        elif conr1 < conr2:
                            result = conr2-conr1
                            await message.channel.send("```평지에서 " + str(con1) + " 내전은 " + str(con1) + "반란군의 승리로 끝이 났습니다.\n\n" + str(con1) + "반란군의 전투력은 " + str(conr2) + ".\n\n" + str(con1) + "정부군의 전투력은 " + str(conr1) + "이였으며\n\n두 세력간 전투력 격차는 " + str(result) + "입니다.```")
                    elif nj == 0:
                        if conr1 == conr2:
                            await message.channel.send("```평지에서 " + str(con1) + ", " + str(con2) + "간 전쟁은 비겼습니다.\n\n" + str(con1) + "의 전투력은 " + str(conr1) + ".\n\n" + str(con2) + "의 전투력은 " + str(conr2) + " 입니다.```")
                        elif conr1 > conr2:
                            result = conr1-conr2
                            await message.channel.send("```평지에서 " + str(con1) + ", " + str(con2) + "간 전쟁은 " + str(con1) + "의 승리로 끝이 났습니다.\n\n" + str(con1) + "의 전투력은 " + str(conr1) + ".\n\n" + str(con2) + "의 전투력은 " + str(conr2) + "이였으며\n\n두 나라간 전투력 격차는 " + str(result) + "입니다.```")
                        elif conr1 < conr2:
                            result = conr2-conr1
                            await message.channel.send("```평지에서 " + str(con2) + ", " + str(con1) + "간 전쟁은 " + str(con2) + "의 승리로 끝이 났습니다.\n\n" + str(con2) + "의 전투력은 " + str(conr2) + ".\n\n" + str(con1) + "의 전투력은 " + str(conr1) + "이였으며\n\n두 나라간 전투력 격차는 " + str(result) + "입니다.```")
                    else:
                        await message.channel.send("뭔가 **크나 큰** 오류가 있었나 봅니다. 개발자에게 DM해보시기 바랍니다.\n\n오류코드:FLTNJERROR")
                elif message.content[8:].startswith("CTR"):
                    conr1 = con11*0.1 + con12*2 + con13*4 + con14*0.1 + con15*0.5
                    conr2 = con21*0.1 + con22*2 + con23*4 + con24*0.1 + con25*0.5
                    if nj ==1:
                        if conr1 == conr2:
                            await message.channel.send("```시가지에서 " + str(con1) + " 내전은 비겼습니다.\n\n" + str(con1) + " 정부군의 전투력은 " + str(conr1) + ".\n\n" + str(con2) + " 반란군의 전투력은 " + str(conr2) + " 입니다.```")
                        elif conr1 > conr2:
                            result = conr1-conr2
                            await message.channel.send("```시가지에서 " + str(con1) + " 내전은 " + str(con1) + " 정부군의 승리로 끝이 났습니다.\n\n" + str(con1) + " 정부군의 전투력은 " + str(conr1) + ".\n\n" + str(con2) + " 반란군의 전투력은 " + str(conr2) + " 이였으며\n\n두 세력간 전투력 격차는 " + str(result) + "입니다.```")
                        elif conr1 < conr2:
                            result = conr2-conr1
                            await message.channel.send("```시가지에서 " + str(con2) + " 내전은 " + str(con2) + " 반란군의 승리로 끝이 났습니다.\n\n" + str(con2) + " 반란군의 전투력은 " + str(conr2) + ".\n\n" + str(con1) + " 정부군의 전투력은 " + str(conr1) + " 이였으며\n\n두 세력간 전투력 격차는 " + str(result) + "입니다.```")

                    elif nj == 0:
                        if conr1 == conr2:
                            await message.channel.send("```시가지에서 " + str(con1) + ", " + str(con2) + "간 전쟁은 비겼습니다.\n\n" + str(con1) + "의 전투력은 " + str(conr1) + ".\n\n" + str(con2) + "의 전투력은 " + str(conr2) + " 입니다.```")
                        elif conr1 > conr2:
                            result = conr1-conr2
                            await message.channel.send("```시가지에서 " + str(con1) + ", " + str(con2) + "간 전쟁은 " + str(con1) + "의 승리로 끝이 났습니다.\n\n" + str(con1) + "의 전투력은 " + str(conr1) + ".\n\n" + str(con2) + "의 전투력은 " + str(conr2) + " 이였으며\n\n두 나라간 전투력 격차는 " + str(result) + "입니다.```")
                        elif conr1 < conr2:
                            result = conr2-conr1
                            await message.channel.send("```시가지에서 " + str(con2) + ", " + str(con1) + "간 전쟁은 " + str(con2) + "의 승리로 끝이 났습니다.\n\n" + str(con2) + "의 전투력은 " + str(conr2) + ".\n\n" + str(con1) + "의 전투력은 " + str(conr1) + " 이였으며\n\n두 나라간 전투력 격차는 " + str(result) + "입니다.```")
                    else:
                        await message.channel.send("뭔가 **크나 큰** 오류가 있었나 봅니다. 개발자에게 DM해보시기 바랍니다.\n\n오류코드:CTRNJERROR")
                else:
                    await message.channel.send("**멍청아. 그런 코드는 존재하지 않는단다**")
        else:
            await message.channel.send("``!도움``을 사용 해 보시겠어요?")

 

    if message.content.startswith("!도움"):
        await message.channel.send("```명령어 리스트\n\n!전투력 측정 (CTR*/FLT**) 도움\n\n!전투력 측정 (CTR*/FLT**) (나라이름 1) (기갑) (포병) (보병) (해상) (공중) (나라이름 2) (기갑) (포병) (보병) (해상) (공중) [전략/전술 부스트***]\n\n- 이때 소괄호 안에 있는 수는 4자리, 대괄호 안에 있는 수는 3자리에 맞춰저 있어야 합니다. (ex. 0001)\n\n각주 * : City area. 시가지\n각주 ** : Flat. 평지\n각주 *** : 선택 사항 + 작동 안함```")



client.run('TOKEN HERE')
