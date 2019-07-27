# Connection to any json files throughout the project

import json, os

TYPE = 'Connection With Json'
file_being_connected = 'connect.py'
signal_types = [
  # bo1: To send but not receive
  "bo1",
  # a01: To recieve from a previous request but not send
  # Exampled: If I were to use ct4, it would just send a signal request. But what if I want to recieve the data?
  # Use a01 and the connection name
  # Example: useConnection(a01,for_con="CONNECTION_01")
  "a01",
  # ct4: To send a signal request to the port
  "ct4",
  # phh: To start a mini-port with a signal of phh for the client to adapt to
  "phh",
  # http: Will excpect a http request signal(a website link)
  "http",
  # https: Will excpect a https request signal(a website link)
  "https",
  # rgbyt: Sends mini bytes to port to support client when both recieving, getting, pulling, and storing request
  "rgbyt",
  # loi: a lazy way of of telling the client to ignore a specific get request
  "loi"
]

# THIS WILL HOPEFULLY BE THE RENDER TEMPLATE TO BE USED IN EVERY OTHER FILE
# WRITING TO client.json
class data_to_send_through_file:
  def __init__(self,signal,connection_name,connection_file,send_Req,get_Req,pull_Req,recieve_Req):
    self.con_name = connection_name
    self.con_file = connection_file
    self.signal = signal
    self.send_req = send_Req
    self.get_req = get_Req
    self.pull_req = pull_Req
    self.rec_req = recieve_Req
  def __requests_to_file__(self):
    OPEN_CLIENT_FILE = open('client.json','w')
    if self.signal in signal_types:
      

if os.path.exists('/data/data/com.termux/files/home/sLang/client.json'):
  # ORIGINAL STATUS TO client.json
  # WILL BE UPDATED
  GET_CONNECTION = open('client.json','w')
  send_data = {'CONNECTION_01':file_being_connected}
  data = json.dumps(send_data,indent=2,sort_keys=True)
  GET_CONNECTION.write(data)
  GET_CONNECTION.close()
if not os.path.exists('/data/data/com.termux/files/home/sLang/client.json'):
  raise Exception('Cannot connect to client.json')
