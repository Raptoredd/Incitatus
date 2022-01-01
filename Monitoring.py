# Initialization :
import os

# Functions :
def clear():
    if ops=='Linux':
        os.system('clear')
    elif ops=='Windows':
        os.system('cls')
    else:
        os.system('clear')

# First launch detection :
file=open("launch.txt",'r')
libs=['platform','random']

# .Txt file analyse :
for ligne in file:
    rt=0
    while rt==0:
        # First launch :
        if ligne=='1':
            print('')
            print('_  _ ____ _  _ _ ___ ____ ____ _ _  _ ____ ')
            print('|\/| |  | |\ | |  |  |  | |__/ | |\ | | __ ')
            print('|  | |__| | \| |  |  |__| |  \ | | \| |__] ')
            print('')
            print("To work, this script need to install some library's")
            print('')
            print("Here are the list of needed library's to start the script :")
            for i in range (len(libs)):
                print(' --> '+libs[i])
            print('')
            print(' [ 1 ] >> Automatic library installation')
            print(' [ 2 ] >> Manually install')
            print('')
            choice=input(' >> Choose a valid number to continue : ')
            # Automatic install :
            if choice=='1':
                for i in range (len(libs)):
                    os.system('pip install '+libs[i])
                rt=1
                file.write('0')
                file.close()
            # Manual install terminal :
            elif choice=='2':
                print(' - You can install all needed library from this terminal, when you finish enter "return" to start the script')
                rrt=0
                while rrt==0:
                    cmd=input('')
                    if cmdt=='return':
                        rrt=1
                        rt=1
                        file.write('0')
                        file.close()
                    else:
                        os.system(cmdt)
            # Invalid input :
            else:
                none=input(' /!\ Invalid input, press Enter to go back : ')

        # Not first launch :
        else:
            file.close()
            none=''

# Libs import :
import random
import platform

# Os Verification :
ops=platform.system()

# Network adaptater :
controler=['wlan0','wlan1','wlan2']
netadapt=controler[1]

# Commands :
ip_cmd=['ip link set '+netadapt+' down','ip link set '+netadapt+' name '+netadapt+'mon']
airmon_cmd=[]

cmd=ip_cmd
# Functions :
def disp():
    print('')
    print('_  _ ____ _  _ _ ___ ____ ____ _ _  _ ____ ')
    print('|\/| |  | |\ | |  |  |  | |__/ | |\ | | __ ')
    print('|  | |__| | \| |  |  |__| |  \ | | \| |__] ')
    print('')
    print('Welcome to the monitoring mode script')
    print('')
    print(' [ 1 ] >> Execute the script')
    print(' [ 2 ] >> Settings acces')
    print('')

def settings():
    print('')
    print('_  _ ____ _  _ _ ___ ____ ____ _ _  _ ____ ')
    print('|\/| |  | |\ | |  |  |  | |__/ | |\ | | __ ')
    print('|  | |__| | \| |  |  |__| |  \ | | \| |__] ')
    print('')
    print('Settings :')
    print('')
    print(' [ 1 ] Wifi Adapter --> '+netadapt)
    print(' [ 2 ] Operating system --> '+ops)
    print(' [ 3 ] Active commands :')
    for i in range (len(cmd)):
        print('    --> '+cmd[i])
    print('')
    print('')
    print('You can go back to the menu by pressing Enter')
    print('')

# Script :
rt=0
# Goto :
while rt==0:
    # Os validation :
    if ops=='Windows':
        clear()
        disp()
        choice=input(' >> To continue, please choose a number between 1 and 2 : ')
        # Commands start :
        if choice=='1':
            for i in range (len(cmd)):
                print(cmd[i])
        # Settings :
        elif choice=='2':
            clear()
            settings()
            choice=input(' >> You can modify a parameter by entering the value next to him : ')
            if choice=='1':
                print('')
            elif choice=='2':
                print('')
            elif choice=='3':
                print('')
        # Invalid input :
        else :
            clear()
            disp()
            none=input(' /!\ Invalid input, press Enter to go back to the menu : ')
    # Exit :
    else:
        print(' - Hello '+ops+'user. This software has been created for Unix Kernels, press Enter to leave the program : ')
        rt=1
