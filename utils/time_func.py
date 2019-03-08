import time                                                


def measure_time(f, cnt=10):
    def timed(*args, **kw):
        ts = time.clock()
        for i in range(cnt):
            result = f(*args, **kw)
        te = time.clock()
        print('%r %.2f msec' % (f.__name__, (te-ts)*1000))
        return result
    return timed