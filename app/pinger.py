from subprocess import Popen
from time import sleep
import os
from app import printer, startasthread, pingcomponents

def pinger(store, pingnumber, primsec, buttondis, buttonen, prefix):
    '''Takes a store number, index as INT, primsec as STRING sets primary or secondary test'''
    print("**********************************\n")
    displayconfirmationline = "Pinging {}{} {} times".format(prefix, store, pingnumber)
    if primsec == "primary":
        print(displayconfirmationline)
        pingthread = Popen("ping -n {} -l 1345 {}{} > 1\\temp{}.txt".format(pingnumber, prefix, store, store), shell=True)
    if primsec == "secondary":
        print(displayconfirmationline)
        pingthread = Popen("ping -n {} -l 4000 {}{} > 1\\temp{}.txt".format(pingnumber, prefix, store, store), shell=True)
    pingcomponents.pingcomponents["process"] = pingthread.pid
    outputthread = startasthread.T(target=printer.printer, args=[pingthread, store, prefix])
    outputthread.start()
    while True:
        threadalive2 = bool(outputthread.is_alive())
        sleep(0.02)
        if threadalive2 == False:
            sleep(0.05)
            buttondis['state'] = 'normal'  # reenables buttons when ping completes.
            buttonen['state'] = 'disabled'
            os.system("del 1\\temp{}.txt".format(store))
            break