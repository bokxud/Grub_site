#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Ne touche this script -_-
#Don't Edit Logo -_-


import requests, httplib, urllib
import socket
from platform import system
import os
import sys, time
import re
import threading
from multiprocessing.dummy import Pool
from colorama import Fore								
from colorama import Style								
from colorama import init												
init(autoreset=True)
fr  =   Fore.RED
fh  =   Fore.RED
fc  =   Fore.CYAN
fo  =   Fore.MAGENTA
fw  =   Fore.WHITE
fy  =   Fore.YELLOW
fbl =   Fore.BLUE
fg  =   Fore.GREEN											
sd  =   Style.DIM
fb  =   Fore.RESET
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT

user = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}

url = "http://www.zone-h.org/archive/notifier="
urll = "http://zone-h.org/archive/published=0"
url2 = "http://www.defacers.org/onhold!"
url4 = "http://www.defacers.org/gold!"
my_cook = {
	"ZHE" : "04a50905b1d7dd2f5e4fe2e72d50fe8f",
	"PHPSESSID" : "30v7olrtj48jkhru4asvf8fb81"
	}


def zonehh():
	print("""
	    |---| Grabb Sites From Zone-h |--|
		\033[91m[1] \033[95mGrabb Sites By Notifier
		\033[91m[2] \033[95mGrabb Sites By Onhold
		""")
	sec = int(raw_input("Choose Section: "))
	if sec == 1:
		notf = raw_input("\033[95mEntre notifier: \033[92m")

		for i in range(1, 51):
			dz = requests.get(url + notf +"/page=" + str(i), cookies=my_cook)
			dzz = dz.content
			print(url + notf +"/page=" + str(i))
			if '<html><body>-<script type="text/javascript"' in dzz:
				print("Change Cookies Please")
				sys.exit()
			elif '<input type="text" name="captcha" value=""><input type="submit">' in dzz:
				print("Entre Captcha In Zone-h From Ur Browser :/")
				sys.exit()	
			else:
				Hunt_urls = re.findall('<td>(.*)\n							</td>', dzz)
				if '/mirror/id/' in dzz:
					for xx in Hunt_urls:
						qqq = xx.replace('...','')
						print '    ['  + '*' + '] ' + qqq.split('/')[0]
						with open( notf + '.txt', 'a') as rr:
							rr.write("http://" + qqq.split('/')[0] + '\n')
				else:
					print("Grabb Sites Completed !!")
					sys.exit()
					
	elif sec == 2:
		print(":* __Grabb Sites By Onhold__ ^_^")
		for qwd in range(1, 51):
			rb = requests.get(urll + "/page=" + str(qwd) , cookies=my_cook)
			dzq = rb.content

			if '<html><body>-<script type="text/javascript"' in dzq:
				print("Change Cookies Plz")
				sys.exit()
				
			elif "captcha" in dzq:
				print("Entre captcha In Your Browser Of Site [zone-h.org]")
			else:
				Hunt_urlss = re.findall('<td>(.*)\n							</td>', dzq)
				for xxx in Hunt_urlss:
					qqqq = xxx.replace('...','')
					print '    ['  + '*' + '] ' + qqqq.split('/')[0]
					with open('onhold_zone.txt', 'a') as rrr:
						rrr.write("http://" + qqqq.split('/')[0] + '\n')
	else:
		print("Fuck You Men")

def defacers():
	print("""
		|---| Grabb Sites From Defacers.org |--|
			\033[91m[1] \033[95mGrabb Sites By Onhold
			\033[91m[2] \033[95mGrabb Sites By Archive
		""")
	sec = int(raw_input("Choose Section: "))
	if sec == 1:
		for i in range(1, 380):
			print("Page: "), str(i) + "\033[91m Waiting Grabbed Sites .....  <3"
			rb = requests.get(url2 + str(i),headers=user)
			okbb = rb.content
			domains = re.findall(r'title=".*" tar.?', okbb)
			for iii in domains:
				iii = iii.replace('" target="_blank" reel="nofollow">', "")
				iii = iii.replace('title="', "")
				iii = iii.replace('" targ', "")
				print("\033[95mhttp://" + iii + "/")
				with open("Onhold_defacer.txt", "a") as by:
					by.writelines("http://" + iii + "/")
					by.writelines("\n")
			print ("\t\t[+] Page Saved_"),str(i) +(" done [+]\n")
	elif sec == 2:
		for i in range(1, 25):
			print("Page: "), str(i) + " \033[91mWaiting Grabbed Sites Governement .....  <3"
			rb = requests.get(url4 + str(i),headers=user)
			okbb = rb.content
			domains = re.findall(r'title=".*" tar.?', okbb)
			for iii in domains:
				iii = iii.replace('" target="_blank" reel="nofollow">', "")
				iii = iii.replace('title="', "")
				iii = iii.replace('" targ', "")
				print("\033[95mhttp://" + iii + "/")
				with open("govSites_defacer.txt", "a") as by:
					by.writelines("http://" + iii + "/")
					by.writelines("\n")
			print ("\t\t[+] Page Saved_"),str(i) +(" done [+]\n")
	else:
		print("Fuck You Men 2")


def mirroirh():
	print("""
		   |---| Grabb Sites From Mirror-h.org |--|
			\033[91m[1] \033[95mGrabb Sites By Onhold
			\033[91m[2] \033[95mGrabb Sites By Auto_Notifier
		""")
	sec = int(raw_input("Choose Section: "))
	if sec == 1:
		url = "https://mirror-h.org/archive/page/"
		try:
			for pp in range(1, 40254):
				dz = requests.get(url + str(pp))
				dzz = dz.content
				qwd = re.findall(r'/zone/(.*)</a></td>', dzz)
				print(" \033[91m[*] Please Wait To Grabb Sites ...... Page: "), pp
				for ii in qwd:
					ii = ii.replace('<i class="icon-search"></i>', "")
					ii = ii.replace(ii[:10], "")
					ii = ii.replace("\r\n\r\n", "\r\n")
					ii = ii.strip()
					#iio = ii.replace('<i class="icon-search"></i>', "hhhhhhhhhhhhh")
					print("\033[95m" + ii)
					with open( 'onzeb_mirror.txt', 'a') as rr:
						rr.write(ii + '\n')
		except:
			pass
	elif sec == 2:
		url = "https://mirror-h.org/search/hacker/" 
		try:
			for ha in range(1, 2000):
				print("\033[91mWait To Grabb From Hacker: "), ha
				dz = requests.get(url + str(ha) + "/pages/1")
				dzz = dz.content
				qwd = re.findall(r'/pages/\d" title="Last"', dzz)
				for i in qwd:
					i = i.rstrip()
					sss = i.replace("/pages/","")
					ss = sss.replace('" title="Last"',"")
					ssf = int(ss) + 1
					for ii in range(1, ssf):
						print(" \033[91m[*] Please Wait To Grabb Sites ...... Page: "), ii
						dd = requests.get(url + str(ha) + "/pages/"+ str(ii))
						op = dd.content
						qwdd = re.findall(r'/zone/(.*)</a></td>', op)
						for idi in qwdd:
							idi = idi.replace('<i class="icon-search"></i>', "")
							idi = idi.replace(idi[:10], "")
							idi = idi.replace("\r\n\r\n", "\r\n")
							idi = idi.strip()
							#iio = ii.replace('<i class="icon-search"></i>', "hhhhhhhhhhhhh")
							print("\033[95m" + idi)
							with open( 'top_mirror.txt', 'a') as rr:
								rr.write(idi + '\n')
		except:
			pass


def overflowzone():
	print("""
		|---| Grabb Sites From overflowzone.com |--|
			\033[91m[1] \033[95mGrabb Sites By Onhold
			\033[91m[2] \033[95mGrabb Sites By AutoNotifier
		""")
	sec = int(raw_input("Choose Section: "))
	if sec == 1:
		url = "http://attacker.work/onhold/onhold/page/"
		dz = requests.get(url + "1")
		dzz = dz.content
		tn = re.findall(r'<a href="/onhold/page/(.*)" title="Last">', dzz)
		for ii in tn:
			qwd = ii.split('/')[-1]
			for ok in range(1, int(qwd)):
				okk = requests.get(url + str(ok))
				print("`\t\t\t" + url + str(ok))
				fel = okk.content
				okkk = re.findall(r'">http://(.*)</a></td>', fel)
				for iii in okkk:
					iii = iii.rstrip()
					print("\033[95mhttp://" + iii.split('/')[0])
					with open( 'onhold_attackerwork.txt', 'a') as rr:
						rr.write("http://" + iii.split('/')[0] + '\n')
	elif sec == 2:
		url = "http://attacker.work/archive/page/"
		dz = requests.get(url + "1")
		dzz = dz.content
		tn = re.findall(r'<a href="/archive/page/(.*)" title="Last">', dzz)
		for ii in tn:
			qwd = ii.split('/')[-1]
			for ok in range(1, int(qwd)):
				okk = requests.get(url + str(ok))
				print("`\t\t\t" + url + str(ok))
				fel = okk.content
				okkk = re.findall(r'">http://(.*)</a></td>', fel)
				for iii in okkk:
					iii = iii.rstrip()

					print("\033[95mhttp://" + iii.split('/')[0])
					with open( 'archive_attackerwork.txt', 'a') as rr:
						rr.write("http://" + iii.split('/')[0] + '\n')
	else:
		print("hhhhhhhh tnkt")
def bYPAS():
	exploit = ["/member/","/admin/login.php","/admin/panel.php","/admin/","/login.php","/admin.html","/admin.php","/admin-login.php"]
	try:
		q = raw_input('\033[96m Entre Liste Site: \033[90m ')
		q = open(q, 'r')
	except:
		print("\033[91mEntre List Sites -_- #Noob ")
		sys.exit()
	for lst in q:
		lst = lst.rstrip()
		print("\033[94m 	Wait Scaning ....... \033[94m"), lst
		for exploits in exploit:
			exploits.rstrip()
			try:
				if lst[:7] == "http://":
					lst = lst.replace("http://","")
				if lst[:8] == "https://":
					lst = lst.replace("https://", "")
				if lst[-1] == "/":
					lst = lst.replace("/","")
				socket.setdefaulttimeout(5)
				conn = httplib.HTTPConnection(lst)
				conn.request("POST", exploits)
				conn = conn.getresponse()
				htmlconn = conn.read()
				if conn.status == 200 and ('type="password"') in htmlconn:
					print("\033[92m [+] Admin Panel [+] ======\033[96m=======> \033[96m ") , lst + exploits
					with open("admin_panels.txt", "a") as by:
						by.writelines(lst + exploits + "\n")
				else:
					print("\033[91m [-] Not Found : [-]"),lst + exploits
			except:
				pass

def add_http():
	dz = raw_input("Entre List Site: ")
	dz = open(dz, "r")
	for i in dz:
		i = i.rstrip()
		print("http://"+i)
		with open( 'aziz.txt', 'a') as rr:
			rr.write("http://" + i + '\n')
	print("Text Saved !!")

def binger():
	qwd = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}

	print("""
		\033[91m[1] \033[95mGrabb Sites By Ip List
		\033[91m[1] \033[95mGrabb Sites Fox_Contact And Bypass By Ip List
		""")
	o = int(raw_input("Choose Section: "))
	if o == 1:
		gr = raw_input('Give me List Ip: ')
		gr = open(gr,'r')
		for done in gr:
		    remo = []
		    page = 1
		    while page < 251:
		        bing = "http://www.bing.com/search?q=ip%3A"+done+"+&count=50&first="+str(page)
		        opene = requests.get(bing,verify=False,headers=qwd)
		        read = opene.content
		        findwebs = re.findall('<h2><a href="(.*?)"', read)
		        for i in findwebs:
		            o = i.split('/')
		            if (o[0]+'//'+o[2]) in remo:
		                pass
		            else:
		                remo.append(o[0]+'//'+o[2])
		                print '{}[XxX] '.format(fg,sb),(o[0]+'//'+o[2])
		                with open('Grabbed.txt','a') as s:
		                    s.writelines((o[0]+'//'+o[2])+'\n')
		        page = page+5
	elif o == 2:
		qwd = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
		gr = raw_input('Give me List Ip: ')
		gr = open(gr,'r')
		for done in gr:
		    remo = []
		    page = 1
		    print("Wait Grabb Sites From iP: "), done
		    while page < 251:
		        bing = "http://www.bing.com/search?q=ip%3A"+done + " powered by fox_contact"+"+&count=50&first="+str(page)
		        opene = requests.get(bing,verify=False,headers=qwd)
		        read = opene.content
		        findwebs = re.findall('<h2><a href="(.*?)"', read)
		        for i in findwebs:
		            o = i.split('/')
		            if (o[0]+'//'+o[2]) in remo:
		                pass
		            else:
		                remo.append(o[0]+'//'+o[2])
		                print '[XxX] ' + (o[0]+'//'+o[2])
		                with open('foxcontact.txt','a') as s:
		                    s.writelines((o[0]+'//'+o[2])+'\n')
		        page = page+5

		        bing = "http://www.bing.com/search?q=ip%3A"+done + " admin/login.php"+"+&count=50&first="+str(page)
		        opene = requests.get(bing,verify=False,headers=qwd)
		        read = opene.content
		        findwebs = re.findall('<h2><a href="(.*?)"', read)
		        for i in findwebs:
		            o = i.split('/')
		            if (o[0]+'//'+o[2]) in remo:
		                pass
		            else:
		                remo.append(o[0]+'//'+o[2])
		                dd = requests.get(o[0]+'//'+o[2] + "/admin/login.php")
		                ddd = dd.content
		                if 'type="password"' in ddd:
		                	print("\033[92mAdmin_Panel Site: >>>>>>\033[91m"),o[0]+'//'+o[2] + "/admin/login.php"
		                	with open('admin panel.txt','a') as s:
		                		s.writelines((o[0]+'//'+o[2])+'\n')
		   		page = page+5
	else:
		print("dir numero azbi nooooooob")


def cms_detected():
	lst = raw_input("Entre List Site: ")
	lst = open(lst, 'r')
	for i in lst:
		i = i.rstrip()
		print("\033[91m[+] \033[95mPlease Waiting To Scaning ... "), "\033[94m" + i + " \033[91m[+]"
		try:
			dz = requests.get(i)
			ok = dz.content
			#-------------WP---------------------------
			
			if "wp-content" in ok:
				print("\033[92mWp Site : >>>>>>>>>>>>>>\033[91m"), i + "/wp-login.php"
				with open("wp sites.txt", "a") as wpp:
					wpp.writelines(i + "/wp-login.php"+ "\n")
					#-------JM--------------------------
			elif "com_content" in ok:
				print("\033[92mJm Site: >>>>>>>>>>>>>>\033[91m"), i + "/administrator/"
				with open("joomla sites.txt", "a") as jmm:
					jmm.writelines(i + "/administrator/"+ "\n")
					#---------OPENCARTE-----------------------
			elif "index.php?route" in ok:
				print("\033[92mOpenCart Site: >>>>>>>>>>>>>>\033[91m"), i + "/admin/"
				with open("OpenCart sites.txt", "a") as opncrt:
					opncrt.writelines(i + "/admin/"+ "\n")
					#---------------------------------
			elif "/node/" in ok:
				print("\033[92mDrupal Site: >>>>>>>>>>>>>>\033[91m"), i + "/user/login"
				with open("Drupal sites.txt", "a") as drbl:
					drbl.writelines(i + "/user/login"+ "\n")
			else:
				bypass = ["/admin/login.php","/admin/","/login.php","/admin.html","/admin.php","/member/"]
				for byp in bypass:
					byp = byp.rstrip()
					dd = requests.get(i + byp)
					ddd = dd.content
					if 'type="password"' in ddd:
					    print("\033[92mAdmin_Panel Site: >>>>>>\033[91m"),i +  byp
					    with open("Admin Sites.txt", "a") as by:
					        by.writelines(i + byp + "\n")
					else:
						pass

				print("\033[91m[-] Not Found Cms: [-]"), "\033[91m" + i
		except:
			pass



def spotii():
	#url =  "https://www.spotify.com"

	rl = "http://www.spotify.com/us/xhr/json/isEmailAvailable.php?signup_form[email]="

	try:
		ok = raw_input("{}root@kil3r~# Entre List Email: ".format(fy,sn))
		okd = open(ok, 'r')
	except:
		print("{}zebi  entre list  email -_- nooob").format(fh,sn)
	for i in okd:
		i = i.rstrip()
		qwd = url + i + "&email=" + i
		dz = requests.get(qwd, headers=user)
		dzz = dz.content
		if 'false' in dzz:
			print("{}   [LIVE]     ".format(fg,sn)), "{}".format(fg,sn) + i
			with open("spotify checked.txt", "a") as zebi:
				zebi.writelines(i + '\n')
		else:
			print("{}   [DEAD]     ").format(fh,sn), "{}".format(fh,sn) + i



def clearscrn():
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
clearscrn()

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)

def helper4():
	clearscrn()
	banner = """\033[94m
  ____  _____  _  _______  ___   ___    _  ___ _ _           
 |  _ \|  __ \| |/ /  __ \|__ \ / _ \  | |/ (_) | |          
 | |_) | |  | | ' /| |__) |  ) | (_) | | ' / _| | | ___ _ __ 
 |  _ <| |  | |  < |  _  /  / / > _ <  |  < | | | |/ _ \ '__|
 | |_) | |__| | . \| | \ \ / /_| (_) | | . \| | | |  __/ |   
 |____/|_____/|_|\_\_|  \_\____|\___/  |_|\_\_|_|_|\___|_|   
                                                             
                                                             
	"""
	print("""\033[95m
  ____  _____  _  _______  ___   ___    _  ___ _ _           
 |  _ \|  __ \| |/ /  __ \|__ \ / _ \  | |/ (_) | |          
 | |_) | |  | | ' /| |__) |  ) | (_) | | ' / _| | | ___ _ __ 
 |  _ <| |  | |  < |  _  /  / / > _ <  |  < | | | |/ _ \ '__|
 | |_) | |__| | . \| | \ \ / /_| (_) | | . \| | | |  __/ |   
 |____/|_____/|_|\_\_|  \_\____|\___/  |_|\_\_|_|_|\___|_|   
                                                             
                                                             	  
                                  Script Name : Tester ^_^
                	Greetz To : \033[93mBANGLADESHI \033[92mHackers  \033[91m|D\033[92mz| \033[91mBDKR28 \033[92mHacker
                                     """)
	slowprint("\n\t\t\t\t\tPowered By : BLACK HAT HACKERS" + "\n\t\t\t\t\t\t Telegram : @bdkr2" + "\n\t\t\t\t\t\t YouTube : BDKR28  ")
	print("")
	print("""
		\033[91m[1] \033[95mGrabb Sites  \033[92m From Zone-h.org   
		\033[91m[2] \033[95mGrabb Sites  \033[92m From Defacers.org   
		\033[91m[3] \033[95mGrabb Sites  \033[92m From mirror-h.org
		\033[91m[4] \033[95mGrabb Sites  \033[92m From overflowzone.com
		\033[91m[5] \033[95mGet Sites bypass With List [Bypass Finder]
		\033[91m[6] \033[95mMass Add (http://) To List ^_^
		\033[91m[7] \033[95mGrabber Sites From Bing :D
		\033[91m[8] \033[95mCms Filtre
		\033[91m[9] \033[95mEmail Valid Spotify


			#######################################################
			# 	  Love 4 Palestine |\033[91m| Live 4 Palestine        #
			#######################################################
			""")		
	try:
		qq = int(raw_input("\033[91m[-] \033[90mroot@bdkr28~# \033[92mChoose Section !!\033[95m : \033[90m"))
		if qq == 1:
			clearscrn()
			print(banner)
			zonehh()
		if qq == 2:
			clearscrn()
			print(banner)
			defacers()
		if qq == 3:
			clearscrn()
			print(banner)
			mirroirh()
		if qq == 4:
			clearscrn()
			print(banner)
			overflowzone()
		if qq == 5:
			clearscrn()
			print(banner)
			bYPAS()
		if qq == 6:
			clearscrn()
			print(banner)
			add_http()
		if qq == 7:
			clearscrn()
			print(banner)
			binger()
		if qq == 8:
			clearscrn()
			print(banner)
			cms_detected()
		if qq == 9:
			clearscrn()
			print(banner)
			spotii()

	except:
		pass
helper4()