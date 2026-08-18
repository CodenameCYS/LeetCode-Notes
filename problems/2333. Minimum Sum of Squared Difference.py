'''
=== 2333. Minimum Sum of Squared Difference ===

You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.
The sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])2 for each 0 <= i < n.
You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.
Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.
Note: You are allowed to modify the array elements to become negative integers.

Example 1:
    Input: nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0
    Output: 579
    Explanation: The elements in nums1 and nums2 cannot be modified because k1 = 0 and k2 = 0. 
    The sum of square difference will be: (1 - 2)2 + (2 - 10)2 + (3 - 20)2 + (4 - 19)2 = 579.
Example 2:
    Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
    Output: 43
    Explanation: One way to obtain the minimum sum of square difference is: 
    - Increase nums1[0] once.
    - Increase nums2[2] once.
    The minimum of the sum of square difference will be: 
    (2 - 5)2 + (4 - 8)2 + (10 - 7)2 + (12 - 9)2 = 43.
    Note that, there are other ways to obtain the minimum of the sum of square difference, but there is no way to obtain a sum smaller than 43.
    
Constraints:
    1. n == nums1.length == nums2.length
    2. 1 <= n <= 105
    3. 0 <= nums1[i], nums2[i] <= 105
    4. 0 <= k1, k2 <= 109
'''
# === 2509ms && 31.9MB === #
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        delta = sorted([abs(x-y) for x, y in zip(nums1, nums2)], reverse=True)
        n = len(delta)
        k = k1 + k2
        # print(delta)
        
        if sum(delta) <= k:
            return 0
        
        tot = 0
        for i in range(n):
            tot += delta[i]
            flag = delta[i+1] if i < n-1 else 0
            if tot - (i+1) * flag >= k:
                avg = math.ceil((tot - k) / (i+1))
                for j in range(i+1):
                    k -= delta[j] - avg
                res = avg*avg*(i+1 - k) + (avg-1)**2 * k
                # print(avg, i, k, res)
                for j in range(i+1, n):
                    res += delta[j] * delta[j]
                return res
        return -1
                
        
        
        