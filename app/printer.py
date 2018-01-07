from time import sleep
def printer(monitoredthread, store, prefix):
    outputstring = ""
    pingcount = 0
    sleep(1)
    while True:
        sleep(0.05)
        openfile = open("1\\temp{}.txt".format(store), 'r')
        openstring = str(openfile.read())
        if openstring == "Ping request could not find host {}{}. Please check the name and try again.\n".format(prefix,
                                                                                                                store):
            print(
                "Ping request could not find host {}{}. Is your prefix correct? Please start ping again when ready.\n".format(
                    prefix, store))
            openfile.close()
            break
        len1 = len(openstring)
        len2 = len(outputstring)
        # print("len 1 is {}".format(len1))
        # print("len 2 is {}".format(len2))
        if len1 > len2:
            outputstring = openstring
            len3 = (len(outputstring.split('\n')))
            # if pingcount > 0:
            # print("{} pings sent".format(pingcount))
            outsplit = outputstring.splitlines()[len3 - 2]
            if outsplit[0] != " ":
                print("{} {}".format((pingcount + 1), outputstring.splitlines()[len3 - 2]))
            if outsplit[0] == " ":
                print("{} {}".format((pingcount + 1), outputstring.splitlines()[len3 - 7]))
                # print("{} pings sent".format(pingcount+1))
            # print(outputstring)
            pingcount = pingcount + 1
        # print("moni thread{}".format(monitoredthread.poll()))
        th1 = monitoredthread.poll()
        # print("TH1 {}".format(th1))
        if th1 != None:
            # print("monitoredthread.poll() was {}".format(monitoredthread.poll()))
            # print("lines = {}".format(len(outputstring.split('\n'))))
            if (outputstring.splitlines()[len3 - 5][0:6])=="Ping s":
                try:
                    print("\n")
                    print(outputstring.splitlines()[len3 - 5])
                    print(outputstring.splitlines()[len3 - 4])
                    print(outputstring.splitlines()[len3 - 3])
                    print(outputstring.splitlines()[len3 - 2])
                    print('\n')
                    print('\n')

                except:
                    print("nothing to print")
            openfile.close()
            # print("output file closed")
            sleep(0.05)
            break
