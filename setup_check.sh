# Setups check

if [ ! -d /data/data/com.termux/files/usr/bin/check ]; then
  mv -v check /data/data/com.termux/files/usr/bin
  chmod +x /data/data/com.termux/files/usr/bin/check
  echo "==> Type 'check' to enable your .s file"
fi

if [ -d /data/data/com.termux/files/usr/bin/check ]; then
  echo "You already have 'check' rooted to your /bin directory. \n Type 'check' to enable your .s file"
fi
