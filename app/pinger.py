from subprocess import Popen
from time import sleep
from app import logger
from app import pingcomponents
wlog=logger.log.writelogline
wlog("imported pinger")

import os
from app import printer, startasthread, pingcomponents

def pinger(store, pingnumber, primsec, buttondis, buttonen, prefix):
    wlog("pinger starting")
    wlog("resetting killed thread tracking")
    pingcomponents.pingcomponents["threadkilled"] = 0
    wlog(pingcomponents.pingcomponents["threadkilled"])
    '''Takes a store number, index as INT, primsec as STRING sets primary or secondary test'''
    print("**********************************\n")
    displayconfirmationline = "Pinging {}{} {} times".format(prefix, store, pingnumber)
    if primsec == "primary":
        wlog(displayconfirmationline)
        print(displayconfirmationline)
        pingthread = Popen("ping -n {} -l 1345 {}{} > 1\\temp{}.txt".format(pingnumber, prefix, store, pingcomponents.pingcomponents["UTCIdentity"]), shell=True)
    if primsec == "secondary":
        print(displayconfirmationline)
        wlog(displayconfirmationline)
        pingthread = Popen("ping -n {} -l 4000 {}{} > 1\\temp{}.txt".format(pingnumber, prefix, store, pingcomponents.pingcomponents["UTCIdentity"]), shell=True)
    pingcomponents.pingcomponents["process"] = pingthread.pid
    wlog("printer is started in its own thread here")
    outputthread = startasthread.T(target=printer.printer, args=[pingthread, store, prefix])
    outputthread.start()
    wlog("output thread started, this is started in printer")
    while True:
        threadalive2 = bool(outputthread.is_alive())
        sleep(0.2)
        if threadalive2 == False:
            buttondis['state'] = 'normal'  # reenables buttons when ping completes.
            buttonen['state'] = 'disabled'
            break