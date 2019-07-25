# This Python script file will get the file, then lead into the reading process

"""
  * Will ask user to open a directory
  * Then will ask for the .ss filename
"""

import os, time
from colorama import Fore, Style

os.system('bash setup_check.sh')

def getFile():
  directory = input(Fore.MAGENTA+Style.BRIGHT+"Director(if it's a folder within the directory then type directoryName/folderName) >> "+Fore.WHITE)
  file_name = input(Fore.MAGENTA".ss FileName >> "+Fore.WHITE)
  cmd = f"""
  cd
  cd {directory}
  cat {file_name}
  """
  if '.ss' in file_name:
    # We want a line spacing
    print('\n')
    os.system('echo " ~~~FILE INFORMATION~~~"')
    time.sleep(1)
    os.system('clear')
    os.system(cmd)
    print('\n')
    return "Checking status started",1078
getFile()
