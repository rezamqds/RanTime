import time, numpy 

# x = time.monotonic_ns()
# print(x)
# print(x%10)




def rand(u=10):
    #random choose
    r = time.monotonic_ns()
    # random less than 10 
    # its easy and have no cond becaz its just ine digit and no need to check it
    if u<=10:
        return (r%10)

    # for less than 100 must check two digit, it should be less than 100 or equal and also be right before choosen number
    elif u<=100:
        while True:
            r = time.monotonic_ns()%100
            if r <= u :
                return (r)
                break



        


while True:
    test = rand(73)
    if test <= 73:
        print("Success! --> ", test)
    else:
        print("noway!xD")
        break
