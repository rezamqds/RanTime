import time
# no func or any library except time ;)
def rand(u=10):
    #random choose
    # r = time.monotonic_ns()
    # random less than 10 
    # its easy and have no cond becaz its just ine digit and no need to check it

    if u == 0:
        return "zero doesnt have any random!"

    elif u < 0 :
        res = rand(-u)
        return -res

    elif 0 < u <= 1:
        # return (r%10)*0.02
        while True:
            r = (time.monotonic_ns()%100) / 10
            r *= time.monotonic_ns()%10
            if 0 < r < 1 :
                return (r)
                break

    elif u<=10:
        while True:
            r = time.monotonic_ns()%100
            if r <= u :
                return (r)
                break

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
        cdev2=c//2
        # print(Dlen)
        # Dlen: use it for times that should mul the num in 10

        """while True:
            count = 0
            r = time.monotonic_ns()%Dlen
            count = count + 1
            if count > 25:
                r = rand(pow(10, cdev2)*rand(pow(10, cdev2)))
            print(f"{count} : its not the res: {r}")
            if r <= u :
                return (r)
                break"""
        
        for itter in range(50):
            r = time.monotonic_ns()%Dlen
            time.sleep(0.005)
            # print(f"{itter} : its not the res: {r}")
            if r <= u :
                return (r)
                break
        return u//rand(100)

# print(rand(45))


# user input :
while True:
    try:
        randinput = float(input("Pls input max rand: "))
        print("\t\t\trand : ",rand(randinput),"\n")
    except:
        print("if you wanna close me use Alt+F4 xD\n")
