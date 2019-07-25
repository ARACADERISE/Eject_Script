# This Python script file will get the file, then lead into the reading process

"""
  * Will ask user to open a directory
  * Then will ask for the .ss filename
"""

def getFile():
  directory = input("Director(if it's a folder within the directory then type directoryName/folderName) >> ")
  file_name = input(".ss FileName >> ")
  cmd = f"""
  cd
  cd {directory}
  cat {file_name}
  """
  if '.ss' in file_name:
    os.system(cmd)
    return "Checking status started",1078
getFile()
