#本插件由Airp开发出现任何问题概不负责
from pyrogram import Client
from pagermaid.listener import listener
from pagermaid.utils import Message, client, edit_delete

@listener(command="tian_dog", description="舔狗日记(Airp)")
async def diss(_: Client, message: Message):
    for _ in range(5):
        req = await client.get("https://api.oddfar.com/yl/q.php?c=1006&encode=text")
        if req.status_code == 200:
            return await message.edit(req.text)
    await edit_delete(message, "出错了呜呜呜 ~ 试了好多好多次都无法访问到 API 服务器 。")