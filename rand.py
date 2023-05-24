import time



def rand(u=10):
    #random choose
    r = time.monotonic_ns()
    # random less than 10 
    # its easy and have no cond becaz its just ine digit and no need to check it

    if u == 0:
        return "zero doesnt have any random!"

    if 0 < u < 1:
        # return (r%10)*0.02
        while True:
            r = (time.monotonic_ns()%100) / 10
            r *= time.monotonic_ns()%10
            if 0 < r < 1 :
                return (r)
                break

    elif u<=10:
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

        # we got the len and use it with .format and join for more greater numbers!
        Dlen = pow(10, c) 
        # print(Dlen)
        # Dlen: use it for times that should mul the num in 10
        while True:
            r = time.monotonic_ns()%Dlen
            if r <= u :
                return (r)
                break


print(rand(0.55))



# # test area ...
# while True:
#     test = rand(263)
#     if test <= 263:
#         print("Success! --> ", test)
#     else:
#         print("noway!xD")
#         break
