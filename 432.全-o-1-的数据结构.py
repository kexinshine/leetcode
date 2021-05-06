#
# @lc app=leetcode.cn id=432 lang=python3
#
# [432] 全 O(1) 的数据结构
#

# @lc code=start
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict=collections.defaultdict(int)
        self.max=''
        self.min=''
        self.max_value=0
        self.min_value=float('inf')


    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        self.dict[key]+=1
        if self.dict[key]>self.max_value:
            self.max_value=self.dict[key]
            self.max=key
        if self.dict[key]<self.min_value:
            self.min_value=self.dict[key]
            self.min=key


    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if self.dict[key]:
            if self.dict[key]==1:
                self.dict.remove(key)
            else:
                self.dict[key]-=1


    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return self.max

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return self.min


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end

