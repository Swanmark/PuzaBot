#-*- coding:utf-8 -*-
import socket
import time
import os
from random import randrange
import json
import urllib2
nick = "DrPuzaBot"
server = "irc.freenode.net"
ras = "#coinking"
ras2 = "##DrPuza"
nickservpass = "nickservpwd"
bSize = "8192"
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, 6667))
time.sleep(1)
irc.recv(8192)
irc.send('NICK '+nick+'\r\n')
irc.send('USER PUZA PUZA PUZA :Puza is #1\r\n')
time.sleep(2)
irc.send('JOIN '+ras+'\r\n')
irc.send('JOIN '+ras2+'\r\n')
#irc.send('PRIVMSG nickserv :IDENTIFY DrPuzaBot '+nickservpass+'\r\n')
while True:
  data = irc.recv(8192)
  print (data)
  if data.find('PING') != -1:
    irc.send('PONG ' +data.split()[1]+'\r\n')
  usrmsg = data.split(':')[-1].strip()
  firstmsg = usrmsg.split(' ')[0].lower()
  if firstmsg == "!love":
    try:
      arg1 = usrmsg.split(' ')[1]
    except:
      arg1 = "error"
    chan = data.split(' ')[2]
    if arg1 == "error":
      irc.send('PRIVMSG '+chan+' :\0036► ► ► ► ► \0034THIS IS THE LOVE ZONE\0036 ◄ ◄ ◄ ◄ ◄\r\n')
    else:
      irc.send('PRIVMSG '+chan+' :\0036► ► ► ► ► \0034I LOVE '+str(arg1.upper())+'\0036 ◄ ◄ ◄ ◄ ◄\r\n')
  if firstmsg == "!charity" or firstmsg == "!donate":
    chan = data.split(' ')[2]
    btcurl = urllib2.urlopen('http://bkchain.org/btc/api/v1/address/balance/1A3k78jypUBPdBxroSBbGdhctNPttDo6FT')
    dogeurl = urllib2.urlopen('http://bkchain.org/doge/api/v1/address/balance/DN1iT4njrHsb61FowPoHa2BQ49SozHw9ep')
    ltcurl = urllib2.urlopen('http://bkchain.org/ltc/api/v1/address/balance/LMWYxZ2jbKhkYqU1jWo2LPUY3Wy255o2nu')
    btcjson = json.load(btcurl)
    dogejson = json.load(dogeurl)
    ltcjson = json.load(ltcurl)
    irc.send('PRIVMSG '+chan+' :Donations to the following addresses will all go to charity! =D\r\n')
    time.sleep(0.1)
    irc.send('PRIVMSG '+chan+' :Every month there will be a different charity receiving the donations.\r\n')
    time.sleep(0.1)
    irc.send('PRIVMSG '+chan+' :BTC: 1A3k78jypUBPdBxroSBbGdhctNPttDo6FT (Current Balance: '+str(btcjson[0]["balance"]/100000000.0)+' BTC)\r\n')
    time.sleep(0.1)
    irc.send('PRIVMSG '+chan+' :DOGE: DN1iT4njrHsb61FowPoHa2BQ49SozHw9ep (Current Balance: '+str(dogejson[0]["balance"]/100000000.0)+' DOGE)\r\n')
    time.sleep(0.1)
    irc.send('PRIVMSG '+chan+' :LTC: LMWYxZ2jbKhkYqU1jWo2LPUY3Wy255o2nu (Current Balance: '+str(ltcjson[0]["balance"]/100000000.0)+' LTC)\r\n')
    time.sleep(0.01)
