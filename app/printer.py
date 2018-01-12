import os
from time import sleep
from app import pingcomponents
from app import logger
from app import pingprint
wlog=logger.log.writelogline



def printer(monitoredthread, store, prefix):
    wlog("printer running")
    outputstring = ""
    pingcount = 0
    while True:
        wlog("in printer, threadkilled = {}".format(pingcomponents.pingcomponents["threadkilled"]))
        wlog("pingcount is {}".format(pingcount))
        sleep(0.5)
        wlog("running printer, slept for 0.5 seconds")
        wlog("in printer after sleep, threadkilled = {}".format(pingcomponents.pingcomponents["threadkilled"]))
        if pingcomponents.pingcomponents["threadkilled"] == 0:
            wlog("printer is attempting to open the temp file")
            openfile = open("1\\temp{}.txt".format(pingcomponents.pingcomponents["UTCIdentity"]), 'r')
        if pingcomponents.pingcomponents["threadkilled"] == 1:
            return
        wlog("opened file is {}".format(openfile))
        openstring = str(openfile.read())
        openfile.close()
        #wlog("opened string is {}".format(openstring))
        if openstring == "Ping request could not find host {}{}. " \
                         "Please check the name and try again.\n".format(prefix, store):
            print(
                "Ping request could not find host {}{}. Is your prefix correct? "
                "Please start ping again when ready.\n".format(
                    prefix, store))
            openfile.close()
            break
        len1 = len(openstring)
        wlog("Length of open string is {}".format(len1))
        len2 = len(outputstring)
        wlog("Length of output string is {}".format(len2))
        wlog("testing if len 1 > len 2")
        if len1 > len2:
            wlog("len1 is > len 2")
            outputstring = openstring
            len3 = (len(outputstring.split('\n')))
            wlog("len 3 is outputstring line count {}".format(len3))
            outsplit = outputstring.splitlines()[len3 - 2] # This finds the first line
            if outsplit[0] != " ":
                print("{} {}".format((pingcount + 1), outputstring.splitlines()[len3 - 2]))
            if outsplit[0] == " ":
                print("{} {}".format((pingcount + 1), outputstring.splitlines()[len3 - 7]))
            pingcount = pingcount + 1
        th1 = monitoredthread.poll()
        wlog("polled monitored thread, it is {}".format(th1))
        if th1 != None:
            wlog("pingprint store {}".format(store))
            pingprint.pingprint(store)
            wlog("output thread has ended")
            break
