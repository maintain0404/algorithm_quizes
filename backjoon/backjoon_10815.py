import sys 
from functools import reduce, lru_cache

read = sys.stdin.readline

def search(list_, num):
    idx_start = 0
    idx_end = len(list_) - 1
    while idx_start <= idx_end:
        idx = (idx_end + idx_start) // 2
        # print(f'{idx_start}, {idx}, {idx_end}')
        if list_[idx] == num:
            return 1
        elif list_[idx] < num:
            idx_start = idx + 1
        elif list_[idx] > num:
            idx_end = idx - 1
    return 0

def solve():
    cnt_has = int(read())
    card_has = sorted([int(x) for x in read().split()])
    cnt_2check = int(read())
    card_2check = [int(x) for x in read().split()]
    for x in card_2check:
        print(search(card_has, x), end=' ')
    print()
    # def is_in(reduced, num):
    #     nonlocal card_has
    #     return f'{reduced} {search(card_has, num)}'

    # return reduce(is_in, card_2check, '')
#print(solve())
solve()