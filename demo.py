# coding: utf-8
import json
import requests
import pprint

# key = 'tLdYoFGg7SFPC1LKRxDO8DQqyC5amuBi'
key = 'IwKTtP7vQ5Mahn5dykDACKqKdzFUY2uT'
city = '北京'
url = 'http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak={}'.format(city, key)
# url = 'http://api.map.baidu.com/telematics/v2/search?q={}&region={}&output=json&ak={}'.format('饭店', city, key)
App_secret = '7a9676bb8ceea89685eaeb9ec4c7fb4b'
AppID = 'wx92a5fb372a254be2'

print(url)
response = requests.get(url)
weather_dict = response.json()
# pprint.pprint(weather_dict)
print(weather_dict['results'][0]['currentCity'])
weather_data = weather_dict['results'][0]['weather_data']
print weather_data
for item in weather_data:
    print(item['date'])
    print(item['weather'])
    print(item['wind'])
    print(item['temperature'])
