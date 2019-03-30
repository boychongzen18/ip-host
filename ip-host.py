from socket import gethostbyname

# Tools Priv8 Header Status Website Python 
# Lihat Header Status Website
# Tested : Windows & Termux Working
# Regard Boychongzen aka Xroot


print ('''\033[1m\033[93m[\033[91m!\033[93m] Tools Priv8 IP Host Python \n \033[1;31m 

 /$$$$$$ /$$$$$$$        /$$   /$$                       /$$    
|_  $$_/| $$__  $$      | $$  | $$                      | $$    
  | $$  | $$  \ $$      | $$  | $$  /$$$$$$   /$$$$$$$ /$$$$$$  
  | $$  | $$$$$$$/      | $$$$$$$$ /$$__  $$ /$$_____/|_  $$_/  
  | $$  | $$____/       | $$__  $$| $$  \ $$|  $$$$$$   | $$    
  | $$  | $$            | $$  | $$| $$  | $$ \____  $$  | $$ /$$
 /$$$$$$| $$            | $$  | $$|  $$$$$$/ /$$$$$$$/  |  $$$$/
|______/|__/            |__/  |__/ \______/ |_______/    \___/  \033[1;34mAuthor \033[91m:\033[37m Boychongzen aka Xroot  
 ''')
print"\033[1;31mEksekusi \033[1;34m: \033[1;37m[Windows]python \033[1;31m& \033[1;37m[Termux]python2 \033[1;34mip-host.py"

print ('\033[1;31m----------\033[1;34m( \033[1;33mWELCOME My Tools IP Host \033[1;34m)\033[1;31m----------\033[1;37m\n')

def Miscript():
	print'\a[Welcomback Tools Ip Host]'
	target = raw_input('==> Host Cuks: ')
	targetHost = gethostbyname(target)
	print '\aIP Target Cuks ===>', targetHost
	print '\n+------------------------------------+'
	Miscript()
Miscript()
