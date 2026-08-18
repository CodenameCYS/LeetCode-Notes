'''
=== 1980. Find Unique Binary String ===

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

Example 1:
    Input: nums = ["01","10"]
    Output: "11"
    Explanation: "11" does not appear in nums. "00" would also be correct.
Example 2:
    Input: nums = ["00","01"]
    Output: "11"
    Explanation: "11" does not appear in nums. "10" would also be correct.
Example 3:
    Input: nums = ["111","011","001"]
    Output: "101"
    Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
 
Constraints:
    1. n == nums.length
    2. 1 <= n <= 16
    3. nums[i].length == n
    4. nums[i] is either '0' or '1'.
'''
class Trie:
    def __init__(self, n):
        self.trie = {}
        self.length = n
        
    def add(self, s):
        trie = self.trie
        for c in s:
            trie = trie.setdefault(c, {})
        trie[c] = "eos"
        
    def get_another(self):
        
        def dfs(trie, k):
            if k == self.length:
                return "eos"
            if "0" not in trie:
                return "0" * (self.length - k)
            elif "1" not in trie:
                return "1" * (self.length - k)
            else:
                s1 = "0" + dfs(trie["0"], k+1)
                s2 = "1" + dfs(trie["1"], k+1)
                return s1 if len(s1) < len(s2) else s2
            
        return dfs(self.trie, 0)
            
# === 36ms && 14.5MB === #
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        trie = Trie(n)
        for s in nums:
            trie.add(s)
        return trie.get_another()