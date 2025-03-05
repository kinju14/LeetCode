class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.node = TrieNode()
    
    def addWord(self, word: str) -> None:
        curr = self.node

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            curr = node

            for i in range(idx, len(word)):
                ch = word[i]
                if ch.isalpha():
                    if ch not in curr.children:
                        return False
                    curr = curr.children[ch]

                else:
                    for child in curr.children.values():
                        if dfs(child, i+1):
                            return True
                    return False

            return curr.is_end_of_word

        return dfs(self.node, 0)
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
