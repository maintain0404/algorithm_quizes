import sys
from collections import deque

dq = deque()

def front():
    global dq
    v = dq.popleft()
    dq.appendleft(v)
    return v

def back():
    global dq
    v = dq.pop()
    dq.append(v)
    return v

cmd_dict = {
    'push_back': dq.append,
    'push_front': dq.appendleft,
    'pop_front': dq.popleft,
    'pop_back': dq.pop,
    'size': lambda: len(dq),
    'empty': lambda: 0 if len(dq) else 1,
    'front': front,
    'back': back,
}


cnt = int(sys.stdin.readline())

for i in range(cnt):
    commands = sys.stdin.readline().split()
    try:
        if commands[0] in ('push_back', 'push_front'):
            cmd_dict[commands[0]](int(commands[1]))
        elif commands[0] in ('pop_front', 'pop_back'):
            print(cmd_dict[commands[0]]())
        else:
            print(cmd_dict[commands[0]]())
    except IndexError:
        print('-1')