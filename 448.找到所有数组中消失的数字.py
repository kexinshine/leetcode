#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums=set(nums)
        ans=[]
        for i in range(1,n+1):
            if i not in nums:
                ans.append(i)
        return ans
        
# @lc code=end

