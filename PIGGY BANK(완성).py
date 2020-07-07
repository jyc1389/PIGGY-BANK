import asyncio
import discord
import random
from discord.ext import commands
from discord.utils import get
from Dtime import Uptime
import openpyxl


app = commands.Bot(command_prefix='`')
uptime = Uptime.uptimeset()

notice = list()

@app.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title=":no_entry: 오류 발생 :no_entry:\n**존재하지 않는 명령어입니다.**", description="**error code : 4932-S7FK-34DE-SI73** \n**오류가 났다면 저에게 DM으로 오류코드를 보내주세요.**", color=0xff0000)
        await ctx.send(content=ctx.author.mention, embed=embed)

@app.event
async def on_member_join(member):
    await member.send("반갑습니다. 저희 서버에 오신 것을 환영합니다. 규칙을 먼저 읽고 활동해주세요.")


@app.event
async def on_ready():
    print("======================================")
    print("서버와의 연결이 성공적으로 끝났습니다")
    print("다음 로봇으로 로그인 합니다 : ")
    print(app.user.name)
    print("Hello, Welcome", app.user.name)
    print("=======================================")

    game = discord.Game("시작하는 중...")
    await asyncio.sleep(1)
    await app.change_presence(status=discord.Status.online, activity=game)
    while True:

        game = discord.Game("코드를 사용하시려면 \"가입\"을 눌러주세요")
        await app.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)

        ch = len(app.users)
        game = discord.Game("{}명의 사용자와 함께하는 중입니다".format(ch))
        await app.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)

        ch = len(app.guilds)
        game = discord.Game("{}개의 서버와 함께하는 중입니다".format(ch))
        await app.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)

        game = discord.Game("SEVENBOT ver.1.0.4ㅣ`도움말")
        await app.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)


@commands.has_permissions(administrator=True)
@app.command(name="청소", pass_context=True)
async def _clear(ctx, *, amount=1):
    await ctx.channel.purge(limit=amount)

@commands.has_permissions(administrator=True)
@app.command()
async def DM(ctx, user: discord.Member, *, msg):
    await ctx.send(" 로딩 중...")
    await asyncio.sleep(1)
    amount = 1
    await ctx.channel.purge(limit=amount)
    await user.send(msg)
    embed = discord.Embed(title="한 우편부가 로켓을 타고 우편을 배달했어요.", color=0xff8DC)
    embed.set_thumbnail(url="https://ifh.cc/g/DzmXyE.png")
    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
    await ctx.channel.send(embed=embed)


@DM.error
async def DM_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title=":no_entry: 오류 발생 :no_entry:\n**해당 명령어를 사용할 권한이 없습니다.**", color=0xff0000)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(content=ctx.author.mention, embed=embed)


    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title=":no_entry: 오류 발생 :no_entry:\n**DM을 보낼 메세지가 입력되지 않았습니다.**", color=0xff0000)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(content=ctx.author.mention, embed=embed)



    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(title=":no_entry: 오류 발생 :no_entry:\n**DM을 보낼 유저가 입력되지 않았습니다.**", color=0xff0000)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(content=ctx.author.mention, embed=embed)


@commands.has_permissions(administrator=True)
@app.command()
async def 공채설정(ctx, channel: discord.TextChannel):
    if channel in notice:
        await ctx.send("이미 등록되어 있는 채널입니다.")
    else:
        notice.append(channel)
        await ctx.send(" 설정이 완료되었습니다.")

@commands.has_permissions(administrator=True)
@app.command()
async def 공지(ctx, *, msg):
    for i in notice:
        await i.send(msg)

@app.command()
async def 프로필(ctx):
    embed = discord.Embed(title="**PIGGY BANK**", description="이것은 **PIGGY BANK**의 프로필입니다.", color=0xFF88C00)
    embed.set_author(name="PIGGY BANK", icon_url="https://ifh.cc/g/IHppOJ.png")
    embed.set_thumbnail(url="https://ifh.cc/g/IHppOJ.png")
    embed.add_field(name="****이름****", value="SEVENBOT.", inline=False)
    embed.add_field(name="****제작자****", value="GODSEVEN#8308", inline=False)
    embed.add_field(name="****제작기간****", value="5월28일부터 진행 중", inline=False)
    embed.add_field(name="****도움****", value="연어봇", inline=False)
    embed.set_footer(text="`VER.1.0.48")
    await ctx.channel.send(embed=embed)


@app.command()
async def 꿀(ctx, *, msg):
    await ctx.send(msg)


@app.command()
async def 업타임(ctx):
    uptime = str(Uptime.uptime()).split(":")
    hours = uptime[0]
    minitues = uptime[1]
    seconds = uptime[2].split(".")[0]
    await ctx.send(f"**{hours}**시간 **{minitues}**분 **{seconds}**초동안 구동 중입니다.")


@app.command()
async def 핑(ctx):
    if (round(app.latency * 1000)) > 210:
        embed = discord.Embed(title="현재 핑: {0}ms \n상태 : 불안정 ⛔".format(round(app.latency * 1000)), color=0xff0000)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="현재 핑: {0}ms \n상태 : 양호 ✅".format(round(app.latency * 1000)), color=0x00ff00)
        await ctx.send(embed=embed)


@app.command()
async def 명령어(ctx):
    embed = discord.Embed(title='**PIGGY BANK** 명령어',
    description='**PIGGY BANK**을 이용하기 위한 **간단한 명령어**입니다. **더 자세한 정보**를 알고 싶으시다면 **밑에 있는 아이콘(반응)**을 클릭해주세요.', color=0xffffff)
    embed.add_field(name='📄 일반 명령어', value='**피기뱅크 서비스**에 가입한 **모든 유저**가 사용할 수 있는 명령어입니다.\n', inline=False) 
    embed.add_field(name='👮‍♂️ 관리 명령어', value='**서버를 관리**하면서 필요한 명령어입니다.\n', inline=False)
    embed.add_field(name='💻 오너 명령어', value='**피기의 주인**인 **GODSEVEN#8308**님만 사용하실 수 있는 명령어입니다.\n', inline=False)
    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
    emjs = ['📄','👮‍♂️','💻']
    msg = await ctx.send(embed=embed)
    for em in emjs:
        await msg.add_reaction(em)
    

    def check(reaction, user):
            return user == ctx.author and msg.id == reaction.message.id and reaction.emoji in ['📄','👮‍♂️','💻']

 
    try:
        reaction, user = await app.wait_for('reaction_add', check=check, timeout=1000000000000)
    except asyncio.TimeoutError:
        await msg.delete(embed=embed)

    else: 
        if reaction.emoji == '📄':
            embed = discord.Embed(title='**📄 일반 명령어**\n**피기뱅크 서비스**에 가입한 **모든 유저**가 사용할 수 있는 명령어입니다.', description="\n\n**📄 일반 명령어 목록** \n**꿀** - 꿀 뒤에 오는 단어를 따라합니다. \n**등록** - 사용자를 등록합니다. (개발 중임) \n**프로필** - **PIGGY BANK**의 프로필을 보여줍니다. \n**업타임** - **PIGGY BANK**가 구동된 총 시간을 보여줍니다. \n**명령어** - **PIGGY BANK**의 모든 명령어를 보여줍니다.(오너 명령어 제외) \n**초대** - **PIGGY BANK**의 초대링크를 보여줍니다. \n**핑** - **PIGGY BANK**의 현재 핑을 알려줍니다.", color=0xffffff)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            emjs = ['↩']
            await asyncio.gather(msg.remove_reaction(reaction, user))
            msg = await msg.edit(embed=embed)
            for em in emjs:
                await msg.add_reaction(em)

        if reaction.emoji == '👮‍♂️':
            embed = discord.Embed(title='**👮‍♂️ 관리 명령어**\n**서버를 관리**하면서 필요한 명령어입니다.', description="\n\n**👮‍♂️ 관리 명령어** \n**추가** - 역할을 추가할 유저를 정해 역할을 추가합니다 \n**제거** - 역할을 제거할 유저를 정해 역할을 제가합니다 \n**공채설정** - \"공지라는 명령어를 사용하기 위한 명령어\"이며, 공지를 할 채널을 설정합니다 \n**공지** 공채설정으로 공지할 채널을 선택해준 뒤 그 채널로 **PIGGY BANK**가 공지 내용을 전달합니다\n**청소** - 메세지가 더럽거나 보기 지저분할 떄 청소(청소할 메세지 수)를 입력해 메세지를 삭제합니다", color=0xffffff)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            emjs = ['↩']
            await asyncio.gather(msg.remove_reaction(reaction, user))
            msg = await msg.edit(embed=embed)
            for em in emjs:
                await msg.add_reaction(em)

                        
        elif reaction.emoji == '💻':
            embed = discord.Embed(title='**💻 오너 명령어**\n**피기의 주인**인 **GODSEVEN#8308**님만 사용하실 수 있는 명령어입니다.', description="오너인 **GODSEVEN#8308님**만 확인하실 수 있습니다.", color=0xffffff)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            emjs = ['↩']
            await asyncio.gather(msg.remove_reaction(reaction, user))
            msg = await msg.edit(embed=embed)
            for em in emjs:
                await msg.add_reaction(em)



@app.command(name="초대")
async def 초대(ctx):
    embed = discord.Embed(title='다른 서버에 저를 초대하실건가요?',
                        description='**PIGGY BANK**을 추가하시려면 **초대링크**를 클릭해주세요. \n \n [초대링크](https://discord.com/oauth2/authorize?client_id=728878946661171264&permissions=0&scope=bot)',
                            color=0xffffff)
    await ctx.send(embed=embed)


@app.command()
async def 등록(ctx):
    embed = discord.Embed(title='**PIGGY BANK** 유저 등록',
    description='**PIGGY BANK**를 이용하기 위한 **이용약관** 및 **개인정보 취급방침**입니다. PIGGY BANK의 모든 기능을 사용하려면 동의가 필요합니다.', color=0xffffff)
    embed.add_field(name='이용약관', value='[클릭](안녕)\n', inline=True)
    embed.add_field(name='개인정보 취급방침', value='[클릭](안녕)\n', inline=True)
    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
    msg = await ctx.send(embed=embed)
    emjs = ['⭕', '❌']
    for em in emjs:
        await msg.add_reaction(em)

    def check(reaction, user):
        return user == ctx.author and msg.id == reaction.message.id and reaction.emoji in ['⭕', '❌']


    try:
        reaction, user = await app.wait_for('reaction_add', check=check, timeout=60)
    except asyncio.TimeoutError:
        amount = 1
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title='**⏱\t시간이 초과되었습니다.**', description="60초가 지나 가입이 자동 취소되었습니다. 다시 시도해주세요.", color=0xff0000)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await msg.edit(embed=embed)

    else: 
        if reaction.emoji == '⭕':
            embed = discord.Embed(title='**✅등록이 승인되셨습니다.**', description="**PIGGY BANK**에 대해 알고 싶다면  **\"`명령어\"** 이라고 입력해주세요.*", color=0x00ff00)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await asyncio.gather(msg.remove_reaction(reaction, user))
            await msg.edit(embed=embed)

        elif reaction.emoji == '❌':
            embed = discord.Embed(title='**⛔등록이 취소되셨습니다.**', description="**잠시 생각하신 뒤, 다시 시도해주세요.**", color=0xff0000)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await asyncio.gather(msg.remove_reaction(reaction, user))
            await msg.edit(embed=embed)




@commands.has_permissions(administrator=True)
@app.command()
async def 추가(ctx, user: discord.Member, txt):
    if ctx.author.guild_permissions.administrator:
        b = txt
        role = discord.utils.get(ctx.guild.roles, name=f"{b}")
        await user.add_roles(role)
        await ctx.send("전달 완료!")

@추가.error
async def 추가_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title=":no_entry: 오류 발생 :no_entry:\n**해당 명령어를 사용할 권한이 없습니다.**", color=0xff0000)
        await ctx.send(content=ctx.author.mention, embed=embed)


    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title=":no_entry: 오류 발생 :no_entry:\n**역할을 추가할 역할또는 유저가 입력되지 않았습니다.**", color=0xff0000)
        await ctx.send(content=ctx.author.mention, embed=embed)



    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(title=":no_entry: 오류 발생 :no_entry:\n**역할을 추가할 유저가 입력되지 않았습니다.**", color=0xff0000)
        await ctx.send(content=ctx.author.mention, embed=embed)

@commands.has_permissions(administrator=True)
@app.command()
async def 제거(ctx, user: discord.Member, txt):
    if ctx.author.guild_permissions.administrator:
        b = txt
        role = discord.utils.get(ctx.guild.roles, name=f"{b}")
        await user.remove_roles(role)
        await ctx.send("회수 완료!")
    else:
        await ctx.send("관리자권한이 없음")

@제거.error
async def 제거_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title=":no_entry: 오류 발생 :no_entry:\n**해당 명령어를 사용할 권한이 없습니다.**", color=0xff0000)
        await ctx.send(content=ctx.author.mention, embed=embed)


    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title=":no_entry: 오류 발생 :no_entry:\n**역할을 제거할 역할또는 유저가 입력되지 않았습니다.**", color=0xff0000)
        await ctx.send(content=ctx.author.mention, embed=embed)



    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(title=":no_entry: 오류 발생 :no_entry:\n**역할을 제거할 유저가 입력되지 않았습니다.**", color=0xff0000)
        await ctx.send(content=ctx.author.mention, embed=embed)




@commands.has_permissions(administrator=True)
@app.command(name="추방", pass_context=True)
async def _kick(ctx, *, user_name: discord.Member, reason=None):
    await user_name.kick(reason=reason)
    await ctx.send(str(user_name) + "을(를) 추방하였습니다.")

@_kick.error
async def _kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title=":no_entry: 오류 발생 :no_entry:\n**해당 명령어를 사용할 권한이 없습니다.**", color=0xff0000)
        await ctx.send(content=ctx.author.mention, embed=embed)


    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title=":no_entry: 오류 발생 :no_entry:\n**추방할 역할또는 유저가 입력되지 않았습니다.**", color=0xff0000)
        await ctx.send(content=ctx.author.mention, embed=embed)




app.run("NzI4ODc4OTQ2NjYxMTcxMjY0.XwAzkA.BN4M0JO9JDY-qsHqtYI25tduLgc")