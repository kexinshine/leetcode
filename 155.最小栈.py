#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack=[]
        self.ans=[]
    def push(self, val: int) -> None:
        self.min_stack.append(val)
        if not self.ans:
            self.ans.append(val)
        else:
            self.ans.append(min(val,self.ans[-1]))
    def pop(self) -> None:
        self.min_stack.pop()
        self.ans.pop()
    def top(self) -> int:
        return self.min_stack[-1]
    def getMin(self) -> int:
        return self.ans[-1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

