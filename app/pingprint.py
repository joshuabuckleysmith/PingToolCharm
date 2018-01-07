import re

def pingprint(openfile, store):
    sent_total = 0
    received_total = 0
    lost_total = 0
    openstring = str(openfile.read())
    pingcount = (len(openstring.split('\n')))
    pingcount = pingcount - 3
    try:
        sent = pingcount
    except:
        sent = "0"
    try:
        received = re.compile('(?<=Reply from )')
        received = ((received.findall(openstring)))
        received = len(received)
    except:
        received = "0"
    try:
        lost = sent - received
    except:
        lost = "0"
    try:
        times = re.compile('(?<=time.)[0-9]*')
        times = ((times.findall(openstring)))
        timesints = []
        try:
            for time in times:
                timesints.append(int(time))
        except:
            raise
        if len(times) < 1:
            timesints.append(0)
            timesints.append(0)
            timesints.append(0)
        maxtime = max(timesints)
        mintime = min(timesints)
        sumtime = sum(timesints)
        lentime = len(timesints)
        avetime = int(sumtime / lentime)
    except:
        raise
    sent_total += int(sent)
    received_total += int(received)
    lost_total += int(lost)
    try:
        loss_total = int(round(lost_total / sent_total * 100))
    except:
        loss_total = "0"
    print(
        '\nPing statistics for {}:\nPackets: Sent = {}, Received = {}, Lost = {} ({}% loss),\nApproximate round trip times in milli-seconds:\nMinimum = {}ms, Maximum = {}ms, Average = {}ms'.format(
            store, sent_total, received_total, lost_total, loss_total, mintime, maxtime, avetime))
    print('\n')

