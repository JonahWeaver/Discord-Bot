import requests
import json

numList = []
userList = []

def retrieve_messages(history):
    j = 0
    for h in history:
        if str(j+1) in h.content:
            if h.author.name in userList:
                numList[userList.index(h.author.name)] = numList[userList.index(h.author.name)]+1
            else:
                userList.append(h.author.name)
                numList.append(1)
            j=j+1

def addCount(message):
    j = sum(numList)
    if str(j+1) in message.content:
            if message.author.name in userList:
                numList[userList.index(message.author.name)] = numList[userList.index(message.author.name)]+1
            else:
                userList.append(message.author.name)
                numList.append(1)
#id = 1087638615783391312
#845993325835452418

