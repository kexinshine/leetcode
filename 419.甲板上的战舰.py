#
# @lc app=leetcode.cn id=419 lang=python3
#
# [419] 甲板上的战舰
#

# @lc code=start
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m=len(board)
        n=len(board[0])
        ans=0
        for i in range(m):
            for j in range(n):
                if board[i][j]=='X':
                    if (i==0 and j==0) or \
                        (i==0 and j>0 and board[i][j-1]=='.') or \
                        (i>0 and j==0 and board[i-1][j]=='.') or \
                        (i>0 and j>0 and board[i-1][j]=='.' and board[i][j-1]=='.'):
                        ans+=1
        return ans            
# @lc code=end

