import sys

def solution():
    for i in range(int(sys.stdin.readline())):
        rx, ry, rd, bx, by, bd = map(int, sys.stdin.readline().split())
        if rx == bx and ry == by:
            if rd == bd:
                print(-1)
            else:
                print(0)
            continue
        
        dist_pow2 = ((rx - bx) ** 2) + ((ry - by) ** 2)
        sum_pow2 = (rd + bd) ** 2
        sub_pow2 = (rd - bd) ** 2
        if dist_pow2 == sum_pow2:
            print(1)
        elif dist_pow2 > sum_pow2:
            print(0)
        elif dist_pow2 < sum_pow2:
            if dist_pow2 == sub_pow2:
                print(1)
            elif sub_pow2 < dist_pow2:
                print(2)
            elif sub_pow2 > dist_pow2:
                print(0)
            
solution()