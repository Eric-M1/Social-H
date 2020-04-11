from huepy import *
from os import system
from sys import exit

def clear():
    system('clear')

def conNot():
    print(bold(red('''

             ____ ____ ____ _ ____ _             __   __ | //
             [__  |  | |    | |__| |       |__| |__| |   |//
             ___] |__| |___ | |  | |___    |  | |  | |__ |\\
              
                    [!] Network error. Verify your connection.\n
''')))
    exit(0)

def phpNot():
    print(red("\n\n[!] PHP installation not found. Please install PHP and run me again. http://www.php.net/ "))
    exit(0)

def pyNot():
    print(red("[!] Please use Python 3. $ python3 SocialFish.py "))

def ngrokNot():
    print(red("[!] Ngrok not found. Downloading it..."))

def head():
    clear()
    print(bold(cyan('''
 - This code has been updated: Eric
 - Instagram: _ph_wallpaper_
 - Version: 3.3.0
 - Social - Hack
 ''')))

def end():
    clear()
    print(cyan(''''''))


def loadModule(module):
    print(bold(red('''
                  [|]
                  [|]
                  [|]
                  [|] 
                  \|/  
                   |
                      \n''')))

    print(bold(cyan(''' [*] %s Module loaded. Building site...'''  % module)))
def checkEd():

    if input(bold(green(' [!] Do you agree to use this tool for educational purposes only [Y/N] > '))).upper() != 'Y':
        clear()
        print(red('\n\n'))
        exit(0)

def checkmail():

    from core.email import smtp_provider, connect_smtp
    from getpass import getpass
    from smtplib import SMTP

    if input(bold(green(' [+] Please confirm user [Y] > '))).upper() == 'n':
        
        login = input(cyan(' [+] Enter your email > '))

        try:
            provider = login.split('@')[1].split('.')[0]
        except (IndexError, ValueError):
            print(red(' [!] This domain is not supported!'))
            return	
	
        if provider.lower() == 'gmail':
            print(yellow(' [!] Before access please enable less secure apps\n --> [https://myaccount.google.com/lesssecureapps]'))

        passwd = getpass(cyan(' [+] Password > '))
      
        domain, port = smtp_provider(provider)

        connect_smtp(domain, port, login, passwd)
        
