#本插件由Airp开发出现任何问题概不负责
from pyrogram import Client
from pagermaid.listener import listener
from pagermaid.utils import Message, client, edit_delete

@listener(command="god", description="啊,哲学")
async def diss(_: Client, message: Message):
    for _ in range(5):
        req = await client.get("https://api.oddfar.com/yl/q.php?c=2011&encode=text")
        if req.status_code == 200:
            return await message.edit(req.text)
    await edit_delete(message, "无法连接至API服务器")