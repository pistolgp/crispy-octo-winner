import asyncio
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='>')

'''
봇이 반응을 해야하는 명령어인지 구분하기 위해 메세지 앞에 붙이는 접두사(prefix)를 설정합니다. 현재 >로 
설정되어있습니다. 이곳을 변경시 해당 문자로 명령어를 시작해야합니다. ext에선 discord.Client() 클래스 처럼 
str.startswith 메서드를 사용할 필요가 없습니다.
'''

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name) # 토큰으로 로그인 된 bot 객체에서 discord.User 클래스를 가져온 뒤 name 프로퍼티를 출력
    print(bot.user.id) # 위와 같은 클래스에서 id 프로퍼티 출력
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def 전투력(ctx, loc, con1, conf1, conf2, conf3, conf4, conf5, boost1):
    global conr1, conr1rounded, conr1multiplied

    
    if loc == 'CTR' or loc == 'ctr' or loc == '시가지':
        conr1 = int(conf1)*0.1 + int(conf2)*2 + int(conf3)*4 + int(conf4)*0.1 + int(conf5)*0.5
        conr1rounded = round(float(conr1), 2)
        conr1multiplied = float(conr1rounded) * float(boost1)
        await ctx.send('```{}의 전투력은 {} 입니다.\n\n\n전술/전략 부스트는 {}배 입니다.```'.format(con1, conr1multiplied, boost1))

    elif loc == 'FLT' or loc == 'flt' or loc == '평지':
        conr1 = int(conf1)*3 + int(conf2)*4 + int(conf3)*1 + int(conf4)*1 + int(conf5)*2.5
        conr1rounded = round(float(conr1), 2)
        conr1multiplied = float(conr1rounded) * float(boost1)
        await ctx.send('```{}의 전투력은 {} 입니다.\n\n\n전술/전략 부스트는 {}배 입니다.```'.format(con1, conr1multiplied, boost1))
    else:
        await ctx.send('ㅋ 그런 장소는 없는걸?')

@bot.command()
async def 도움(ctx):
    await ctx.send('```=== 명령어 도움말 ===\n\n\n>전투력 (시가지/평지) (나라이름) (기갑) (포병) (보병) (해상) (공중) (전술/전략 부스트)\n\n\n소괄호 : 필수 / 대괄호 : 선택```')

@bot.command()
async def 전투(ctx):
    await ctx.send('``````')


bot.run('TOKEN HERE')
