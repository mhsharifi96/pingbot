#!/usr/bin/env python2.5
from threading import Thread
import subprocess
from Queue import Queue
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters,CommandHandler, CallbackQueryHandler

num_threads = 4
queue = Queue()
ips = ["google.com","linuxkhan.ir","gitiserver.com","bing.com"]


class pingModules(object):
    def __init__(self):
        
        self.handlers=[
            CommandHandler('start',self.start_ping),
            CommandHandler('finish',self.finish)]
            
    def get_handlers(self):
        return self.handlers
        
    def start_ping(self,bot,update):
        print "i am in start ping :)"
        user_id=update.message.from_user.id
        ips = ["185.88.152.87","linuxkhan.ir","gitiserver.com","iran-choob.com"]
        for ip in ips:
            
            res = subprocess.call(['ping', '-c', '5', ip])
            if res == 0:
                print "ping to", ip, "OK"

                spc_ip="%s: is alive" % ip
                bot.sendMessage(user_id,
                        text= spc_ip)
            elif res == 2:
                spc_ip="%s: no response" % ip

                print "no response from",ip
                bot.sendMessage(user_id,
                        text= spc_ip)
            else:
                print "ping to", ip, "failed!"
                spc_ip="%s: failed" % ip
        bot.sendMessage(user_id,
                        text= spc_ip)
       
        
    
    def finish(self):
        print "I am in finish"

    