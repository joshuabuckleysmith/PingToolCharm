from time import sleep
def printer(monitoredthread, store, prefix):
    outputstring = ""
    pingcount = 0
    sleep(1)
    while True:
        sleep(0.05)
        openfile = open("1\\temp{}.txt".format(store), 'r')
        openstring = str(openfile.read())
        if openstring == "Ping request could not find host {}{}. " \
                         "Please check the name and try again.\n".format(prefix, store):
            print(
                "Ping request could not find host {}{}. Is your prefix correct? "
                "Please start ping again when ready.\n".format(
                    prefix, store))
            openfile.close()
            break
        len1 = len(openstring)
        len2 = len(outputstring)
        if len1 > len2:
            outputstring = openstring
            len3 = (len(outputstring.split('\n')))
            outsplit = outputstring.splitlines()[len3 - 2]
            if outsplit[0] != " ":
                print("{} {}".format((pingcount + 1), outputstring.splitlines()[len3 - 2]))
            if outsplit[0] == " ":
                print("{} {}".format((pingcount + 1), outputstring.splitlines()[len3 - 7]))
            pingcount = pingcount + 1
        th1 = monitoredthread.poll()
        if th1 != None:
            if (outputstring.splitlines()[len3 - 5][0:6])=="Ping s":
                try:
                    print("\n")
                    print(outputstring.splitlines()[len3 - 5])
                    print(outputstring.splitlines()[len3 - 4])
                    print(outputstring.splitlines()[len3 - 3])
                    print(outputstring.splitlines()[len3 - 2])
                    print('\n')
                except:
                    print("nothing to print")
            openfile.close()
            sleep(0.05)
            break
