from itertools import product

def square_check(nums, x, y, i):
    if nums[x][y] == nums[x+i][y] == nums[x][y] == nums[x+i][y+i]:
        return i
    else:
        return 0

def solution():
    n, m = map(int, input().split(' '))
    nums = []
    for _ in range(n):
        nums.append(
            [int(x) for x in input()]
        )

    maximum = 0
    minofnm = min(n, m)
    for x, y in product(range(n), range(m)):
        for i in range(0, minofnm):
            if x + i < n and y + i < m:
                if (num := square_check(nums, x, y, i)) > maximum:
                    maximum = num
    
    print((maximum + 1) ** 2)

solution()