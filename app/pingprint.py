import re
def pingprint(openfile):
    sent_total = 0
    received_total = 0
    lost_total = 0
    loss_total = 0
    maximum_total = 0
    minimum_total = 100000000
    average_total = 0
    openstring = str(openfile.read())
    print('openfile is {} and open string is {}'.format(openfile, openstring))
    pingcount = (len(openstring.split('\n')))
    pingcount = pingcount - 3
    print('pingcount is {}'.format(pingcount))
    try:
        ipadd = re.compile('(?<=Pinging )[0-9]+.[0-9]+.[0-9]+.[0-9]+')
        ipadd = ((ipadd.search(openstring).group(0)))
        print('ip address is {}'.format(ipadd))
    except:
        ipadd = "none"
        print('ipadd not found')
    try:
        # sent = re.compile('(?<=Sent = )[0-9]')
        # sent = ((sent.search(openstring).group(0)))
        sent = pingcount
        print('sent was found it is {}'.format(sent))
    except:
        sent = "0"
        print('sent was not found, it is now {}'.format(sent))
    try:
        print('received before search string {}'.format(openstring))
        received = re.compile('(?<=Reply from )')
        received = ((received.findall(openstring)))
        received = len(received)
        print('received {}'.format(received))
    except:
        received = "0"
        print('received was not found, it is {}'.format(received))
    try:
        lost = sent - received
    except:
        lost = "0"
        print('lost was {}'.format(lost))
    try:
        times = re.compile('(?<=time.)[0-9]*')
        print('times before search {} and string {}'.format(times, openstring))
        times = ((times.findall(openstring)))
        print('times {}'.format(times))
        maxtime = max(times)
        mintime = min(times)
        timesints = []
        for time in times:
            timesints.append(int(time))
        if len(timesints) == 0:
            timesints.append(0)
        sumtime = sum(timesints)
        lentime = len(timesints)
        avetime = int(sumtime / lentime)
        print('max {} min {} average {}'.format(maxtime, mintime, avetime))
    except:
        raise
    try:
        minimum = re.compile('(?<=Minimum = )[0-9]*')
        minimum = ((minimum.search(openstring).group(0)))
    except:
        minimum = "0"
    try:
        maximum = re.compile('(?<=Maximum = )[0-9]*')
        maximum = ((maximum.search(openstring).group(0)))
    except:
        maximum = "0"
    try:
        average = re.compile('(?<=Average = )[0-9]*')
        average = ((average.search(openstring).group(0)))
    except:
        average = "0"
    sent_total += int(sent)
    received_total += int(received)
    lost_total += int(lost)
    if maximum_total < int(maximum):
        maximum_total = int(maximum)
    if minimum_total > int(minimum):
        minimum_total = int(minimum)
        average_total += int(average)
    try:
        loss_total = int(round(lost_total / sent_total * 100))
    except:
        loss_total = "0"
    try:
        average_total = int(round(average_total / sent_total, 0))
    except:
        average_total = "0"
    try:
        percentage_lost = (lost_total / sent_total * 100)
    except:
        percentage_lost = "0"
    print('\nPing Statistics: \n')
    print(
        'Ping statistics for {}:\nPackets: Sent = {}, Received = {}, Lost = {} ({}% loss),\nApproximate round trip times in milli-seconds:\nMinimum = {}ms, Maximum = {}ms, Average = {}ms'.format(
            ipadd, sent_total, received_total, lost_total, loss_total, maxtime, mintime, avetime))


