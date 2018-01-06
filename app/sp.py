from app import startasthread, startping, pingcomponents
def sp(a, b, c, d, e, f, g, h):
    '''a store.get(), b test.get(), c pingnumber.get(), d ping, e cancelping, f prefix.get(), g options, h storetxt'''
    pingcomponents.pingcomponents["store"] = a
    pingcomponents.pingcomponents["test"] = b
    pingcomponents.pingcomponents["pingnumber"] = c
    pingcomponents.pingcomponents["prefix"] = f
    startasthread.startasthread(startping.startping(a, b, c, d, e, f, g, h))