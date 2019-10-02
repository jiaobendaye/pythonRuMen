# coding: utf-8

from typing import List
"""
二叉树与数组， 二叉堆与优先队列
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
  / \
 8   9

    3
   /  \
  6    9
 / \
12  15
push 2
    2
   /  \
  6    3
 / \   /
12  15 9
pop

[0,1,2,3,4,  5,6,7,8,9]
[0,3,6,9,12,15  ]
[0,3,6,9,12,15,2  ] push 2
[0,3,6,2,12,15,9  ] _swim
[0,2,6,3,12,15,9  ] _swim
[0, ,6,3,12,15,9  ] pop
[0,3,6,9,12,15  ] _sink
[0,3,6,9,12,15  ]
[0,3,6,9,12,15  ]

n
2n 2n+1

n/2

"""


class PQHeap:
    arr: List[int] = [None]
    N: int = 0

    def push(self, num: int):
        self.arr.append(num)
        self.N += 1
        self._swim(self.N)

    def _swim(self, k: int):
        knum = self.arr[k]
        while k > 1:
            ppos = k // 2
            pnum = self.arr[ppos]
            if knum < pnum:
                self.arr[k] = pnum
                k = ppos
            else:
                break
        self.arr[k] = knum
    def _sink(self, k:int):
        knum = self.arr[k]
        while k * 2 < self.N:
            leftpos  = k * 2
            miner_pos = leftpos
            if leftpos < self.N:
                rightpos = leftpos + 1
                if self.arr[rightpos] < self.arr[leftpos]:
                    miner_pos = rightpos
            
            child_num = self.arr[miner_pos]
            if child_num < knum:
                self.arr[miner_pos] = knum
                self.arr[k] = child_num
                k = miner_pos
            else:
                break
    
    def pop(self):
        self.N -=1
        last = self.arr.pop()
        if self.N > 0:
            min_value = self.arr[1]
            self.arr[1] = last
            self._sink(1)
            return min_value
        else:
            return last 

    def min(self):
        if self.N > 0:
            return self.arr[1]
def test_my_heap():
    h = PQHeap()
    h.push(3)
    assert h.min() == 3
    h.push(6)
    assert h.min() == 3
    h.push(7)
    assert h.min() == 3
    h.push(9)
    assert h.min() == 3
    h.push(231)
    assert h.min() == 3
    h.push(2)
    assert h.min() == 2
    h.pop()
    assert h.min() == 3
    h.pop()
    assert h.min() == 6
