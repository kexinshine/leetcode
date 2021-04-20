#
# @lc app=leetcode.cn id=403 lang=python3
#
# [403] 青蛙过河
#

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = {}
        dp[1] = [1]
        for s in stones[1:]:
            if s not in dp:
                continue
            for step in dp[s]:
                if step!=1:
                    if s + step - 1 not in dp:
                        dp[s + step - 1] = {step-1}
                    else:
                        dp[s + step - 1].add(step - 1)
                if step!=0:
                    if s + step not in dp:
                        dp[s + step] = {step}
                    else:
                        dp[s + step].add(step)
                if s + step + 1 not in dp:
                    dp[s + step + 1] = {step+1}
                else:
                    dp[s + step + 1].add(step + 1)
        if dp.get(stones[-1],None):
            return True
        return False
                

# @lc code=end

