#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_list=[[],[],[],[],[],[],[],[],[]]
        nine_list=[[],[],[],[],[],[],[],[],[]]
        row_index=0
        for row in board:
            row_index+=1
            i=0
            for column in column_list:
                column.append(row[i])
                i+=1
            if row_index<=3:
                flag=0
            elif row_index<=6:
                flag=3
            elif row_index<=9:
                flag=6
            j=0
            for nine in nine_list[flag:flag+3]:
                nine.append(row[j])
                nine.append(row[j+1])
                nine.append(row[j+2])
                j+=3
            row_count=defaultdict(int)
            for num in row:
                row_count[num]+=1
            len_dict=len(row_count)
            if 9-row_count['.']!=len_dict-1:
                return False
        for column in column_list:
            column_count=defaultdict(int)
            for num in column:
                column_count[num]+=1
            len_dict=len(column_count)
            if 9-column_count['.']!=len_dict-1:
                return False
        for nine in nine_list:
            nine_count=defaultdict(int)
            for num in nine:
                nine_count[num]+=1
            len_dict=len(nine_count)
            if 9-nine_count['.']!=len_dict-1:
                return False   
        return True
# @lc code=end

