import collections
import os
import tkinter as tk
from time import sleep
from app import pingcomponents
from app import killthread, sp, startasthread
from app import logger
wlog=logger.log.writelogline
rlog=logger.log.readlog


root = tk.Tk()

options = collections.OrderedDict(
    [
        ("IP Address", ""), ("Router(dg)", "dg"),
        ("Switch US(ussw010)", "ussw010"),
        ("Switch Canada(casw010)", "casw010"),
        ("Workstation(mws)", "mws"), ("FoH Switch(ussw030)", "ussw030")
    ]
)
test = tk.StringVar()
pingnumber = tk.IntVar()
store = tk.StringVar()
prefix = tk.StringVar()
logoutput = tk.StringVar()

prefix.set("IP Address")
storetxt = tk.Label(text="Store Number")

wlog("vars set")


def updatetext(button2): #for ipaddress
    wlog("updatetext")
    button2['text'] = "Store Number"


def downdatetext(button2):  # for store number
    wlog("downdatetext")
    button2['text'] = "IP Address"


def destroyapp():
    wlog("downdatetext")
    os.system("del 1\* /s /q")
    root.destroy()


def buttons():
    wlog("buttons from tkwindows")
    '''creates tk window'''
    testbutton = tk.Checkbutton\
        (text="Set MTU to 4000 (default 1345)", variable=test, onvalue="secondary",
        offvalue="primary", )
    testbutton.deselect()
    testbutton.grid(row=2, column=2)
    pingtxt = tk.Label(text="Ping Number")  # Ping test labels for text boxes.
    pingtxt.grid(row=0, column=2)
    storetxt = tk.Label(text="Store Number")  # Ping test labels for text boxes.
    storetxt.grid(row=0, column=1)
    pingentry = tk.Entry(textvariable=pingnumber)
    pingentry.grid(row=1, column=2)
    storeentry = tk.Entry(textvariable=store)
    storeentry.grid(row=1, column=1)
    dropout = tk.OptionMenu(root, prefix, *options)
    dropout.grid(row=1, column=0)

    def spf(*args):
        wlog("spf run")
        sp.sp(store.get(), test.get(), pingnumber.get(), ping, cancelping, prefix.get(), options, storetxt)
    ping = tk.Button(text="Start Ping", command=spf)
    ping.grid(row=1, column=3)

    def killthreadf():
        wlog("killthreadf run")
        killthread.killthread(cancelping, ping)
    cancelping = tk.Button(text="Cancel Ping", command=killthreadf)
    cancelping['state'] = 'disabled'
    cancelping.grid(row=1, column=4)
    exit = tk.Button(text="exit", fg="red", command=destroyapp)
    exit.grid(row=2, column=1)
    wlog("loggingwindow run")

    logout=tk.Toplevel()

    outlabel = tk.Text(logout, height=40, width=80, font="Consolas 10")
    outlabel.grid(row=0, column=0)
    outlabel.see("end")
    scrollb = tk.Scrollbar(logout, command=outlabel.yview)
    outlabel['yscrollcommand'] = scrollb.set
    scrollb.grid(row=0, column=1, sticky='nsew')


    def loggingwindowf(outlabel):
        while True:
            # optional var monitoring, will update constantly:
            wlog("Threadkilled = {}".format(pingcomponents.pingcomponents["threadkilled"]))
            # optional var monitoring:
            outlabel.insert(tk.END, rlog())
            outlabel.see(tk.END)
            sleep(0.2)

    loggingwindowdaemon = startasthread.T(target=loggingwindowf, args=[outlabel])
    loggingwindowdaemon.setDaemon(True)
    loggingwindowdaemon.start()


    root.bind('<Return>', spf)
    root.title("Starbucks Ping")


    def textdaemonf(prefix, storetxt):
        wlog("textdaemonf run")
        while True:
            if prefix.get() == "IP Address":
                storetxt['text'] = "IP Address"
            if prefix.get() != "IP Address":
                storetxt['text'] = "Store Number"
            sleep(0.02)

    textdaemon = startasthread.T(target=textdaemonf, args=[prefix, storetxt])
    textdaemon.setDaemon(True)
    textdaemon.start()



    def loggingwindowf(outlabel):

        outlabel['text']=logger.log
        #loggingwindowdaemon = startasthread.T(target=updatelog())
        #loggingwindowdaemon.setDaemon(True)
        #loggingwindowdaemon.start()