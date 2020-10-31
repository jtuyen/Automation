while true;
do
  ping -c1 www.google.com
  if [ $? -eq 0 ]
  then
	  echo -e "\e[1;32m modem and router is ok \e[0m" | ts '[%Y-%m-%d %H:%M:%S]' >> logs.txt
  else
	  echo -e "\e[1;31m can't ping google.com \e[0m" | ts '[%Y-%m-%d %H:%M:%S]' >> logs.txt
	  echo -e "\e[1;31m rebooting modem and router.. \e[0m" | ts '[%Y-%m-%d %H:%M:%S]' >> logs.txt
	  ( cd ~/Downloads/python-kasa ; poetry shell &>/dev/null ; kasa --host 192.168.18.2 --strip off --name modem ; sleep 30 ; kasa --host 192.168.18.2 --strip on --name modem ; sleep 5m ; kasa --host 192.168.18.2 --strip off --name router ; sleep 30 ; kasa --host 192.168.18.2 --strip on --name router ; exit) | ts '[%Y-%m-%d %H:%M:%S]' >> logs.txt
	  echo -e "\e[1;43m modem and router has been rebooted \e[0m" | ts '[%Y-%m-%d %H:%M:%S]' >> logs.txt
  fi

  ping -c1 192.168.18.5
  if [ $? -eq 0 ]
  then
	  echo -e "\e[1;32m obihai is ok \e[0m" | ts '[%Y-%m-%d %H:%M:%S]' >> logs.txt
	  exit 0
  else
	  echo -e "\e[1;31m rebooting obihai \e[0m" | ts '[%Y-%m-%d %H:%M:%S]' >> logs.txt
	  ( cd ~/Downloads/python-kasa ; poetry shell &>/dev/null ; kasa --host 192.168.18.2 --strip off --name obihai ; sleep 5m ; kasa --host 192.168.18.2 --strip on --name obihai ; exit ) | ts '[%Y-%m-%d %H:%M:%S]' >> logs.txt
	  echo -e "\e[1;43m obihai has been rebooted \e[0m" | ts '[%Y-%m-%d %H:%M:%S]' >> logs.txt
  fi
done
