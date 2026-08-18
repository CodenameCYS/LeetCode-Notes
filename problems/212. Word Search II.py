'''
=== 212. Word Search II ===

Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:
    Input: 
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]
 
Note:
    1. All inputs are consist of lowercase letters a-z.
    2. The values of words are distinct.
'''
class Trie:
    def __init__(self, words):
        self.trie = {}
        for word in words:
            self.add(word)
            
    def add(self, word):
        trie = self.trie
        for c in word:
            trie = trie.setdefault(c, {})
        trie["eos"] = "eos"
        
    def find(self, word, mode="full"):
        trie = self.trie
        for c in word:
            if c not in trie:
                return False
            trie = trie[c]
        if mode != "full":
            return True
        else:
            return "eos" in trie
# === 632ms(17.22%) && 28.3MB(65.08%) === #
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        have_visited = set()
        ans = set()
        stack = []
        n = len(board)
        m = len(board[0])
        trie = Trie(words)
        
        def dfs(row, col):
            nonlocal stack, have_visited, ans
            stack.append(board[row][col])
            have_visited.add((row, col))
            if not trie.find(stack, mode='half'):
                stack.pop()
                have_visited.remove((row, col))
                return
            if trie.find(stack, mode='full'):
                ans.add(''.join(stack))
            if row-1 >= 0 and (row-1, col) not in have_visited:
                dfs(row-1, col)
            if row+1 < n and (row+1, col) not in have_visited:
                dfs(row+1, col)
            if col-1 >= 0 and (row, col-1) not in have_visited:
                dfs(row, col-1)
            if col+1 < m and (row, col+1) not in have_visited:
                dfs(row, col+1)
            stack.pop()
            have_visited.remove((row, col))
            return
        
        for i in range(n):
            for j in range(m):
                dfs(i, j)
        return list(ans)