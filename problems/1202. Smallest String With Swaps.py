'''
=== 1202. Smallest String With Swaps ===

You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
You can swap the characters at any pair of indices in the given pairs any number of times.
Return the lexicographically smallest string that s can be changed to after using the swaps.

Example 1:
    Input: s = "dcab", pairs = [[0,3],[1,2]]
    Output: "bacd"
    Explaination: 
    Swap s[0] and s[3], s = "bcad"
    Swap s[1] and s[2], s = "bacd"
Example 2:
    Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
    Output: "abcd"
    Explaination: 
    Swap s[0] and s[3], s = "bcad"
    Swap s[0] and s[2], s = "acbd"
    Swap s[1] and s[2], s = "abcd"
Example 3:
    Input: s = "cba", pairs = [[0,1],[1,2]]
    Output: "abc"
    Explaination: 
    Swap s[0] and s[1], s = "bca"
    Swap s[1] and s[2], s = "bac"
    Swap s[0] and s[1], s = "abc"

Constraints:
    1. 1 <= s.length <= 10^5
    2. 0 <= pairs.length <= 10^5
    3. 0 <= pairs[i][0], pairs[i][1] < s.length
    4. s only contains lower case English letters.
'''
class DSU:
    def __init__(self, n):
        self.dsu = [i for i in range(n)]
        
    def find(self, x):
        if x == self.dsu[x]:
            return x
        self.dsu[x] = self.find(self.dsu[x])
        return self.dsu[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.dsu[yr] = xr
        return
# === 1344ms(10.04%) && 50.6MB(43.41%) === #  
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        dsu = DSU(n)
        for x, y in pairs:
            dsu.union(x, y)
        groups = defaultdict(list)
        for i in range(n):
            key = dsu.find(i)
            groups[key].append(s[i])
        for k in groups:
            groups[k] = sorted(groups[k])
        ans = []
        for i in range(n):
            key = dsu.find(i)
            ans.append(groups[key].pop(0))
        return "".join(ans)
        