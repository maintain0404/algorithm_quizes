from itertools import groupby

def solution():
    data = sorted(input(), reverse=True)
    odd = None
    ret = ''
    for key, group in groupby(data):
        str_group = ''.join(group)
        str_cnt = len(str_group)
        if str_cnt % 2 == 1:
            if odd:
                print('I\'m Sorry Hansoo')
                return
            else:
                odd = str_group[0]
        ret = f'{str_group[0:str_cnt//2]}{ret}'
    if odd:
        print(f'{ret}{odd}{"".join(reversed(ret))}')
    else:
        print(f'{ret}{"".join(reversed(ret))}')

solution()