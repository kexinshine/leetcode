#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        word_dict={
            "2":['a','b','c'],
            "3":['d','e','f'],
            "4":['g','h','i'],
            "5":['j','k','l'],
            "6":['m','n','o'],
            "7":['p','q','r','s'],
            "8":['t','u','v'],
            "9":['w','x','y','z']
        }
        word_lists=list()
        if len(digits)==0:
            return []
        for i in range(len(digits)):
            word_lists.append(word_dict.get(digits[i]))
        fn = lambda x: reduce(lambda x, y: [str(i)+str(j) for i in x for j in y], x)
        return fn(word_lists)

        
# @lc code=end

