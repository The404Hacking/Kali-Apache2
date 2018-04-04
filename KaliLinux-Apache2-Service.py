#Kali Linux Apache2 Service
#Coded By Hanieh Panahi
#--------------------------
#The404Hacking
#Digital Security ReSearch Group
#T.me/The404Hacking
#-------------------------------
import os
import sys
import platform

def clear():
	linux = 'clear'
	windows = 'cls'
	os.system([linux, windows][os.name == 'nt'])

clear()
if os.name == "nt":
	print (' [!] Please run the script on Linux Machine !')
	quit()
elif os.name != "nt":
	data = ' Hi '+platform.uname()[1]+' !\n'
	data += ' WelCome to Apache2 Script :)\n'
	data += ' ----------------------------\n'
	data += ' Coded By Hanieh Panahi\n'
	data += ' The404Hacking\n'
	data += ' Digital Security ReSearch Group\n'
	data += '\n'
	data += ' Select a Method:\n'
	data += ' [1] Start Apache2\n'
	data += ' [2] Stop Apache2\n'
	data += ' [3] ReStart Apache2\n'
	data += ' [4] Open Localhost\n'
	data += ' [5] Coder [Telegram]\n'
	data += ' [6] The404Hacking\n'
	data += ' [0] Exit\n'
	print data


number = input(" Number~# ")

if number == 1:
	print "\n [***] Please wait ..."
	os.system("service apache2 start")
	print " [I] Apache2 Service has been Started !\n"
	quit()
elif number == 2:
	print '\n [***] Please wait ...'
	os.system("service apache2 stop")
	print " [O] Apache2 Service has been Stoped !\n"
	quit()
elif number == 3:
	print '\n [***] Please wait ...'
	os.system("service apach2 restart")
	print " [R] Apache2 Service has been ReStarted !\n"
	quit()
elif number == 4:
	print "\n [***] Please wait ...\n"
	print " [O] Opening http://127.0.0.1 ...\n"
	os.system("firefox http://127.0.0.1")
	print " Successfully !\n"
	quit()
elif number == 5:
	print '\n Apache2 Script\n Coded By Hanieh Panahi\n\n The404Hacking\n Digital Security ReSearch Group\n'
	os.system("firefox https://T.me/HaniePanahi")
	quit()
elif number == 6:
	print '\n The404Hacking\n Digital Security ReSearch Group\n'
	os.system("firefox https://T.me/The404Hacking")
	quit()
elif number == 0:
	print '\n [+] Good Bye '+platform.uname()[1]+' !\n'	
	quit()
else:
	print "\n [X] Error !\n [!] Select this number: 1, 2, 3, 4, 5, 6 or 0\n"

