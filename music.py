# coding:utf-8
import os
import itchat
from NetEaseMusicApi import interact_select_song

with open('stop.mp3', 'w') as f: pass

HELP_MSG = u'''
欢迎使用微信网易云音乐
帮助：显示帮助
关闭：关闭歌曲
歌名：按照引导播放音乐
'''
def close_music():
    os.startfile('stop.mp3')


@itchat.msg_register(itchat.content.TEXT)
def music_player(msg):
    if msg['ToUserName'] != 'filehelper': return
    if msg['Text'] == u'关闭':
        # close_music()
        itchat.send(u'音乐已关闭', 'filehelper')
        os._exit(0)
    if msg['Text'] == u'帮助':
        itchat.send(u'帮助信息', 'filehelper')
    else:
        itchat.send(interact_select_song(msg['Text']), 'filehelper')

itchat.auto_login(True)
itchat.send(HELP_MSG, 'filehelper')
itchat.run()