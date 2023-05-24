import time



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
            #ended with succes :)
    
    elif u<=1000:
        while True:
            r = time.monotonic_ns()%1000
            if r <= u :
                return (r)
                break
    else:
        # if more than 1000 we should count the digit len
        # digit count with logic
        """c = 0
        nu = u
        while nu > 0:
            c += 1
            nu //= 10
        print(c)"""
        # also with this method:
        c = (len(str(u)))
        Dlen = 
        while True:
            r = time.monotonic_ns()%1000
            if r <= u :
                return (r)
                break

rand(15684645)

# # test area ...
# while True:
#     test = rand(730)
#     if test <= 730:
#         print("Success! --> ", test)
#     else:
#         print("noway!xD")
#         break
