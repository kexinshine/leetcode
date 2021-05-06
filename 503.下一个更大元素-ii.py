#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        n=len(nums)
        ans=[-1]*n
        for i in range(n):
            if not stack:
                stack.append(i)
                continue
            if nums[i]<=nums[stack[-1]]:
                stack.append(i)
                continue
            while stack and  nums[i]>nums[stack[-1]]:
                ans[stack.pop()]=nums[i]
            stack.append(i)    
        for i in range(n-1):
            while stack and nums[i]>nums[stack[-1]]:
                ans[stack.pop()]=nums[i]
        return ans

# @lc code=end

