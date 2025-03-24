class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str):
        curr = self.node
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endOfWord = True

    def search(self, s: str, i: int, memo: dict):
        if i == len(s):
            return True
        if i in memo:
            return memo[i]
        
        curr = self.node
        for idx in range(i, len(s)):
            if s[idx] not in curr.children:
                break
            
            curr = curr.children[s[idx]]
            if curr.endOfWord and self.search(s, idx + 1, memo):
                memo[i] = True
                return True

        memo[i] = False
        return False
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        return trie.search(s, 0, {})

