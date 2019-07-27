# SINGLE LINE COMMENTS

"""
  * A single line comment #
  * This will also format the color of the comment(white)
"""

import os

def comment(directory,file_name):
  cmd = f"""
  cd
  cd {directory}
  """
  
  os.system(cmd)

  op = open(file_name,'r')
  if '#' in op.read():
    print(Fore.WHITE)
    op.close()
    return "Returned with status",1078
    
  else:
   return "No returned status",1078
   op.close()
   
  # RESETTING ALL COLORS
  print(Style.RESET_ALL)
