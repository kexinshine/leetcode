#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        str_num=str(num)
        len_num=len(str_num)
        s=''
        hundred_dict={
            '0':'',
            '1':'C',
            '2':'CC',
            '3':'CCC',
            '4':'CD',
            '5':'D',
            '6':'DC',
            '7':'DCC',
            '8':'DCCC',
            '9':'CM'
        }
        ten_dict={
            '0':'',
            '1':'X',
            '2':'XX',
            '3':'XXX',
            '4':'XL',
            '5':'L',
            '6':'LX',
            '7':'LXX',
            '8':'LXXX',
            '9':'XC'
        }
        unit_dict={
            '0':'',
            '1':'I',
            '2':'II',
            '3':'III',
            '4':'IV',
            '5':'V',
            '6':'VI',
            '7':'VII',
            '8':'VIII',
            '9':'IX'
        }
        for i in str_num:
            if len_num==4:
                s=s+('M'*int(i))
            elif len_num==3:
                s=s+(hundred_dict.get(i))
            elif len_num==2:
                s=s+(ten_dict.get(i))
            else:
                s=s+(unit_dict.get(i))
            len_num-=1
        return s



# @lc code=end

