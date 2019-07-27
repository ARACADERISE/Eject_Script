# Connection to any json files throughout the project

import json, os

TYPE = 'Connection With Json'
file_being_connected = 'connect.py'
signal_types = [
  # THIS IS ONLY USED ONCES
  # Used to send a request to send signals and data to the client.json file
  "cco",
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

now_recieve = open('client.json'

# THIS WILL HOPEFULLY BE THE RENDER TEMPLATE TO BE USED IN EVERY OTHER FILE
# WRITING TO client.json
class data_to_send_through_file:
  def __init__(self,port):
    self.port = port
    self.send_req = ""
    self.get_req = ""
    self.store_req = ""
    self.appended_file = ""
    self.signal_to_recieve_from = ""
  
  # THIS WILL ONLY USE ONE TYPE OF SIGNAL, SO WE HARD CODED WHAT SIGNAL IT'S USING
  def __requests_to_file__(self,file_being_appended):
    self.appeneded_file = file_being_appended
                   
    OPEN_CLIENT_FILE_READ = open('client.json','r')
    OPEN_CLIENT_FILE_WRITE = open('client.json','w')
                   
    if self.signal in signal_types:
      self.send_req = signal_types[0]
                   
      if signal_type[0] in OPEN_CLIENT_FILE_READ.read() and self.send_req == signal_types[0]:
        send_data = {'new_connection_status': ['requestsGET','requestSEND','requestSTORE'], 'file_appended_to_connection_requests': self.appended_file}
        data_to_send = json.dumps(send_data,indent=2,sort_keys=True)
        OPEN_CLIENT_FILE_WRITE.write(data_to_send)
        OPEN_CLIENT_FILE_WRITE.close()
        
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
