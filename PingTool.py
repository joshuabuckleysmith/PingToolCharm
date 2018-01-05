import os
import subprocess
import threading
import sys
import re
import signal
from IPy import IP
from subprocess import Popen, PIPE, check_output
import tkinter as tk
from time import sleep
import app
from app import tkbuttons

test = 1
T = threading.Thread
STOREOK = False
process = 0

pingcomponents = {}
pingcomponents["store"] = 1
pingcomponents["test"] = "primary"
pingcomponents["pingnumber"] = "1"
pingcomponents["prefix"] = "IP Address"
pingcomponents["cancelled"] = "0"






def startasthread(funct):
    thread = T(target=funct)
    thread.start()





# def onclick(event=None):
#    startasthread(lambda:startping(store.get(), test.get(), pingnumber.get(), ping, cancelping, target.get(), options, storetxt))

def killthread(buttondis, buttonen):
    buttondis['state'] = 'disabled'
    buttonen['state'] = 'normal'
    global pingcomponents
    process = pingcomponents["process"]
    store = pingcomponents["store"]
    try:
        storeip = IP(store)
    except:
        storeip = store
    if storeip != store:
        store = store.zfill(5)
    else:
        store = storeip
    # print("store is {}".format(store))
    # print("pid is {} ".format(process))
    os.system("TASKKILL /F /PID {} /T".format(process))
    # os.system("TASKKILL /F /PID {} /T > nul".format(process))
    openfile = open("temp{}.txt".format(store), 'r')
    pingprint(openfile)


#    try:
#        openfile = open("temp{}.txt".format(store), 'r')
#        pingprint(openfile)
#        openstring = str(openfile.read())
#        print(outputstring)
#        #print(outputstring.splitlines()[len3-5])
#        #print(outputstring.splitlines()[len3-4])
#        #print(outputstring.splitlines()[len3-3])
#        #print(outputstring.splitlines()[len3-2])
#        openfile.close()
#        os.system("del temp{}.txt".format(store))
#        print("ping Cancelled")
#    except:
#        pass


def startping(store, test, pingnumber, buttondis, buttonen, prefix, options, storetxt):
    global pingcomponents
    pingsize = 0
    store = pingcomponents["store"]
    pingnumber = pingcomponents["pingnumber"]
    prefix = pingcomponents["prefix"]
    print("store {}".format(store))
    print("test {}".format(test))
    print("pingno {}".format(pingnumber))
    print("pingsize {}".format(pingsize))
    print("options {}".format(options))
    print("prefix passed is {}".format(prefix))
    if test == "primary":
        pingsize = "1345"
    else:
        pingsize = "4000"
    if testpingnumber(pingnumber) == True:
        print("pingnumber tested true")
        if prefix != "IP Address":
            print("prefix did not equal IP Address")
            store = (str(store).zfill(5))
            print('Pinging {}{} with {} bytes {} times.'.format(prefix, store, pingsize, pingnumber))
        if prefix == "":
            print("prefix equals nothing")
            try:
                IP(store)
                # print(IP(store))
                print('Pinging ip address {} with {} bytes {} times.'.format(IP(store), pingsize, pingnumber))
            except:
                raise
        buttonen['state'] = 'normal'
        buttondis['state'] = 'disabled'
        pingthread = T(target=pinger, args=[store, pingnumber, test, buttondis, buttonen, prefix])
        pingthread.start()
    else:
        print('Number of pings was not a number.')


def testpingnumber(pingnumber):
    if pingnumber == "":
        # print('ping setup 333')
        return False
    try:
        int(pingnumber)
        # print('ping setup 11')
        return True
    except:
        # print('ping setup 12')
        return False


def pinger(store, pingnumber, primsec, buttondis, buttonen, prefix):
    # print(prefix)
    '''Takes a store number, index as INT, primsec as STRING sets primary or secondary test'''
    global pingcomponents
    print("\n")
    if primsec == "primary":
        print("ping -n {} -l 1345 {}{} > temp{}.txt".format(pingnumber, prefix, store, store))
        pingthread = Popen("ping -n {} -l 1345 {}{} > temp{}.txt".format(pingnumber, prefix, store, store), shell=True)
    if primsec == "secondary":
        print("ping -n {} -l 4000 {}{} > temp{}.txt".format(pingnumber, prefix, store, store))
        pingthread = Popen("ping -n {} -l 4000 {}{} > temp{}.txt".format(pingnumber, prefix, store, store), shell=True)
    pingcomponents["process"] = pingthread.pid
    print(pingcomponents["process"])
    outputthread = T(target=printoutput, args=[pingthread, store, prefix])
    outputthread.start()
    while True:
        threadalive = bool(pingthread.poll())
        threadalive2 = bool(outputthread.is_alive())
        sleep(0.02)
        # print("pingthread is {}".format(threadalive))
        # print("outputthread is {}".format(threadalive2))
        if threadalive2 == False:
            # print("pid is {} ".format(pingthread.pid))
            # print(pingthread.poll())
            # os.system("TASKKILL /F /PID {} /T > nul".format(pingthread.pid))
            # print('waiting timeout')
            # if threadalive == False:
            sleep(0.05)
            print("\nPing Complete. Start a new ping with the GUI.")
            buttondis['state'] = 'normal'  # reenables buttons when ping completes.
            buttonen['state'] = 'disabled'
            os.system("del temp{}.txt".format(store))
            break


def printoutput(monitoredthread, store, prefix):
    outputstring = ""
    pingcount = 0
    sleep(1)
    while True:
        sleep(0.05)
        openfile = open("temp{}.txt".format(store), 'r')
        openstring = str(openfile.read())
        if openstring == "Ping request could not find host {}{}. Please check the name and try again.\n".format(prefix,
                                                                                                                store):
            print(
                "Ping request could not find host {}{}. Is your prefix correct? Please start ping again when ready.\n".format(
                    prefix, store))
            openfile.close()
            break
        len1 = len(openstring)
        len2 = len(outputstring)
        # print("len 1 is {}".format(len1))
        # print("len 2 is {}".format(len2))
        if len1 > len2:
            outputstring = openstring
            len3 = (len(outputstring.split('\n')))
            # if pingcount > 0:
            # print("{} pings sent".format(pingcount))
            outsplit = outputstring.splitlines()[len3 - 2]
            if outsplit[0] != " ":
                print("{} {}".format((pingcount + 1), outputstring.splitlines()[len3 - 2]))
            if outsplit[0] == " ":
                print("{} {}".format((pingcount + 1), outputstring.splitlines()[len3 - 7]))
                # print("{} pings sent".format(pingcount+1))
            # print(outputstring)
            pingcount = pingcount + 1
        # print("moni thread{}".format(monitoredthread.poll()))
        th1 = monitoredthread.poll()
        # print("TH1 {}".format(th1))
        if th1 != None:
            # print("monitoredthread.poll() was {}".format(monitoredthread.poll()))
            # print("lines = {}".format(len(outputstring.split('\n'))))
            try:
                print("\n")
                print(outputstring.splitlines()[len3 - 5])
                print(outputstring.splitlines()[len3 - 4])
                print(outputstring.splitlines()[len3 - 3])
                print(outputstring.splitlines()[len3 - 2])
            except:
                print("nothing to print")
            openfile.close()
            # print("output file closed")
            sleep(0.05)
            break




tkbuttons.tkbuttons()
root.mainloop()


