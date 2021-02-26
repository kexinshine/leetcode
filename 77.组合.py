#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = list()
        n_list=list()
        for i in range(n):
            n_list.append(i+1)
        per_list = itertools.combinations(n_list, k)
        for per in per_list:
            temp_list=list()
            for p in per:
                temp_list.append(int(p))
            ans.append(temp_list)
        return ans

# @lc code=end

