# coding:utf-8
import os
import requests
import pprint


def search_place(hot_place="旅游", city="北京"):
    url = 'http://api.map.baidu.com/place/v2/search?q={}&region={}&output=json&ak={}'.format(hot_place, city, key)
    response = requests.get(url)
    place_dict = response.json()
    return place_dict['results']


key = 'IwKTtP7vQ5Mahn5dykDACKqKdzFUY2uT'
place_dict = search_place(hot_place='美食')
print('Total: {}'.format(len(place_dict)))
for index, item in enumerate(place_dict):
    pprint.pprint(index + 1)
    pprint.pprint(item['name'])
    if 'address' in item:
        pprint.pprint(item['address'])
    else:
        pprint.pprint('Address None')
    if 'telephone' in item:
        pprint.pprint(item['telephone'])
    else:
        pprint.pprint('Telephone None')
# pprint.pprint(place_dict)