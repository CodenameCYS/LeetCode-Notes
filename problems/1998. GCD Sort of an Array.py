'''
=== 1998. GCD Sort of an Array ===

You are given an integer array nums, and you can perform the following operation any number of times on nums:
    - Swap the positions of two elements nums[i] and nums[j] if gcd(nums[i], nums[j]) > 1 where gcd(nums[i], nums[j]) is the greatest common divisor of nums[i] and nums[j].
Return true if it is possible to sort nums in non-decreasing order using the above swap method, or false otherwise.

Example 1:
    Input: nums = [7,21,3]
    Output: true
    Explanation: We can sort [7,21,3] by performing the following operations:
    - Swap 7 and 21 because gcd(7,21) = 7. nums = [21,7,3]
    - Swap 21 and 3 because gcd(21,3) = 3. nums = [3,7,21]
Example 2:
    Input: nums = [5,2,6,2]
    Output: false
    Explanation: It is impossible to sort the array because 5 cannot be swapped with any other element.
Example 3:
    Input: nums = [10,5,9,3,15]
    Output: true
    We can sort [10,5,9,3,15] by performing the following operations:
    - Swap 10 and 15 because gcd(10,15) = 5. nums = [15,5,9,3,10]
    - Swap 15 and 3 because gcd(15,3) = 3. nums = [3,5,9,15,10]
    - Swap 10 and 15 because gcd(10,15) = 5. nums = [3,5,9,10,15]
 
Constraints:
    1. 1 <= nums.length <= 3 * 104
    2. 2 <= nums[i] <= 105
'''
import time

class DSU:
    def __init__(self):
        self.dsu = {}
    
    def add(self, x):
        if x not in self.dsu:
            self.dsu[x] = x
        return
    
    def find(self, x):
        if self.dsu[x] == x:
            return x
        self.dsu[x] = self.find(self.dsu[x])
        return self.dsu[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        self.dsu[x] = y
        return 
# === 6880ms && 14.3MB === #   
class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        def get_primes(n):
            k = int(math.sqrt(n+1))
            res = []
            for i in range(2, k+1):
                if n == 1:
                    break
                if n % i != 0:
                    continue
                res.append(i)
                while n % i == 0:
                    n = n // i
            if n != 1:
                res.append(n)
            return res
        
        t = time.time()
        dsu = DSU()
        for n in nums:
            primes = get_primes(n)
            dsu.add(n)
            for k in primes:
                dsu.add(k)
                dsu.union(n, k)
        # print(f"dsu time cost: {(time.time()-t)/1000:.2f}s")
        # t= time.time()
        
        groups_var = defaultdict(list)
        groups_idx = defaultdict(list)
        for i, n in enumerate(nums):
            groups_idx[dsu.find(n)].append(i)
            groups_var[dsu.find(n)].append(n)
        # print(f"group time cost: {(time.time()-t)/1000:.2f}s")
        # t= time.time()
        
        fin = []
        for k in groups_var.keys():
            groups_var[k] = sorted(groups_var[k])
            fin.extend([(idx, var) for idx, var in zip(groups_idx[k], groups_var[k])])
        fin = sorted(fin, key=lambda x: (x[1], x[0]))
        res = all(fin[i][0] == i for i in range(len(nums)))
        # print(f"final time cost: {time.time()-t:.2f}s")
        # t= time.time()
        # print("=" * 10)
        return res
                
        
        