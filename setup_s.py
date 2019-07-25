# Setting up the language itself(the reader)

"""
  * This is the startup
  * Nothing big will be in here, yet
"""

import os, json
from colorama import Fore, Style

def reader(file_name):
  if '.s' in file_name:
    # Will read the file
    open_file = open(file_name,r)
    print(open_file.read())
    open_file.close()
  else:
    # If it isn't a .s file we will raise a exception
    raise Exception(f"The file you wanted to open isn't a .s file. {Fore.YELLOW}Aborting..")
