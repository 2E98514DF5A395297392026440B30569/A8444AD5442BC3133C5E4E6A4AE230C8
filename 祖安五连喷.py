#本插件由Airp测试性开发概不负责
from pyrogram import Client 
from pagermaid.listener import listener 
from pagermaid.utils import Message, client, edit_delete 
import requests
chat = '-1001125179638'


@listener(command="5xdisss", description="祖安连喷(不良林)")
async def disss(bot: Client, message: Message):
    req = requests.get("https://api.oddfar.com/yl/q.php?c=1009&encode=text").text
    await bot.send_message(chat, req)
    req = requests.get("https://api.oddfar.com/yl/q.php?c=1009&encode=text").text
    await bot.send_message(chat, req)
    req = requests.get("https://api.oddfar.com/yl/q.php?c=1009&encode=text").text
    await bot.send_message(chat, req)
    req = requests.get("https://api.oddfar.com/yl/q.php?c=1009&encode=text").text
    await bot.send_message(chat, req)
    req = requests.get("https://api.oddfar.com/yl/q.php?c=1009&encode=text").text
    await bot.send_message(chat, req)
