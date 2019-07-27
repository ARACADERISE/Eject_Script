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

# Implementing into the client.json what signals it will now recieve
now_recieve = open('client.json','w')
recieve_from = {'RECIEVING_REQUESTS_FROM_SIGNAL_TYPES':['cco','bo1','a01','ct4','phh','http','https','rgbyt','loi']}
recieving_from = json.dumps(recieve_from,indent=2,sort_keys=True)
now_recieve.write(recieving_from)
now_recieve.close()

# THIS WILL HOPEFULLY BE THE RENDER TEMPLATE TO BE USED IN EVERY OTHER FILE
# WRITING TO client.json
class data_to_send_through_file:
  def __init__(self,port):
    self.port = port
    self.send_req = ""
    self.get_req = ""
    self.store_req = ""
    self.appended_file = ""
    self.signal = ""
  
  # THIS WILL ONLY USE ONE TYPE OF SIGNAL, SO WE HARD CODED WHAT SIGNAL IT'S USING
  def __requests_to_file__(self,file_being_appended):
    self.appeneded_file = file_being_appended
    # Hard coded signal
    # Usually it will be assigned to the functions argument but if the user
    # decides to make another file(for whatever benifit) we need to make sure they don't have to type in the signal to
    # create a new files connection to and with client.json
    self.signal = 'cco'
                   
    OPEN_CLIENT_FILE_READ = open('client.json','r')
    OPEN_CLIENT_FILE_WRITE = open('client.json','w')
                   
    if self.signal in signal_types:
      self.send_req = self.signal
                   
      if signal_type[0] in OPEN_CLIENT_FILE_READ.read() and self.send_req == signal_types[0]:
        send_data = {'new_connection_status': ['requestsGET','requestSEND','requestSTORE'], 'file_appended_to_connection_requests': self.appended_file}
        data_to_send = json.dumps(send_data,indent=2,sort_keys=True)
        OPEN_CLIENT_FILE_WRITE.write(data_to_send)
        OPEN_CLIENT_FILE_WRITE.close()
        
if os.path.exists('/data/data/com.termux/files/home/sLang/client.json'):
  # ORIGINAL STATUS TO client.json
  # WILL BE UPDATED
  GET_CONNECTION = open('client.json','w')
  # Since this file is the file that will always write into client.json this is going to be the original client.json
  # connection
  send_data = {'OFFICIAL_CONNECTION':file_being_connected}
  data = json.dumps(send_data,indent=2,sort_keys=True)
  GET_CONNECTION.write(data)
  GET_CONNECTION.close()
if not os.path.exists('/data/data/com.termux/files/home/sLang/client.json'):
  raise Exception('Cannot connect to client.json')
