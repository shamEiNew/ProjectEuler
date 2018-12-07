import time
def collatz_seq():
    i = 1
    maxL = 0
    position = 0
    while i != 1000000:
        n = i
        j=0
        while n != 1:
            if n % 2 ==0:
                n = n/2
                j = j + 1
            else:
                n = 3*n + 1
                j = j + 1
            if maxL < j:
                maxL = j
                position = i
        i = i+1
    return maxL,position
start_time = time.time()
print(collatz_seq())
print(time.time()-start_time)