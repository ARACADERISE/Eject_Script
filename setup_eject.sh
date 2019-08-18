if [ ! -d /data/data/com.termux/files/usr/bin/Eject_Script ]; then
  mv -v Eject_Script /data/data/com.termux/files/usr/bin
  chmod +x /data/data/com.termux/files/usr/bin/Eject_Script
  echo "==> Type: Eject_Script to run the Application!"
  cd
  exit
fi

if [ -d /data/data/com.termux/files/usr/bin/Eject_Script ]; then
  echo "Looks you have already rooted 'Eject_Script' to /usr/bin\nType 'Eject_Script' to run the application"
fi
