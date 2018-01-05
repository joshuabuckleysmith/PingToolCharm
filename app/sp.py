from app import startasthread, startping
def sp(a, b, c, d, e, f, g, h, i):
    '''store.get(), test.get(), pingnumber.get(), ping, cancelping, prefix.get(), options, storetxt'''
    i["store"] = a
    i["test"] = b
    i["pingnumber"] = c
    i["prefix"] = g
    startasthread(startping(a, b, c, d, e, f, g, h, i))