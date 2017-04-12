# coding:utf-8
import itchat
import json
import pprint
import requests
import time
import os
from itchat.content import *


# @itchat.msg_register
# def simple_reply(msg):
#     if msg['Type'] == TEXT :
#     # if msg['Type'] == TEXT and msg['Content'] == 'weather':
#         # send_weather()
#         return 'I received: %s' % msg['Content']


def print_ts(message):
    print("[%s] %s"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), message))


def get_weather(city):
    key = 'IwKTtP7vQ5Mahn5dykDACKqKdzFUY2uT'
    # city = '北京'
    city = city
    url = 'http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak={}'.format(city, key)
    # url = 'http://api.map.baidu.com/telematics/v2/search?q={}&region={}&output=json&ak={}'.format('饭店', city, key)
    App_secret = '7a9676bb8ceea89685eaeb9ec4c7fb4b'
    AppID = 'wx92a5fb372a254be2'

    # print(url)
    response = requests.get(url)
    weather_dict = response.json()
    # pprint.pprint(weather_dict)
    print(weather_dict['results'][0]['currentCity'])
    weather_data = weather_dict['results'][0]['weather_data']
    return weather_data
    # data1 = {}
    # data1['date'] =weather_data[0]['date']
    # data1['weather'] = weather_data[0]['weather']
    # data1['wind'] = weather_data[0]['wind']
    # data1['temperature'] = weather_data[0]['temperature']
    # print data
    # return data

    # for item in weather_data:
    #     print(item['date'])
    #     print(item['weather'])
    #     print(item['wind'])
    #     print(item['temperature'])
    # return weather_data


def send_weather():

    # itchat.auto_login()

    friends = itchat.search_friends(name='R.D.I')
    # friends = itchat.search_friends(name='sxw2251')

    username = friends[0]['UserName']
    print(username)
    weather_data = get_weather('北京')

    itchat.send('Hello, ' + u'我是机器人超，现在开始播报天气', toUserName=username)
    time.sleep(3)
    itchat.send(u'您所处的位置：【北京】', toUserName=username)
    time.sleep(3)
    itchat.send(u'今天的日期：' + weather_data[0]['date'], toUserName=username)
    time.sleep(3)
    itchat.send(u'今天的天气：' + weather_data[0]['weather'], toUserName=username)
    time.sleep(3)
    itchat.send(u'今天的风力：' + weather_data[0]['wind'], toUserName=username)
    time.sleep(3)
    itchat.send(u'今天的温度：' + weather_data[0]['temperature'], toUserName=username)
    time.sleep(3)
    itchat.send(u'接下来播报未来三天的天气：', toUserName=username)
    for index, item in enumerate(weather_data):
        if index == 0:
            continue
        itchat.send(u'日期：【' + item['date'] + u'】', toUserName=username)
        time.sleep(1)
        itchat.send(u'天气：' + item['weather'], toUserName=username)
        time.sleep(1)
        itchat.send(u'风力：' + item['wind'], toUserName=username)
        time.sleep(1)
        itchat.send(u'温度：' + item['temperature'], toUserName=username)
        time.sleep(3)
    itchat.send(u'播报完毕，祝您生活愉快!', toUserName=username)


def run(interval):
    # print_ts("-"*100)
    # print_ts("Command %s"%command)
    # print_ts("Starting every %s seconds."%interval)
    # print_ts("-"*100)
    while True:
        try:
            # sleep for the remaining seconds of interval
            time_remaining = interval-time.time() % interval
            print_ts("Sleeping until %s (%s seconds)..."%((time.ctime(time.time()+time_remaining)), time_remaining))
            time.sleep(time_remaining)
            # print_ts("Starting command.")
            # execute the command
            # status = os.system(command)
            send_weather()
            # print_ts("-"*100)
            # print_ts("Command status = %s."%status)
        except Exception, e:
            print e


# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     if msg['Content'] == 'weather':
#         send_weather()

        # itchat.send(msg['Text'], msg['FromUserName'])


if __name__ == '__main__':
    itchat.auto_login()
    # itchat.run()
    send_weather()
    # interval = 10
    # run(interval)
