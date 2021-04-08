import sys
sys.setrecursionlimit(10**6)

cache_dict = {(1,i):i for i in range(1, 11)}
def asc_num(n, available):
    arg_tuple = (n, available,)
    if temp := cache_dict.get(arg_tuple):
        return temp
    else:
        cache_dict[arg_tuple] = sum(
            asc_num(n - 1, i) for i in range(1, available + 1)
        )
        return cache_dict[arg_tuple]

def solution():
    n = int(input())
    print(asc_num(n, 10) % 10007)

solution()