def pendulum(finish):
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
    pend = pendulum(5)
    for _ in range(100):
        i = next(pend)
        print(i,end=",")
