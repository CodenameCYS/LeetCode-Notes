'''
=== 2334. Subarray With Elements Greater Than Varying Threshold ===

You are given an integer array nums and an integer threshold.
Find any subarray of nums of length k such that every element in the subarray is greater than threshold / k.
Return the size of any such subarray. If there is no such subarray, return -1.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [1,3,4,3,1], threshold = 6
    Output: 3
    Explanation: The subarray [3,4,3] has a size of 3, and every element is greater than 6 / 3 = 2.
    Note that this is the only valid subarray.
Example 2:
    Input: nums = [6,5,6,5,8], threshold = 7
    Output: 1
    Explanation: The subarray [8] has a size of 1, and 8 > 7 / 1 = 7. So 1 is returned.
    Note that the subarray [6,5] has a size of 2, and every element is greater than 7 / 2 = 3.5. 
    Similarly, the subarrays [6,5,6], [6,5,6,5], [6,5,6,5,8] also satisfy the given conditions.
    Therefore, 2, 3, 4, or 5 may also be returned.
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i], threshold <= 109
'''
class DSU:
    def __init__(self, N):
        self.root = [i for i in range(N)]
        self.size = [1 for _ in range(N)]
        
    def find(self, k):
        if self.root[k] == k:
            return k
        self.root[k] = self.find(self.root[k])
        return self.root[k]
    
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            self.root[y] = x
            self.size[x] += self.size[y]
        return
    
    def get_size(self, x):
        x = self.find(x)
        return self.size[x]
# === 4663ms && 32.8MB === #
class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        dsu = DSU(n)
        
        record = defaultdict(list)
        for i, x in enumerate(nums):
            record[x].append(i)
            
        keys = sorted(record.keys(), reverse=True)
        for k in keys:
            for idx in record[k]:
                if idx+1 < n and nums[idx+1] >= nums[idx]:
                    dsu.union(idx, idx+1)
                if idx-1 >= 0 and nums[idx-1] >= nums[idx]:
                    dsu.union(idx, idx-1)
                if k > threshold / dsu.get_size(idx):
                    return dsu.get_size(idx)
        return -1
            