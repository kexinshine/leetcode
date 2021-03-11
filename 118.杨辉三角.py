#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp=[]
        dp.append([1])
        dp.append([1,1])
        if numRows<=2:
            return dp[:numRows]
        for i in range(2,numRows):
            temp=[1]
            for j in range(1,i):
                temp.append(dp[i-1][j-1]+dp[i-1][j])
            temp.append(1)
            dp.append(temp)
        return dp
# @lc code=end

