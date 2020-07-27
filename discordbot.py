# インストールした discord.py を読み込む
import discord
import asyncio
import os

ID_CHANNEL_1 = 670294227846037514  # 1チャンネルID（事前設定用）
ID_CHANNEL_2 = 715596202032496760  # 2チャンネルID（事前設定用）
ID_CHANNEL_3 = 670294262696509469  # 3チャンネルID（事前設定用）
ID_CHANNEL_4 = 715596251927675023  # 4チャンネルID（事前設定用）
ID_CHANNEL_5 = 715596307762380811  # 5チャンネルID（事前設定用）
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
    # 「/2段階目」と発言したら「一段階目」が返る処理
    if message.content == '/2段階目':
        channel = client.get_channel(ID_CHANNEL_2)
        await channel.send('--------------------2段階目--------------------')
    # 「/3段階目」と発言したら「一段階目」が返る処理
    if message.content == '/3段階目':
        channel = client.get_channel(ID_CHANNEL_2)
        await channel.send('--------------------3段階目--------------------')
    # 「/4段階目」と発言したら「一段階目」が返る処理
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
        
# Botの起動とDiscordサーバーへの接続
client.run(token)
