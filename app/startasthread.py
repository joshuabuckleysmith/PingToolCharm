def startasthread(funct):
    thread = T(target=funct)
    thread.start()
