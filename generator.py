import time
from random import randint

def gen_crescent(N):
    L=[]
    for i in range(0,N,1):
        L.append(i + 17)
    return L

def gen_decreasing(N):
    L=[]
    for i in range(N,0, -1):
        L.append(i + 17)
    return L

def gen_random(N):
    L=[]
    for i in range(0,N,1):
        L.append(randint(0,N))
    return L

def now():
    return int(round(time.time() * 1000))

def dif_time(a, b):
    return a - b

