#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
            max_size=0
            len_l=len(height)
            left=0
            right=len_l-1
            while True:
                if left==right:
                    break
                if height[left]<height[right]:
                    now_size=(right-left)*height[left]
                    max_size=max(max_size,now_size)
                    left+=1
                else:
                    now_size=(right-left)*height[right]
                    max_size=max(max_size,now_size)
                    right-=1
            return max_size




# @lc code=end

