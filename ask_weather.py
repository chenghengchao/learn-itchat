# coding:utf-8
import itchat
import json
import pprint

itchat.auto_login()

# itchat.send('Hello, filehelper', toUserName='filehelper')
friends = itchat.search_friends(name='butterfly')
print type(friends)
# friends = json.dumps(friends)
pprint.pprint(friends)
print type(friends)
username = friends[0]['UserName']
print username
itchat.send('Hello,' + username, toUserName=username)
