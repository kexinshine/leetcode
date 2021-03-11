#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex+=1
        dp=[]
        dp.append([1])
        dp.append([1,1])
        if rowIndex<=2:
            return dp[rowIndex-1]
        for i in range(2,rowIndex):
            temp=[1]
            for j in range(1,i):
                temp.append(dp[i-1][j-1]+dp[i-1][j])
            temp.append(1)
            dp.append(temp)
        return dp[rowIndex-1]
# @lc code=end

