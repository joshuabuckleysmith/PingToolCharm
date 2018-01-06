from subprocess import Popen
from time import sleep
import os
from app import printer, startasthread, pingcomponents

def pinger(store, pingnumber, primsec, buttondis, buttonen, prefix):
    # print(prefix)
    '''Takes a store number, index as INT, primsec as STRING sets primary or secondary test'''
    print("**********************************")
    if primsec == "primary":
        print("ping -n {} -l 1345 {}{} > 1\\temp{}.txt".format(pingnumber, prefix, store, store))
        pingthread = Popen("ping -n {} -l 1345 {}{} > 1\\temp{}.txt".format(pingnumber, prefix, store, store), shell=True)
    if primsec == "secondary":
        print("ping -n {} -l 4000 {}{} > 1\\temp{}.txt".format(pingnumber, prefix, store, store))
        pingthread = Popen("ping -n {} -l 4000 {}{} > 1\\temp{}.txt".format(pingnumber, prefix, store, store), shell=True)
    pingcomponents.pingcomponents["process"] = pingthread.pid
    #print(pingcomponents.pingcomponents["process"])
    outputthread = startasthread.T(target=printer.printer, args=[pingthread, store, prefix])
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
            os.system("del 1\\temp{}.txt".format(store))
            break