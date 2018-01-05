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





#root.mainloop()


