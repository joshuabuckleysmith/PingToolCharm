import os
from app import pingprint
from app import pingcomponents
def killthread(buttondis, buttonen):
    #should disable cancel and enable ping
    buttondis['state'] = 'disabled'
    buttonen['state'] = 'normal'
    try:
        process = pingcomponents.pingcomponents["process"]
    except:
        pass
    store = pingcomponents.pingcomponents["store"]
    try:
        os.system("TASKKILL /F /PID {} /T > nul".format(process))
    except:
        pass
    try:
        openfile = open("1\\temp{}.txt".format(store), 'r')
        pingprint.pingprint(openfile, store)
        openfile.close()
    except:
        print('Ping failed')
