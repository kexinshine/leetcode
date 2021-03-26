#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        i,j=m-1,0
        while i>-1 and j<n:
            if target>matrix[i][j]:
                j+=1
            elif target<matrix[i][j]:
                i-=1
            else:
                return True
        return False

        
# @lc code=end

