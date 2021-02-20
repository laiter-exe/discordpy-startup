#condig=utf-8

# インストールした discord.py を読み込む
import discord
import random
import time

# 自分のBotのアクセストークンに置き換えてください
TOKEN = "Nzg1MDM2NTM5MDExNzkyOTY2.X8yAQA.9zjKsCXERphNBa7LyuhsS3f6fTg"

# 接続に必要なオブジェクトを生成
client = discord.Client()


# 起動時に動作する処理
@client.event                                            #discordbotのイベント発動に必要なやつとりあえずこれとasyncは関数作るときにとりあえずつけときゃおｋ
async def on_ready():                                 #on_xxxxxxxx      のところでイベント名を指定できる。今回の場合はdiscordbotが起動したとき
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    guild = discord.utils.get(client.guilds, name="laiter_exeのサーバー")                     #このguild（サーバー）を取得しないとチャンネル等にプログラムがかけない
    channel = discord.utils.get(guild.text_channels, name="一般")                              #この行では一般という名前のチャンネルを取得している
#awaitはdiscordにコマンドを実行したいときはとりあえずつけとけ　channel = さっきのやつ send = 送るって意味　この関数を使うとさっき取得したチャンネルにメッセージを送る

#メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    #ヘルプの表示
    if message.content == "/aki help":
        await message.channel.send("""/aki help    でコマンドリストを表示
/aki saikoro   で０～100までの乱数を降ることができます""")
    #乱数
    if message.content == "/aki saikoro":
        random100 = random.randint(0,100)
        await message.channel.send(random100)


    if message.content == "/aki DM" :
        guild = discord.utils.get(client.guilds, name="laiter_exeのサーバー")                   
        channel = discord.utils.get(guild.text_channels, name="一般")
        dm = await message.author.create_dm()                       #DMのメッセージを作る変数
        await dm.send("ぱぁああああああああああああああああ")            #メッセージを送ってきた人に対して指定したメッセージを送るプログラム


        
# Botの起動とDiscordサーバーへの接続（これはdiscordbotの起動に必須です）
client.run(TOKEN)
