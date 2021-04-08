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

    def set_lr(self, left, right):
        self.left = left
        self.right = right

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

    # TODO: 한 루프에서 다 하도록 고쳐야함
    counter = 0
    dq = deque((nodes[root], ))
    try:
        while node := dq.popleft():
            counter += 1
            if node.left == 0:
                node.left = counter
                to_extendleft = sorted(filterfalse(
                    lambda x: x.left, node.connected_node
                ), reverse=True)
                if to_extendleft:
                    dq.appendleft(node)
                    dq.extendleft(to_extendleft)
                else:
                    node.right = (counter := counter + 1)
            elif node.right == 0:
                node.right = counter
    except IndexError:
        pass

    for n in range(1, N + 1):
        print(nodes[n])

solution()