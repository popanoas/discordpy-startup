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
#鯖チャンネルID
#ID_CHANNEL_1 = 670294227846037514
ID_CHANNEL_ZANGE = 741739653245173800
ID_taskkill = 731046340674453567
ID_Mana = 730136347477540908
#ロールID
ID_role_1 = 767199879641694268
ID_role_2 = 767200011749949470
ID_role_3 = 767200106557865985
ID_role_tk = 767200196827676683
#鯖専用絵文字
ID_emoji = '<:61ok:728923368870510605>'
ID_tk = '<:syarururage:737890640519495712>'
ID_emoji_zange = '<:61ok:728923368870510605>'
ID_1 = '<:59na:726842370116812850>'
ID_2 = '<:58no:726842380673876091>'
ID_3 = '<:57ra:726842390949789696>'
token = os.environ['DISCORD_BOT_TOKEN']
# 接続に必要なオブジェクトを生成
client = discord.Client()
# メッセージ受信時に動作する処理
#@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
        
    # チャンネル1に対するアクション
    if message.content == '/1段階目':
        channel = client.get_channel(ID_CHANNEL_1)
        await channel.send('--------------------1段階目--------------------')
          
    
# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '05:00':
        #ランドソル杯データ入力
        #channel = client.get_channel(ID_Mana)
        #msg = await channel.send('日付が変わりました！記入が終わったらリアクションを付けてね♡ \n https://docs.google.com/spreadsheets/d/1nCdtFHS-60WcRZDx8hTXHFm3mPuEqefntQxeRfM2Lv0/edit#gid=632518118')  
        #await msg.add_reaction(ID_emoji) 
        #凸、タスクキル管理
        channel = client.get_channel(ID_taskkill)
        msg = await channel.send('------------------------------------------------------------ \n 日付が変わりました！今日も頑張りましょう♡') 
    
        msg = await channel.send('今日の凸状況')
        await msg.add_reaction(ID_1)
        await msg.add_reaction(ID_2)
        await msg.add_reaction(ID_3)
        
        msg = await channel.send('今日のタスクキル')
        await msg.add_reaction(ID_tk)
        
#ループ処理実行
loop.start()    
#@client.event
#async def on_raw_reaction_add(payload):
    # author: リアクションがついたメッセージを書いた人
    #channel = client.get_channel(payload.channel_id)
    #message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    #if channel.id == ID_Mana:
        #guild = client.get_guild(payload.guild_id)  
        #member = guild.get_member(payload.user_id)    
        #user = client.get_user(payload.user_id)                
        #if user.bot:
            #return
        #else:
            #text = member.name + 'さんが記入しました♡'  
            
    #if channel.id == ID_taskkill:
        #guild = client.get_guild(payload.guild_id)  
        #member = guild.get_member(payload.user_id)    
        #user = client.get_user(payload.user_id)        
        #if user.bot:
            #return
        #else:
            #text = member.name + 'さんが入力しました♡' 
            
@client.event
async def on_reaction_add(self, reaction, user):
    if channel.id == ID_CHANNEL_ZANGE:
        if payload.emoji.name == '\N{GRINNING FACE}':
            text = "父と子とゴデチアのみ名によって、" + message.author.name + "の罪をゆるします。アーメン。安心して行きなさい"
    await channel.send(text)
@client.event  
async def on_raw_reaction_add(payload):  
    channel = client.get_channel(payload.channel_id)  
    if channel.id == ID_taskkill:
        if payload.emoji.name == '\N{GRINNING FACE}':
            guild = client.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id)  
            role = guild.get_role(ID_role_1)  
            await member.add_roles(role)  


client.run(token)
