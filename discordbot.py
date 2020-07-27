# インストールした discord.py を読み込む
import discord
import asyncio
import os

CHANNEL_ID = 673477447785644042 673477457550114826 673477466274398208 673477474293645313 673477482317611008 #チャンネルID
token = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/1段階目」と発言したら「一段階目」が返る処理
    if message.content == '/1段階目':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('--------------------1段階目--------------------')
    # 「/2段階目」と発言したら「一段階目」が返る処理
    if message.content == '/2段階目':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('--------------------2段階目--------------------')
    # 「/3段階目」と発言したら「一段階目」が返る処理
    if message.content == '/3段階目':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('--------------------3段階目--------------------')
    # 「/4段階目」と発言したら「一段階目」が返る処理
    if message.content == '/4段階目':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('--------------------4段階目--------------------')
# Botの起動とDiscordサーバーへの接続
client.run(token)
