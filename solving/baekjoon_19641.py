import sys
import operator
from itertools import filterfalse
from collections import deque

input = sys.stdin.readline

class Node:
    def __init__(self, number, connected_node):
        self.number = number
        self.connected_node = sorted(connected_node)
        self.left = 0
        self.right = 0

    def __str__(self):
        return f'{self.number} {self.left} {self.right}'

    def _operate(self, other, operator_):
        if isinstance(other, self.__class__):
            return operator_(self.number, other.number)
        else:
            return TypeError('Node must be compared with Node only')

    def __gt__(self, other):
        return self._operate(other, operator.gt)

    def __ge__(self, other):
        return self._operate(other, operator.ge)

    def __eq__(self, other):
        return self._operate(other, operator.eq)

    def __ne__(self, other):
        return self._operate(other, operator.ne)

    def __lt__(self, other):
        return self._operate(other, operator.lt)
        
    def __le__(self, other):
        return self._operate(other, operator.le)

def solution():
    # get inputs
    nodes = {}
    N = int(input())
    for _ in range(N):
        nums = [int(x) for x in input().split()]
        node_num, connected_node = nums[0], nums[1:-1]
        nodes[node_num] = Node(node_num, connected_node)

    for node in nodes.values():
        node.connected_node = [
            nodes[x] for x in node.connected_node
        ]

    root = int(input())

    # callculate left and right
    left_counter, right_counter = 0, N * 2 + 1
    dq = deque((nodes[root], ))
    try:
        while node := dq.popleft():
            print(node)
            node.left = (left_counter := left_counter + 1)
            if node.connected_node:
                temp = filterfalse(lambda x: x.left, sorted(node.connected_node, reverse=True))
                dq.extendleft(temp)
    except IndexError:
        pass

    dq = deque((nodes[root], ))
    try:
        while node := dq.pop():
            print(node)
            node.right = (right_counter := right_counter - 1)
            if node.connected_node:
                temp = filterfalse(lambda x: x.right, node.connected_node)
                dq.extend(temp)
    except IndexError:
        pass

    for n in range(1, N + 1):
        print(nodes[n])

solution()