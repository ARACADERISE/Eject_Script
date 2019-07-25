# Setting up the language itself(the reader)

"""
  * This is the startup
  * Nothing big will be in here, yet
"""

import os, json
from colorama import Fore, Style

os.system('bash setup_check.sh')

def reader():
 folder = input(Fore.MAGENTA+'.s File Name(with .s) >> ')
  if '.s' in folder:
    # Will read the file
    open_file = open(folder,r)
    print(open_file.read())
    os.system(f'check -file')
    open_file.close()
  else:
    # If it isn't a .s file we will raise a exception
    raise Exception(f"The file you wanted to open isn't a .s file. {Fore.YELLOW}Aborting..")
reader()
