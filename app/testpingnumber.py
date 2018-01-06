def testpingnumber(pingnumber):
    if pingnumber == "":
        # print('ping setup 333')
        return False
    try:
        int(pingnumber)
        # print('ping setup 11')
        return True
    except:
        # print('ping setup 12')
        return False
