"""
  "Putting .txt, .db and .sql files to use"
"""

from start_engine import starter
# from begin_eject import ejector

# Establish connection
start = starter('connection.txt','18080','sql')
start.getConnection(start_connection=True)

# Start cache process
start.startCaching()

# Ejection process
start.startEjecting();
