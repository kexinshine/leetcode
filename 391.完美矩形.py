#
# @lc app=leetcode.cn id=391 lang=python3
#
# [391] 完美矩形
#

# @lc code=start
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        min_left=rectangles[0][0]
        min_down=rectangles[0][1]
        max_right=rectangles[0][2]
        max_up=rectangles[0][3]
        demo=collections.defaultdict(int)
        for r in rectangles:
            min_left = min(min_left,r[0])
            min_down = min(min_down,r[1])
            max_right = max(max_right,r[2])
            max_up = max(max_up,r[3])
            for i in range(r[0],r[2]):
                for j in range(r[1],r[3]):
                    demo[(i,j)]+=1
        for i in range(min_left,max_right):
            for j in range(min_down,max_up):
                if demo[(i,j)]==0 or demo[(i,j)]>1:
                    return False
        return True
# @lc code=end

