get_file()
{
  read -p "Director(NOTE: if it's a folder within the directory then directory/folderName) >> " dir_name
  cd
  cd $dir_name
  ls
  read -p ".s File >> " dot_s_file
  if [ '.s' in $dot_s_file ]
  then
    cat $dot_s_file
  else
    echo "error. not .s file"
  fi
}
get_file
