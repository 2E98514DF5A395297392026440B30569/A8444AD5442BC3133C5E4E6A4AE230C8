# 本插件由Airp开发出现任何问题概不负责
import http.client
import json
import urllib

from pagermaid.listener import listener
from pagermaid.utils import Message, client, edit_delete
from pyrogram import Client

conn = http.client.HTTPSConnection('apis.tianapi.com')  # 接口域名
params = urllib.parse.urlencode({'key': '0a46aa100052d8337341c13268052e19'})
headers = {'Content-type': 'application/x-www-form-urlencoded'}
conn.request('POST', '/zhanan/index', params, headers)
tianapi = conn.getresponse()
result = tianapi.read()
data = result.decode('utf-8')
dict_data = json.loads(data)
a = dict_data.get('result')
vlea = a.get('content')


@listener(command="oneman", description="渣男文学")
async def airp(_: Client, message: Message):
    await message.edit(vlea)
