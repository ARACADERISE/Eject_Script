import os,sys,json,time

# simple easy script to create a client for the user
# will be used to most likely help read and format the .ss file
# I do not know though

NAME = 'user-cli'
CREATE_CLIENT = f'a01\\{NAME}-|-{os.name}.{sys.platform}[{os.getgid()}--.{os.getegid()}]|noll_nom_om/|\='
TOTAL_BYTES = 5000
CLIENT = []
try:
  # this will "run" the client for a runtime
  class runClientWithRuntime_timer:
    
    # countdown False by default
    def __init__(self, client_name, runtime, countdown=bool(False), client_being_started=[object], has_exited=bool):
      self.runtime = TOTAL_BYTES
      self.countdown = bool(countdown)
      self.start_client = [client_being_started]
      self.has_exited= bool(has_exited)
      self.client_name = client_name
      
    def end(self):

      # have to hard code this due to the fact
      # there is no other way to change the value
      self.has_exited = True

      if self.runtime > 0 and self.has_exited == True:
        self.countdown=False
        self.runtime = 0
        print('Success')
        return f'{self.client_name} passed with exit status',1078
      
      if self.runtime < 0 and self.has_exited == True:
        raise OverflowError("Error. The client went over available bytes of data")
        return "Exit success, client fail @ over-draw-of-bye-data with exit status",1078
      
    def start(self):
      if self.runtime == self.runtime:
        if self.countdown == True:
          while self.runtime > 0 and self.countdown and not self.has_exited:

            # Client Buffer(NOT THE RUNTIME)
            time.sleep(0.06)
            print(self.runtime)
            self.runtime = self.runtime - 50

            if self.runtime < 200:
              break
            
            if self.runtime < 0:
              raise RuntimeError('Runtime of client ran out. Runtime error @ line ')
              return "Program crash at runtimeerror with exit status",1078
            
            if self.runtime == 0:
              self.runtime = TOTAL_BYTES / 6 * 3

            # if it is still greater than 2 we will pass
            else:
              pass

  def _set_user_client(client,runtime):
    # Runtime will be over 1400
    set_client = (CREATE_CLIENT)
    client_ = runClientWithRuntime_timer(client,runtime,countdown=True,client_being_started=[client],has_exited=False)
    if not len(client) > TOTAL_BYTES:
      CLIENT.append(['CLIENT_SETUP_STARTED'])
      client_.start()
      CLIENT.append([{'USER_CLIENT':client}])
      client_.end()
      CLIENT.append(['CLIENT_SETUP_ENDED'])
      return client
    if len(client) > TOTAL_BYTES:
      raise OverflowError('Error: Client got too long. Byte overflow error')
    
  CLIENT_RUNTIME = len(CREATE_CLIENT)*38
  runtime_timer = CLIENT_RUNTIME
  _set_user_client(CREATE_CLIENT,runtime_timer)
finally:
  def json_data(dumping):
    with open('client.json','w') as c_j:
      json.dump(dumping,c_j,indent=2,sort_keys=True)
    return "Status upgrade with info in json files with exit status",1078
  json_data(CLIENT)
