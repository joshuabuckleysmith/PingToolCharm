import threading
from app import testpingnumber
from app import pingcomponents
from app import pinger
import IPy

T=threading.Thread

def startping(store, test, pingnumber, buttondis, buttonen, prefix, options, storetxt):
    store = pingcomponents.pingcomponents["store"]
    pingnumber = pingcomponents.pingcomponents["pingnumber"]
    prefix = options[pingcomponents.pingcomponents["prefix"]]
    if testpingnumber.testpingnumber(pingnumber) == True:
        if prefix != "":
            store = (str(store).zfill(5))
            store = store[-5:]
        if prefix == "":
            try:
                IPy.IP(store)
            except:
                raise
        buttonen['state'] = 'normal'
        buttondis['state'] = 'disabled'
        pingthread = T(target=pinger.pinger, args=[store, pingnumber, test, buttondis, buttonen, prefix])
        pingthread.start()
    else:
        print('Number of pings was not a number.')