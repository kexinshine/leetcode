#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split(' ')
        index = 0
        for i in range(len(s_list)):
            index-=1
            if s_list[index] != '':
                return len(s_list[index])
        return 0
# @lc code=end

