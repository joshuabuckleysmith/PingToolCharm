import os
from app import pingprint
from app import pingcomponents
from app import logger
wlog=logger.log.writelogline

wlog("imported killthread")

def killthread(buttondis, buttonen):
    wlog("in killthread, threadkilled = {}".format(pingcomponents.pingcomponents["threadkilled"]))
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
    pingcomponents.pingcomponents["threadkilled"] = 1
    wlog("in killthread after taskkill threadkilled = {}".format(pingcomponents.pingcomponents["threadkilled"]))
    try:
        pingprint.pingprint(store)
    except:
        print('Ping failed')
