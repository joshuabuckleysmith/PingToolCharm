from datetime import datetime




logfile = "log.txt"
file = open(logfile, "a")
file.write("**********************")
file.write("Application Launched\n")



class Log:
    def __init__(self):
        self.log = "Log Start"
        self.logoutput = ""
        self.logline = ""

    def readlog(self):
        a = self.logoutput
        self.logoutput = ""
        if a == "":
            return False
        return a

    def writelogline(self, logstr):
        self.logoutput = self.logoutput + "\n" + (str(datetime.utcnow())) + "  |  "
        self.logoutput = self.logoutput + logstr
        self.log = self.log + self.logoutput



log=Log()

log.writelogline("bar")
log.writelogline("fat")
print(log.readlog())
