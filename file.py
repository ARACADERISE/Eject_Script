"""
  "Putting .txt, .db and .sql files to use"
  * ROOT BASED: /data/data/com.termux/files/usr/bin
"""

import os

if os.path.exists('/data/data/com.termux/files/usr/bin/Eject_Script')
  from time import sleep

  # CHECKS FOR CERTAIN ASSIGNMENTS IN database.env
  if not 'main_file=file.py' in open('database.env','r').read():
    raise Exception('main_file=file.py::corrupted')
  if not 'cache_file=CACHE.txt' in open('database.env','r').read():
    raise Exception('cache_file=CACHE.txt::corrupted')
  if not 'connection_file=connection.txt' in open('database.env','r').read():
    raise Exception('connection_file=connection.txt::corrupted')
  if not 'eject_file=eject_type_info.txt' in open('database.env','r').read():
    raise Exception('eject_file=eject_type_info.txt::corrupted')
  if not 'start_file=start_engine.py' in open('database.env','r').read():
    raise Exception('start_file=start_engine.py::corrupted')
  if not 'eject_py_script=begin_eject.py' in open('database.env','r').read():
    raise Exception('eject_py_script=begin_eject.py::corrupted')

  if '18080' in open('database.env','r').read() and 'start_by=engine' in open('database.env','r').read():
    from start_engine import starter
    # from begin_eject import ejector

    # Establish connection
    start = starter('connection.txt','18080','sql')
    start.getConnection(start_connection=True)

    # Start cache process
    start.startCaching()

    # Ejection process
    start.startEjecting();
  else:
    sleep(4)

    raise Exception('connection port 18080 and start_by=engine not found in database.env')
else:
  raise Exception('Eject_Script is not rooted to /usr/bin. Please run the command "bash setup_eject.sh" to root Eject_script")
