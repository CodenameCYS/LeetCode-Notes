'''
=== 3542. Minimum Operations to Convert All Elements to Zero ===

You are given an array nums of size n, consisting of non-negative integers. Your task is to apply some (possibly zero) operations on the array so that all elements become 0.
In one operation, you can select a subarray [i, j] (where 0 <= i <= j < n) and set all occurrences of the minimum non-negative integer in that subarray to 0.
Return the minimum number of operations required to make all elements in the array 0.
A subarray is a contiguous sequence of elements within an array.
 
Example 1:
    Input: nums = [0,2]
    Output: 1
    Explanation:
    Select the subarray [1,1] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0].
    Thus, the minimum number of operations required is 1.
Example 2:
    Input: nums = [3,1,2,1]
    Output: 3
    Explanation:
    Select subarray [1,3] (which is [1,2,1]), where the minimum non-negative integer is 1. Setting all occurrences of 1 to 0 results in [3,0,2,0].
    Select subarray [2,2] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [3,0,0,0].
    Select subarray [0,0] (which is [3]), where the minimum non-negative integer is 3. Setting all occurrences of 3 to 0 results in [0,0,0,0].
    Thus, the minimum number of operations required is 3.
Example 3:
    Input: nums = [1,2,1,2,1,2]
    Output: 4
    Explanation:
    Select subarray [0,5] (which is [1,2,1,2,1,2]), where the minimum non-negative integer is 1. Setting all occurrences of 1 to 0 results in [0,2,0,2,0,2].
    Select subarray [1,1] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,2,0,2].
    Select subarray [3,3] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,0,0,2].
    Select subarray [5,5] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,0,0,0].
    Thus, the minimum number of operations required is 4.

Constraints:
    1. 1 <= n == nums.length <= 105
    2. 0 <= nums[i] <= 105
'''
# === 1674ms && 47.3MB === #
class DSU:
    def __init__(self, arr):
        self.arr = arr
        self.root = [i for i in range(len(arr))]
        
    def find(self, k):
        if self.root[k] != k:
            self.root[k] = self.find(self.root[k])
        return self.root[k]
    
    def find_elem(self, k):
        return self.arr[self.find(k)]
    
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            if self.arr[x] <= self.arr[y]:
                self.root[y] = x
            else:
                self.root[x] = y
        return

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        dsu = DSU(nums)
        seen = set()
        nums = sorted([(x, i) for i, x in enumerate(nums)], reverse=True)
        ans = 0
        for x, i in nums:
            if x == 0:
                break
            need_op = True
            seen.add(i)
            if i-1 >= 0 and i-1 in seen:
                if dsu.find_elem(i-1) <= x:
                    need_op = False
                dsu.union(i-1, i)
            if i+1 < n and i+1 in seen:
                if dsu.find_elem(i+1) <= x:
                    need_op = False
                dsu.union(i+1, i)
            if need_op:
                ans += 1
        return ans
        
        
        