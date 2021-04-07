import math
from time import sleep
from copy import copy

def get_available(L, W, H, A):
    ret = (L // A) * (W // A) * (H // A)
    return ret

def minus_little(A, N):
    return (A + N) / 2

def solution():
    N, L, W, H = map(int, input().split())
    A = max(L, W, H)
    # 
    while temp := get_available(L, W, H, A) <= N:
        A = A / 2
        print(A)
    
    m = copy(A) / 2
    print('hi')
    while not (temp := math.isclose(get_available(L, W, H, A), N)):
        if temp <= N:
            A += m
        else:
            A -= m
        m = m / 2
        sleep(1)
        print(A)

    while (temp := math.isclose(get_available(L, W, H, A), N)):
        if temp <= N:
            A += m
        else:
            A -= m
        m = m / 2
        sleep(1)
        print(A)
    print(A)
solution()