def killthread(buttondis, buttonen):
    #should disable cancel and enable ping
    buttondis['state'] = 'disabled'
    buttonen['state'] = 'normal'
    global pingcomponents
    process = pingcomponents["process"]
    store = pingcomponents["store"]
    try:
        storeip = IP(store)
    except:
        storeip = store
    if storeip != store:
        store = store.zfill(5)
    else:
        store = storeip
    # print("store is {}".format(store))
    # print("pid is {} ".format(process))
    os.system("TASKKILL /F /PID {} /T".format(process))
    # os.system("TASKKILL /F /PID {} /T > nul".format(process))
    openfile = open("temp{}.txt".format(store), 'r')
    pingprint(openfile)

