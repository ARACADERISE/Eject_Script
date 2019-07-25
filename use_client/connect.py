# Connection to any json files throughout the project

import json, os

TYPE = 'Connection With Json'

if os.path.exists('/data/data/com.termux/files/home/sLang/client.json'):
  GET_CONNECTION = open('client.json','r')
if not os.path.exists('/data/data/com.termux/files/home/sLang/client.json'):
  raise Exception('Cannot connect to client.json')
