# SINGLE LINE COMMENTS

"""
  * A single line comment #
  * This will also format the color of the comment(white)
"""

def comment(directory,file_name):
  cmd = f"""
  cd
  cd {directory}
  """
  os.system(cmd)
  op = open(file_name,'r')
  if '#' in op.read():
    print('Yes')
  else:
    print('No')
