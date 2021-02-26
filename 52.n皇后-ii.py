#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        s = '.'*n
        trace = [s]*n
        self.backtrace(trace, 0)  
        return len(self.res)
    def __init__(self):
        self.res = []
    def isvalidqueen(self, trace: List[str], row: int, col: int) -> bool:
        nLen = len(trace)
        # 列
        for item in trace:
            if item[col] == 'Q' :
                return False
        # 右上
        for i,j in zip(range(row-1, -1, -1), range(col+1, nLen)):
             if(trace[i][j] == 'Q'):
                return False
        # 左上
        for i,j in zip(range(row-1,-1,-1), range(col-1, -1, -1)):
            if(trace[i][j] == 'Q'):
                return False
        return True
    def replacechar(self, string:str, idx:int, char: str)-> str:
        strList = list(string)
        strList[idx] = char
        s = ''.join(strList)
        return s
    def backtrace(self, trace: List[str], row: int):
        # 停止条件
        if(len(trace) == row):
            ret = list(trace)
            self.res.append(ret)
            return
        for col in range(len(trace)):
            if(not self.isvalidqueen(trace, row, col)):
                continue
            trace[row] = self.replacechar(trace[row],col,'Q')
            self.backtrace(trace, row+1)
            trace[row] = self.replacechar(trace[row],col,'.')
# @lc code=end

