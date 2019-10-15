# coding: utf-8

"""
为了装修新房，你需要加工一些长度为正整数的棒材 sticks。
如果要将长度分别为 X 和 Y 的两根棒材连接在一起，你需要支付 X + Y 的费用。
由于施工需要，你必须将所有棒材连接成一根。
返回你把所有棒材 sticks 连成一根所需要的最低费用。
注意你可以任意选择棒材连接的顺序。
示例：
input: sticks = [2, 4, 3]
output: 14
explain: 2 and 3 :cost 5;
         5 and 4 cost 9; 
         5 + 9 = 14
"""
from typing import List
from bisect import insort

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        sticks.sort()
        lo = 0
        cost = 0
        while lo + 1 < len(sticks):
            s1 = sticks[lo]
            s2 = sticks[lo+1]
            stick = s1 + s2
            lo +=2
            insort(sticks, stick, lo) 
            cost += stick
        return cost
        
def test():
    s = Solution()
    assert s.connectSticks(sticks=[2, 4, 3]) == 14
    assert s.connectSticks(sticks=[1, 8, 3, 5]) == 30
if __name__ == "__main__":
    test()