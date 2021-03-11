#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans=0
        nums=set(nums)
        for i in nums:
            if i-1 not in nums:
                temp=1
                start=i+1
                while start in nums:
                    temp+=1
                    start+=1
                
                ans=max(temp,ans)
        return ans

# @lc code=end

