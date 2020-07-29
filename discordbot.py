# インストールした discord.py を読み込む
import discord
import asyncio
import os
import traceback
import random
from datetime import datetime
from discord.ext import tasks

CHANNEL_ID = 726398497384824853 #毎日朝5時を通知するチャンネルID
ID_CHANNEL_1 = 670294227846037514  # 1チャンネルID（事前設定用）
ID_CHANNEL_2 = 715596202032496760  # 2チャンネルID（事前設定用）
ID_CHANNEL_3 = 670294262696509469  # 3チャンネルID（事前設定用）
ID_CHANNEL_4 = 715596251927675023  # 4チャンネルID（事前設定用）
ID_CHANNEL_5 = 670294289028350012  # 5チャンネルID（事前設定用）
ID_CHANNEL_6 = 715596307762380811  # 6チャンネルID（事前設定用）
ID_CHANNEL_7 = 670294326131032064  # 7チャンネルID（事前設定用）
ID_CHANNEL_8 = 715596648570552341  # 8チャンネルID（事前設定用）
ID_CHANNEL_9 = 670294357944958976  # 9チャンネルID（事前設定用）
ID_CHANNEL_10 = 715596743450034188  # 10チャンネルID（事前設定用）

token = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
     # コマンドを受け取ったときのアクション   
    if message.content == "/1段階目":
        await client.send_message(message.channel, "1段階目に入ります")
        
    if message.content == "/2段階目":
        await client.send_message(message.channel, "2段階目に入ります")     
 
    if message.content == "/3段階目":
        await client.send_message(message.channel, "3段階目に入ります")
 
    if message.content == "/4段階目":
        await client.send_message(message.channel, "4段階目に入ります")
        
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
        
    if message.content == "占い":
#レスポンスされる運勢のリストを作成
        unsei = ["大吉", "中吉", "吉", "末吉", "小吉", "凶", "大凶"]
        choice = random.choice(unsei) #randomモジュールでunseiリストからランダムに一つを選出
        await message.channel.send(choice)

# プレイヤーデータクラス
class PlayerData:
    def __init__(self, user, atk_list, atk_cnt_m, atk_cnt_b, done_cnt, task_killed, req_none, notice_req, req_list,
                 rolled_time, rolled_type, recent_boss):
        self.rolled_time = rolled_time  # 持越時間

# 持ち越しダメージ計算
async def rollover_simulate(message, msg_content):
    current_hp = 0
    expect_dmg = 0
    is_current_hp = False  # 現在のHP判定
    is_expected_dmg = False  # 想定ダメージ判定
    for i in msg_content:
        # ボス番号読み取って該当ボスのフラグを立てる
        if not is_expected_dmg and re.match('\d', i):
            is_current_hp = True
            current_hp = current_hp * 10 + int(i)
        if is_expected_dmg and re.match('\d', i):
            expect_dmg = expect_dmg * 10 + int(i)
        # 現HP読取後の区切り以降は想定ダメージとして読取
        if is_current_hp and not is_expected_dmg and (i == '-' or i == 'ー' or i == '－' or i == ' ' or i == '　'):
            is_expected_dmg = True

    if not expect_dmg:  # 想定ダメージが入力されていない場合、一定秒持越に必要なダメージを出す
        i = 70
        reply = '```持越秒数に対して必要なダメージ一覧\n\n'
        while True:
            suggested_dmg = current_hp / (1 - i / 90)
            reply += f"{i + 20}s：{int(suggested_dmg)} 万ダメージ\n"
            i -= 5
            if i < 0:
                break
        reply += "```"
        await reply_and_delete(message, reply, DELAY_L)
        return
    elif expect_dmg < current_hp:
        reply = "そのダメージだと倒しきれません"
        await reply_and_delete(message, reply, DELAY_S)
        return

    rolled_time = 90 * (1 - current_hp / expect_dmg) + 20
    if rolled_time >= 90:
        rolled_time = 90

    reply = "予想される持越時間は " + str(rolled_time) + "秒です"
    await reply_and_delete(message, reply, DELAY_M)
    return       
        
# Botの起動とDiscordサーバーへの接続
client.run(token)
