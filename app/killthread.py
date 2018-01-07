import os
from app import pingprint
from app import pingcomponents
def killthread(buttondis, buttonen):
    #should disable cancel and enable ping
    buttondis['state'] = 'disabled'
    buttonen['state'] = 'normal'
    process = pingcomponents.pingcomponents["process"]
    store = pingcomponents.pingcomponents["store"]
    os.system("TASKKILL /F /PID {} /T > nul".format(process))
    openfile = open("1\\temp{}.txt".format(store), 'r')
    pingprint.pingprint(openfile, store)
    openfile.close()

