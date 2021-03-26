#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.son={}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree=self.son
        for a in word:
            if a not in tree:
                tree[a]={}
            tree=tree[a]
        tree['#']='#'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.startsWith(word+'#')


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.son
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

