import os,sys,json,time
from use_client.original_client_connection import data_to_send_through_file

# simple easy script to create a client for the user
# will be used to most likely help read and format the .ss file
# I do not know though

NAME = 'user-cli'
CREATE_CLIENT = f'a01\\{NAME}-|-{os.name}.{sys.platform}[{os.getgid()}--.{os.getegid()}]|noll_nom_om/|\='
TOTAL_BYTES = 5000
PATH = '/data/data/com.termux/files/home'
DATABASE_SIGNAL_CONNECTIONS = ['cco','bo1','a01','ct4','phh','http','https','default']
CLIENT = []
try:
  # this will "run" the client for a bootup
  class runClientWithRuntime_timer:
    
    # countdown False by default
    def __init__(self, client_name, bootup_time, countdown=bool(False), client_being_started=[object], has_exited=bool):
      self.bootup = bootup_time
      self.set_port = '18080'
      self.countdown = bool(countdown)
      self.start_client = [client_being_started]
      self.has_exited= bool(has_exited)
      self.client_name = client_name
      
    def end(self):

      # have to hard code this due to the fact
      # there is no other way to change the value
      self.has_exited = True

      if self.bootup > 0 and self.has_exited == True:
        self.countdown=False
        self.bootup = 0
        return f'{self.client_name} passed with exit status',1078
      
      if self.bootup < 0 and self.has_exited == True:
        raise OverflowError("Error. The client went over available bytes of data")
        return "Exit success, client fail @ over-draw-of-bye-data with exit status",1078
      
    def start(self):
      if self.bootup == self.bootup:
        if self.countdown == True:
          while self.bootup > 0 and self.countdown and not self.has_exited:

            # Client Buffer(NOT THE RUNTIME)
            time.sleep(0.06)
            self.bootup = self.bootup - 10

            if self.bootup == 0:
              break
            
            if self.bootup < 0:
              raise RuntimeError('Runtime of client ran out. Runtime error @ line ')
              return "Program crash at runtimeerror with exit status",1078

            # if it is still greater than 2 we will pass
            else:
              pass
      get_requests = data_to_send_through_file(self.set_port)
      get_requests.__requests_to_file__('client_server/create_client_for_platform_name.py')
  def _set_user_client(client,bootup):
    set_client = (CREATE_CLIENT)

    client_ = runClientWithRuntime_timer(client,bootup,countdown=True,client_being_started=[client],has_exited=False)
    
    # Runtime will be over 1400
    if not bootup > TOTAL_BYTES:
      CLIENT.append(['CLIENT_SETUP_STARTED'])
      client_.start()
      CLIENT.append([{'USER_CLIENT':client,'port_open_to_signals':DATABASE_SIGNAL_CONNECTIONS}])
      client_.end()
      CLIENT.append(['CLIENT_SETUP_ENDED'])
      return client

    if bootup > TOTAL_BYTES:
      raise OverflowError('Error: Client got too long. Byte overflow error')
    
  CLIENT_BOOTUP = len(CREATE_CLIENT)*38
  bootup_timer = CLIENT_BOOTUP
  _set_user_client(CREATE_CLIENT,bootup_timer)
finally:
  # For the fact that the .json file stores very simple data that doesn't change
  # we will make it to where it uploades once
  if not os.path.exists(f'{PATH}'):
    prev = f'{PATH}/slang'
    if not os.path.exists(f'{prev}/client.json'):
      def json_data(dumping):
        with open('client.json','w') as c_j:
          json.dump(dumping,c_j,indent=2,sort_keys=True)
        return "Status upgrade with info in json files with exit status",1078
      json_data(CLIENT)
  if os.path.exists(f'{PATH}'):
    prev = f'{PATH}/sLang'
    if os.path.exists(f'{prev}/client.json'):
      pass
