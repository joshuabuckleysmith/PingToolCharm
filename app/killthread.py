import os
import IPy
from app import pingprint
from app import pingcomponents
def killthread(buttondis, buttonen):
    #should disable cancel and enable ping
    buttondis['state'] = 'disabled'
    buttonen['state'] = 'normal'
    process = pingcomponents.pingcomponents["process"]
    store = pingcomponents.pingcomponents["store"]
    store = (str(store).zfill(5))
    store = store[-5:]
    try:
        storeip = IPy.IP(store)
    except:
        storeip = store
    if storeip != store:
        store = store.zfill(5)
    else:
        store = storeip
    # print("store is {}".format(store))
    # print("pid is {} ".format(process))
    os.system("TASKKILL /F /PID {} /T > nul".format(process))
    # os.system("TASKKILL /F /PID {} /T > nul".format(process))
    openfile = open("1\\temp{}.txt".format(store), 'r')
    pingprint.pingprint(openfile, store)
    openfile.close()

