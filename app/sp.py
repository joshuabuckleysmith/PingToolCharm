from datetime import datetime
from app import startasthread
from app import startping
from app import pingcomponents
from app import logger
wlog=logger.log.writelogline

def sp(a, b, c, d, e, f, g, h):
    wlog("sp defined")
    '''a store.get(), b test.get(), c pingnumber.get(), d ping, e cancelping, f prefix.get(), g options, h storetxt'''
    pingcomponents.pingcomponents["store"] = a
    pingcomponents.pingcomponents["test"] = b
    pingcomponents.pingcomponents["pingnumber"] = c
    pingcomponents.pingcomponents["prefix"] = f
    pingcomponents.pingcomponents["UTCIdentity"] = (datetime.utcnow() - datetime(1970, 1, 1)).total_seconds()
    wlog("startping runs this point")
    startasthread.startasthread(startping.startping(a, b, c, d, e, f, g, h))