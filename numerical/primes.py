#from math import sqrt,floor
#import timeit
def isFactor(dividend,divisor):
    if(dividend%divisor==0):
        return True
    return False
    
def isPrime(n):
    for i in range (2,n//2+1): #floor(sqrt(n))+1 # //integer division or floor value
        if isFactor(n,i):
            return False
    return True
            
    
    
def genPrime(k):    
    primecounter=0
    seqcounter=2
    while primecounter<k:
        if isPrime(seqcounter):
            print(seqcounter, end=' ')
            primecounter+=1
        seqcounter+=1
#st=timeit.default_timer()
