
def coroutine(fn):
    def wrapped(*args,**kwargs):
        gen = fn(*args,**kwargs)
        next(gen)
        return gen
    return wrapped

@coroutine
def pendulum(finish):
    yield
    step, i = 1, 0
    while True:
        yield i
        i += step
        if i<=0:
            step = 1
        elif i>=finish:
            step = -1
#         if i<=0 or i>=finish:
#             step = -step

if __name__=="__main__":
    num=1
    pendulum_generator = pendulum(5)
    for i in pendulum_generator:
        print(str(i),end=",")
        num += 1
        if num > 100:
            break
