#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFindSet()
        for i in range(n):
            uf.add(i)
            for j in range(i):
                if isConnected[i][j]:
                    uf.merge(i, j)
        return uf.count


class UnionFindSet:
    def __init__(self):
        self.father = {}
        self.count = 0

    def find(self, x):
        root = x
        while self.father[root]!=None:
            root = self.father[root]

        while x != root:
            temp = self.father[x]
            self.father[x] = root
            x = temp
        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.count -= 1

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.count += 1

# @lc code=end

