#
# @lc app=leetcode.cn id=554 lang=python3
#
# [554] 砖墙
#

# @lc code=start
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        m_map = {}
        for row in wall:
            m_sum = 0
            for i in range(len(row) - 1):
                m_sum += row[i]
                if m_sum in m_map:
                    # 我们在遍历同一行的时候不会遇到相同的 sum 两次。所以如果 sum 在遍历过程中遇到相同的值，说明一定存在别的行，并且当前 sum 也是那些行的衔接处（砖缝的位置）。所以对应的 count 值需要加一。
                    m_map[m_sum] += 1
                else:
                    # 如果这个 sum 在 map 中没有出现过，我们创建一个初始 count 值为 1 的相应条目，表示【有一行砖头在当前sum出现了砖缝】。
                    m_map[m_sum] = 1
        res = len(wall)
        for m_sum in m_map:
            # 墙的总行数 - 当前m_sum穿过的砖缝行数 = 当前m_sum穿过的砖块数
            res = min(res, len(wall) - m_map[m_sum])
        return res
        
# @lc code=end

