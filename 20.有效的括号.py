#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        list_stack=list()
        stack_index=-1
        for i in range(len(s)):
            list_stack.append(s[i])
            stack_index+=1
            if stack_index>=1 and ((list_stack[stack_index]==')' and list_stack[stack_index-1]=='(')
            or (list_stack[stack_index]==']' and list_stack[stack_index-1]=='[')
            or (list_stack[stack_index]=='}' and list_stack[stack_index-1]=='{')
            ):
                list_stack.pop(stack_index)
                list_stack.pop(stack_index-1)
                stack_index-=2
                
                
        if list_stack:
            return False
        return True

# @lc code=end

