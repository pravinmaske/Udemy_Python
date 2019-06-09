import time
import sys

def calc(a):
    for i in range(10000000):
        2*a
        #pass

start=time.perf_counter()
calc(2**100000)
end=time.perf_counter()

print('Time taken for calculation of 2**100000:',end-start)
