# インストールした discord.py を読み込む
import discord
import asyncio
import os

CHANNEL_ID = 673477447785644042 #チャンネルID
token = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「!１段階目」と発言したら「一段階目」が返る処理
    if message.content == '!1段階目':
        channel = client.get_channel(CHANNEL_ID)
        await message.channel.send('----------1段階目----------')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
