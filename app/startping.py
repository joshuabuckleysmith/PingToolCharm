import threading
from app import testpingnumber
from app import pingcomponents
from app import pinger

import IPy


T=threading.Thread

def startping(store, test, pingnumber, buttondis, buttonen, prefix, options, storetxt):

    pingsize = 0
    store = pingcomponents.pingcomponents["store"]
    pingnumber = pingcomponents.pingcomponents["pingnumber"]
    prefix = options[pingcomponents.pingcomponents["prefix"]]
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
    if testpingnumber.testpingnumber(pingnumber) == True:
        print("pingnumber tested true")
        if prefix != "IP Address":
            print("prefix did not equal IP Address")
            store = (str(store).zfill(5))
            print('Pinging {}{} with {} bytes {} times.'.format(prefix, store, pingsize, pingnumber))
        if prefix == "":
            print("prefix equals nothing")
            try:
                IPy.IP(store)
                # print(IP(store))
                print('Pinging ip address {} with {} bytes {} times.'.format(IPy.IP(store), pingsize, pingnumber))
            except:
                raise
        buttonen['state'] = 'normal'
        buttondis['state'] = 'disabled'
        pingthread = T(target=pinger.pinger, args=[store, pingnumber, test, buttondis, buttonen, prefix])
        pingthread.start()
    else:
        print('Number of pings was not a number.')