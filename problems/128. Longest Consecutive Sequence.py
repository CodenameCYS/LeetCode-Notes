'''
=== 128. Longest Consecutive Sequence ===

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.

Example:
    Input: [100, 4, 200, 1, 3, 2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''
class DSU:
    def __init__(self):
        self.dsu = {}
        
    def find(self, n):
        if n not in self.dsu:
            return None
        if n == self.dsu[n]:
            return n
        self.dsu[n] = self.find(self.dsu[n])
        return self.dsu[n]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr is None or yr is None:
            return
        self.dsu[yr] = xr
        return
    
    def add(self, n):
        if n not in self.dsu:
            self.dsu[n] = n
        return
# === 80ms(32.58%) && 22.3MB(5.03%) === #
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        dsu = DSU()
        nums = list(set(nums))
        for n in nums:
            dsu.add(n)
            dsu.union(n, n-1)
            dsu.union(n, n+1)
        counter = defaultdict(int)
        for n in nums:
            counter[dsu.find(n)] += 1
        return max(counter.values())
                
        