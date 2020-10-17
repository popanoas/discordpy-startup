# インストールした discord.py を読み込む
import discord
import asyncio
import os
import traceback
import random
from datetime import datetime
from discord.ext import tasks
from discord.ext import commands
import threading

CHANNEL_ID = 730136347477540908 #毎日朝5時を通知するチャンネルID
CHANNEL_ID2 = 726398497384824853 #タスクキルチャンネル
#ID_CHANNEL_1 = 670294227846037514  # 1チャンネルID（事前設定用）
#ID_CHANNEL_2 = 715596202032496760  # 2チャンネルID（事前設定用）
#ID_CHANNEL_3 = 670294262696509469  # 3チャンネルID（事前設定用）
#ID_CHANNEL_4 = 715596251927675023  # 4チャンネルID（事前設定用）
#ID_CHANNEL_5 = 670294289028350012  # 5チャンネルID（事前設定用）
#ID_CHANNEL_6 = 715596307762380811  # 6チャンネルID（事前設定用）
#ID_CHANNEL_7 = 670294326131032064  # 7チャンネルID（事前設定用）
#ID_CHANNEL_8 = 715596648570552341  # 8チャンネルID（事前設定用）
#ID_CHANNEL_9 = 670294357944958976  # 9チャンネルID（事前設定用）
#ID_CHANNEL_10 = 715596743450034188  # 10チャンネルID（事前設定用）
#ID_CHANNEL_ZANGE = 741739653245173800 #懺悔部屋のチャンネルID

ID_emoji = '<:61ok:728923368870510605>'
ID_tk = '<:syarururage:737890640519495712>'
ID_taskkill = 726398497384824853
ID_Mana = 730136347477540908
ID_emoji_zange = '<:61ok:728923368870510605>'

token = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
        
    # チャンネル1に対するアクション
    if message.content == '/1段階目':
        channel = client.get_channel(ID_CHANNEL_1)
        await channel.send('--------------------1段階目--------------------')
        
    if message.content == '/2段階目':
        channel = client.get_channel(ID_CHANNEL_1)
        await channel.send('--------------------2段階目--------------------')
  
    if message.content == '/3段階目':
        channel = client.get_channel(ID_CHANNEL_1)
        await channel.send('--------------------3段階目--------------------')

    if message.content == '/4段階目':
        channel = client.get_channel(ID_CHANNEL_1)
        await channel.send('--------------------4段階目--------------------')
    
    if message.content == '/9月':
        channel = client.get_channel(ID_CHANNEL_1)
        await channel.send('--------------------9月--------------------') 
        
    # チャンネル2に対するアクション
    if message.content == '/1段階目':
        channel = client.get_channel(ID_CHANNEL_2)
        await channel.send('--------------------1段階目--------------------')

    if message.content == '/2段階目':
        channel = client.get_channel(ID_CHANNEL_2)
        await channel.send('--------------------2段階目--------------------')

    if message.content == '/3段階目':
        channel = client.get_channel(ID_CHANNEL_2)
        await channel.send('--------------------3段階目--------------------')

    if message.content == '/4段階目':
        channel = client.get_channel(ID_CHANNEL_2)
        await channel.send('--------------------4段階目--------------------')     
        
    if message.content == '/9月':
        channel = client.get_channel(ID_CHANNEL_2)
        await channel.send('--------------------9月--------------------') 
        
    # チャンネル3に対するアクション
    if message.content == '/1段階目':
        channel = client.get_channel(ID_CHANNEL_3)
        await channel.send('--------------------1段階目--------------------')

    if message.content == '/2段階目':
        channel = client.get_channel(ID_CHANNEL_3)
        await channel.send('--------------------2段階目--------------------')

    if message.content == '/3段階目':
        channel = client.get_channel(ID_CHANNEL_3)
        await channel.send('--------------------3段階目--------------------')

    if message.content == '/4段階目':
        channel = client.get_channel(ID_CHANNEL_3)
        await channel.send('--------------------4段階目--------------------')
        
    if message.content == '/9月':
        channel = client.get_channel(ID_CHANNEL_3)
        await channel.send('--------------------9月--------------------')   
        
    # チャンネル4に対するアクション
    if message.content == '/1段階目':
        channel = client.get_channel(ID_CHANNEL_4)
        await channel.send('--------------------1段階目--------------------')

    if message.content == '/2段階目':
        channel = client.get_channel(ID_CHANNEL_4)
        await channel.send('--------------------2段階目--------------------')

    if message.content == '/3段階目':
        channel = client.get_channel(ID_CHANNEL_4)
        await channel.send('--------------------3段階目--------------------')

    if message.content == '/4段階目':
        channel = client.get_channel(ID_CHANNEL_4)
        await channel.send('--------------------4段階目--------------------')   
        
    if message.content == '/9月':
        channel = client.get_channel(ID_CHANNEL_4)
        await channel.send('--------------------9月--------------------') 
    
    # チャンネル5に対するアクション
    if message.content == '/1段階目':
        channel = client.get_channel(ID_CHANNEL_5)
        await channel.send('--------------------1段階目--------------------')

    if message.content == '/2段階目':
        channel = client.get_channel(ID_CHANNEL_5)
        await channel.send('--------------------2段階目--------------------')

    if message.content == '/3段階目':
        channel = client.get_channel(ID_CHANNEL_5)
        await channel.send('--------------------3段階目--------------------')

    if message.content == '/4段階目':
        channel = client.get_channel(ID_CHANNEL_5)
        await channel.send('--------------------4段階目--------------------')   
 
    if message.content == '/9月':
        channel = client.get_channel(ID_CHANNEL_5)
        await channel.send('--------------------9月--------------------') 
        
    # チャンネル6に対するアクション
    if message.content == '/1段階目':
        channel = client.get_channel(ID_CHANNEL_6)
        await channel.send('--------------------1段階目--------------------')

    if message.content == '/2段階目':
        channel = client.get_channel(ID_CHANNEL_6)
        await channel.send('--------------------2段階目--------------------')

    if message.content == '/3段階目':
        channel = client.get_channel(ID_CHANNEL_6)
        await channel.send('--------------------3段階目--------------------')

    if message.content == '/4段階目':
        channel = client.get_channel(ID_CHANNEL_6)
        await channel.send('--------------------4段階目--------------------')   
        
    if message.content == '/9月':
        channel = client.get_channel(ID_CHANNEL_6)
        await channel.send('--------------------9月--------------------') 
        
    # チャンネル7に対するアクション
    if message.content == '/1段階目':
        channel = client.get_channel(ID_CHANNEL_7)
        await channel.send('--------------------1段階目--------------------')

    if message.content == '/2段階目':
        channel = client.get_channel(ID_CHANNEL_7)
        await channel.send('--------------------2段階目--------------------')

    if message.content == '/3段階目':
        channel = client.get_channel(ID_CHANNEL_7)
        await channel.send('--------------------3段階目--------------------')

    if message.content == '/4段階目':
        channel = client.get_channel(ID_CHANNEL_7)
        await channel.send('--------------------4段階目--------------------')
        
    if message.content == '/9月':
        channel = client.get_channel(ID_CHANNEL_7)
        await channel.send('--------------------9月--------------------') 
        
    # チャンネル8に対するアクション
    if message.content == '/1段階目':
        channel = client.get_channel(ID_CHANNEL_8)
        await channel.send('--------------------1段階目--------------------')

    if message.content == '/2段階目':
        channel = client.get_channel(ID_CHANNEL_8)
        await channel.send('--------------------2段階目--------------------')

    if message.content == '/3段階目':
        channel = client.get_channel(ID_CHANNEL_8)
        await channel.send('--------------------3段階目--------------------')

    if message.content == '/4段階目':
        channel = client.get_channel(ID_CHANNEL_8)
        await channel.send('--------------------4段階目--------------------')     
        
    if message.content == '/9月':
        channel = client.get_channel(ID_CHANNEL_8)
        await channel.send('--------------------9月--------------------')    

    # チャンネル9に対するアクション
    if message.content == '/1段階目':
        channel = client.get_channel(ID_CHANNEL_9)
        await channel.send('--------------------1段階目--------------------')

    if message.content == '/2段階目':
        channel = client.get_channel(ID_CHANNEL_9)
        await channel.send('--------------------2段階目--------------------')

    if message.content == '/3段階目':
        channel = client.get_channel(ID_CHANNEL_9)
        await channel.send('--------------------3段階目--------------------')

    if message.content == '/4段階目':
        channel = client.get_channel(ID_CHANNEL_9)
        await channel.send('--------------------4段階目--------------------')
        
    if message.content == '/9月':
        channel = client.get_channel(ID_CHANNEL_9)
        await channel.send('--------------------9月--------------------') 
 
    # チャンネル10に対するアクション
    if message.content == '/1段階目':
        channel = client.get_channel(ID_CHANNEL_10)
        await channel.send('--------------------1段階目--------------------')

    if message.content == '/2段階目':
        channel = client.get_channel(ID_CHANNEL_10)
        await channel.send('--------------------2段階目--------------------')

    if message.content == '/3段階目':
        channel = client.get_channel(ID_CHANNEL_10)
        await channel.send('--------------------3段階目--------------------')

    if message.content == '/4段階目':
        channel = client.get_channel(ID_CHANNEL_10)
        await channel.send('--------------------4段階目--------------------') 
        
    if message.content == '/9月':
        channel = client.get_channel(ID_CHANNEL_10)
        await channel.send('--------------------9月--------------------') 

        
    if message.content == "/kurabatotest":
        channel = client.get_channel(CHANNEL_ID2)
        msg = await channel.send('------------------------------------------------------------ \n 日付が変わりました！今日も頑張りましょう♡') 
    
        msg = await channel.send('今日の凸状況')
        await msg.add_reaction(ID_totu1)
        await msg.add_reaction(ID_totu2)
        await msg.add_reaction(ID_totu3)
        
        msg = await channel.send('今日のタスクキル')
        await msg.add_reaction(ID_tk)
   
#@client.event
async def on_raw_reaction_add(payload):
    # author: リアクションがついたメッセージを書いた人
    channel = client.get_channel(payload.channel_id)
    message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    if channel.id == ID_Mana:
        guild = client.get_guild(payload.guild_id)  
        member = guild.get_member(payload.user_id)    
        user = client.get_user(payload.user_id)
                
        if user.bot:
            return
        else:
            text = member.name + 'さんが記入しました♡'  

            
    if channel.id == ID_taskkill:
        guild = client.get_guild(payload.guild_id)  
        member = guild.get_member(payload.user_id)    
        user = client.get_user(payload.user_id)
        

        if user.bot:
            return
        else:
            text = member.name + 'さんがタスクキルをしました♡'  
            
@client.event
async def on_reaction_add(self, reaction, user):
    if channel.id == ID_CHANNEL_ZANGE:
        if payload.emoji.name == '\N{GRINNING FACE}':
            text = "父と子とゴデチアのみ名によって、" + message.author.name + "の罪をゆるします。アーメン。安心して行きなさい"
    await channel.send(text)
    
# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '05:00':
        #ランドソル杯データ入力
        #channel = client.get_channel(CHANNEL_ID)
        #msg = await channel.send('日付が変わりました！記入が終わったらリアクションを付けてね♡ \n https://docs.google.com/spreadsheets/d/1nCdtFHS-60WcRZDx8hTXHFm3mPuEqefntQxeRfM2Lv0/edit#gid=632518118')  
        #await msg.add_reaction(ID_emoji) 

        #凸、タスクキル管理
        channel = client.get_channel(CHANNEL_ID2)
        msg = await channel.send('------------------------------------------------------------ \n 日付が変わりました！今日も頑張りましょう♡') 
    
        msg = await channel.send('今日の凸状況')
        await msg.add_reaction(:one:)
        await msg.add_reaction(:two:)
        await msg.add_reaction(:three:)
        
        msg = await channel.send('今日のタスクキル')
        await msg.add_reaction(ID_tk)
        
#ループ処理実行
loop.start()    

client.run(token)
