from collections import deque
from itertools import groupby, chain
from copy import deepcopy

class Board:
    def __init__(self, size, board):
        self.size = size
        self.board = board
        for x in board:
            print(x)
        print()

    # 왼 -> 오
    def rotated_board(self, board):
        board = board[:]
        board.reverse()
        return [
            [x[idx] for x in board] 
            for idx in range(self.size)
        ]

    # 오 -> 왼
    def reverse_rotated_board(self, board):
        return [
            [x[-idx - 1] for x in board]
            for idx in range(self.size)
        ]

    def up(self):
        new_board = []
        for line in self.reverse_rotated_board(self.board):
            new_board.append(self.move(line))

        return Board(self.size, self.rotated_board(new_board))

    def down(self):
        new_board = []
        for line in self.rotated_board(self.board):
            new_board.append(self.move(line))

        return Board(self.size, self.reverse_rotated_board(new_board))


    def left(self):
        new_board = []
        for line in self.board:
            new_board.append(self.move(line))
        return Board(self.size, new_board)

    def right(self): 
        new_board = []
        for line in self.board:
            line.reverse()
            new_board.append(self.move(line))
        for line in new_board:
            line.reverse()
        return Board(self.size, new_board)

    def move(self, line):
        groups = []
        for v, group in groupby(filter(lambda x: True if x != 0 else False, line)):
            group = list(group)
            if len(group) >=2:
                groups += [v * 2] + [v] * (len(group) - 2)
            else:
                groups += list(group)
        groups = groups + [0] * (self.size - len(groups))
        return groups

def get_max(board, cnt=0):
    if cnt > 5:
        return max(chain.from_iterable(board.board))
        
    print(f'\n{cnt} up')
    up = get_max(board.up(), cnt + 1)
    print(f'\n{cnt} down')
    down = get_max(board.down(), cnt + 1)
    print(f'\n{cnt} left')
    left = get_max(board.left(), cnt + 1)
    print(f'\n{cnt} right')
    right = get_max(board.right(), cnt + 1)

    return max(up, down, left, right)

def solve():
    board = []
    size = int(input())
    for x in range(size):
        board.append(
            [int(x) for x in input().split()]
        )
    print(get_max(Board(size, board)))

solve()