if [ ! -d /data/data/com.termux/files/usr/bin/check ]; then
  sh ./check
  mv -v check /data/data/com.termux/files/usr/bin
  chmod /dat/data/com.termux/files/usr/bin/check
  echo "\n==> Type 'check -file' to check the .ss file. As of right now you are booting into the Python mode\n"
fi

if [ -d /data/data/com.termux/files/usr/bin/check ]; then
  echo "\n==> You already have 'check' rooted to your /bin directry. Type 'check -file', if you haven't booted yourself into the Pythons scripts, to check your .ss file"
fi
