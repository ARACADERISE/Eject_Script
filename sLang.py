# Setting up the language itself(the reader)

"""
  * This is the startup
  * Nothing big will be in here, yet
  * .ss : Simple Scripting
"""

import os, json
from colorama import Fore, Style

os.system('bash setup_check.sh')

def reader():
 directory = input(Fore.MAGENTA+'Directry >> '+Fore.WHITE)
 os.system(f'cd && cd {directory}')
 folder = input(Fore.MAGENTA+'.s File Name(with .ss) >> ')
 os.system(f'cat {folder}')
 if '.ss' in folder:
   os.system('check -file')
 else:
   # If it isn't a .s file we will raise a exception
   raise Exception(f"The file you wanted to open isn't a .s file. {Fore.YELLOW}Aborting..")
reader()
