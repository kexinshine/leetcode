#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_m=len(matrix)
        a=matrix
        b=self.trans(a)
        for i in range(len_m):
            matrix[i]=b[i]
    def trans(self, m):
        a = [[] for i in m[0]]
        for i in m:
            for j in range(len(i)):
                a[j].append(i[j])
        b=[]
        for i in a:
            b.append(list(reversed(i)))
        return b
# @lc code=end

