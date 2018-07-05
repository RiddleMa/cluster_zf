import time, timeit
def clock(func):
    '''
    计时器
    :param func:
    :return:
    '''
    def clocked(*args):
        t0 = timeit.default_timer()
        result = func(*args)
        elapsed = timeit.default_timer() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        # print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        print('[%0.8fs] %s' % (elapsed, name))
        return result
    return clocked