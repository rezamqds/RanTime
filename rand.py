import time, numpy 

# x = time.monotonic_ns()
# print(x)
# print(x%10)




def rand(u=10):
    r = time.monotonic_ns()
    if u<=10:
        print(r%10)
    elif u<=100:
        print(r%100)

        


rand()
