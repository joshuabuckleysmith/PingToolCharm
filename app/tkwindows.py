import threading
import tkinter as tk
from time import sleep
from app import killthread, sp, pingcomponents, startasthread


root = tk.Tk()

def buttons():
    test = tk.StringVar()
    pingnumber = tk.IntVar()
    store = tk.StringVar()
    prefix = tk.StringVar()
    prefix.set("IP Address")
    options = {"Router(dg)": "dg", "Switch US(ussw010)": "ussw010", "Switch Canada(casw010)": "casw010",
               "Workstation(mws)": "mws", "IP Address": ""}
    '''creates tk window'''
    testbutton = tk.Checkbutton(text="Set MTU to 4000 (default 1345)", variable=test, onvalue="secondary",
                                offvalue="primary", )
    testbutton.deselect()
    testbutton.grid(row=2, column=2)
    pingtxt = tk.Label(text="Ping Number")  # Ping test labels for text boxes.
    pingtxt.grid(row=0, column=2)
    storetxt = tk.Label(text="Store Number")  # Ping test labels for text boxes.
    storetxt.grid(row=0, column=1)
    pingentry = tk.Entry(text="Number of Pings", textvariable=pingnumber)
    pingentry.grid(row=1, column=2)
    storeentry = tk.Entry(text="Store Number", textvariable=store)
    storeentry.grid(row=1, column=1)
    dropout = tk.OptionMenu(root, prefix, *options)
    dropout.grid(row=1, column=0)

    # Ping command, sends store, test, pingnumber, ping, cancelping, prefix options and storetxt)
    def spf():
        sp.sp(store.get(), test.get(), pingnumber.get(), ping, cancelping, prefix.get(), options, storetxt)
    ping = tk.Button(text="Start Ping", command=spf)
    ping.grid(row=1, column=3)
    # cancelping = tk.Button(text="Cancel Ping", command=lambda:killthread(cancelping, ping))
    def killthreadf():
        killthread.killthread(cancelping, ping)
    cancelping = tk.Button(text="Cancel Ping", command=killthreadf)
    cancelping['state'] = 'disabled'
    cancelping.grid(row=1, column=4)
    exit = tk.Button(text="exit", fg="red", command=root.destroy)
    exit.grid(row=2, column=1)
    root.bind('<Return>', sp)
    root.title("Starbucks Ping")
    def updatetext(button1, button2):
        while True:
            sleep(0.05)
            # print('checking text button')
            if button1.get() == "IP Address":
                button2['text'] = "IP Address"
            if button1.get() != "IP Address":
                button2['text'] = "Store Number"
    textdaemon = startasthread.T(target=updatetext, args=[prefix, storetxt])
    textdaemon.setDaemon(True)
    textdaemon.start()

    root.mainloop()

