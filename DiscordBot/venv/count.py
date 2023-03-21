import requests
import json

def retrieve_messages(channelid):
    headers = {
        'authorization': 'NTkwNzUyNzU4MTA2NDIzMzAx.GF0zDi.3svbHt-pqyxz80IOxJzFWFt5kyfkllv_77O-xg'
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    jsonn = json.loads(r.text)
    jsonn.reverse()
    i = 0
    for value in jsonn:

        if value['content'].isnumeric() and i+1 == int(value['content']):
            i=i+1
    print(i)
#id = 1087638615783391312
#845993325835452418

