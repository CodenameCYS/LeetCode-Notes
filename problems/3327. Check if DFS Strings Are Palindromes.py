'''
=== 3327. Check if DFS Strings Are Palindromes ===

You are given a tree rooted at node 0, consisting of n nodes numbered from 0 to n - 1. The tree is represented by an array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.
You are also given a string s of length n, where s[i] is the character assigned to node i.
Consider an empty string dfsStr, and define a recursive function dfs(int x) that takes a node x as a parameter and performs the following steps in order:
    - Iterate over each child y of x in increasing order of their numbers, and call dfs(y).
    - Add the character s[x] to the end of the string dfsStr.
Note that dfsStr is shared across all recursive calls of dfs.
You need to find a boolean array answer of size n, where for each index i from 0 to n - 1, you do the following:
    - Empty the string dfsStr and call dfs(i).
    - If the resulting string dfsStr is a palindrome, then set answer[i] to true. Otherwise, set answer[i] to false.
Return the array answer.
A palindrome is a string that reads the same forward and backward.

Example 1:
    Input: parent = [-1,0,0,1,1,2], s = "aababa"
    Output: [true,true,false,true,true,true]
    Explanation:
    Calling dfs(0) results in the string dfsStr = "abaaba", which is a palindrome.
    Calling dfs(1) results in the string dfsStr = "aba", which is a palindrome.
    Calling dfs(2) results in the string dfsStr = "ab", which is not a palindrome.
    Calling dfs(3) results in the string dfsStr = "a", which is a palindrome.
    Calling dfs(4) results in the string dfsStr = "b", which is a palindrome.
    Calling dfs(5) results in the string dfsStr = "a", which is a palindrome.
Example 2:
    Input: parent = [-1,0,0,0,0], s = "aabcb"
    Output: [true,true,true,true,true]
    Explanation:
    Every call on dfs(x) results in a palindrome string.

Constraints:
    1. n == parent.length == s.length
    2. 1 <= n <= 105
    3. 0 <= parent[i] <= n - 1 for all i >= 1.
    4. parent[0] == -1
    5. parent represents a valid tree.
    6. s consists only of lowercase English letters.
'''
# === 6643ms && 72.9MB === #
class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        if len(set(s)) == 1:
            return [True for _ in parent]
        
        n = len(parent)        
        graph = defaultdict(list)
        for i in range(n):
            graph[parent[i]].append(i)
        
        ans = [False for _ in range(n)]
        
        def dfs(root):
            nonlocal ans
            dfs_str = ""
            for u in graph[root]:
                dfs_str += dfs(u)
            dfs_str += s[root]
            n = len(dfs_str)
            ans[root] = (dfs_str == dfs_str[::-1])
            return dfs_str
        
        dfs(0)
        return ans