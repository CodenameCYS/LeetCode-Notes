'''
=== 3605. Minimum Stability Factor of Array ===

You are given an integer array nums and an integer maxC.
A subarray is called stable if the highest common factor (HCF) of all its elements is greater than or equal to 2.
The stability factor of an array is defined as the length of its longest stable subarray.
You may modify at most maxC elements of the array to any integer.
Return the minimum possible stability factor of the array after at most maxC modifications. If no stable subarray remains, return 0.
Note:
    - A subarray is a contiguous sequence of elements within an array.
    - The highest common factor (HCF) of an array is the largest integer that evenly divides all the array elements.
    - A subarray of length 1 is stable if its only element is greater than or equal to 2, since HCF([x]) = x.
 
Example 1:
    Input: nums = [3,5,10], maxC = 1
    Output: 1
    Explanation:
    The stable subarray [5, 10] has HCF = 5, which has a stability factor of 2.
    Since maxC = 1, one optimal strategy is to change nums[1] to 7, resulting in nums = [3, 7, 10].
    Now, no subarray of length greater than 1 has HCF >= 2. Thus, the minimum possible stability factor is 1.
Example 2:
    Input: nums = [2,6,8], maxC = 2
    Output: 1
    Explanation:
    The subarray [2, 6, 8] has HCF = 2, which has a stability factor of 3.
    Since maxC = 2, one optimal strategy is to change nums[1] to 3 and nums[2] to 5, resulting in nums = [2, 3, 5].
    Now, no subarray of length greater than 1 has HCF >= 2. Thus, the minimum possible stability factor is 1.
Example 3:
    Input: nums = [2,4,9,6], maxC = 1
    Output: 2
    Explanation:
    The stable subarrays are:
    [2, 4] with HCF = 2 and stability factor of 2.
    [9, 6] with HCF = 3 and stability factor of 2.
    Since maxC = 1, the stability factor of 2 cannot be reduced due to two separate stable subarrays. Thus, the minimum possible stability factor is 2.
 
Constraints:
    1. 1 <= n == nums.length <= 105
    2. 1 <= nums[i] <= 109
    3. 0 <= maxC <= n
'''
class SegmentTree:
    def __init__(self, arr):
        self.length = len(arr)
        self.tree = self.build(arr)

    def feature_func(self, *args):
        args = list(args)
        def fn(arr):
            n = len(arr)
            if n == 1:
                return arr[0]
            elif n == 2:
                return gcd(arr[0], arr[1])
            else:
                return gcd(fn(arr[:n//2]), fn(arr[n//2:]))
        return fn(args)

    def build(self, arr):
        n = len(arr)
        tree = [0 for _ in range(2*n)]
        for i in range(n):
            tree[i+n] = arr[i]
        for i in range(n-1, 0, -1):
            tree[i] = self.feature_func(tree[i<<1], tree[(i<<1) | 1])
        return tree

    def update(self, idx, val):
        idx = idx + self.length
        self.tree[idx] = val
        while idx > 1:
            self.tree[idx>>1] = self.feature_func(self.tree[idx], self.tree[idx ^ 1])
            idx = idx>>1
        return

    def query(self, lb, rb):
        lb += self.length 
        rb += self.length
        nodes = []
        while lb < rb:
            if lb & 1 == 1:
                nodes.append(self.tree[lb])
                lb += 1
            if rb & 1 == 0:
                nodes.append(self.tree[rb])
                rb -= 1
            lb = lb >> 1
            rb = rb >> 1
        if lb == rb:
            nodes.append(self.tree[rb])
        return self.feature_func(*nodes)
# === 5745ms && 34.37MB === #
class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)
        if n - Counter(nums)[1] <= maxC:
            return 0 
        segment_tree = SegmentTree(nums)

        def is_possible(k):
            idx, cnt = 0, 0
            while idx + k < n:
                if segment_tree.query(idx, idx+k) <= 1:
                    idx += 1
                else:
                    cnt += 1
                    idx += k+1
                if cnt > maxC:
                    return False
            return True
        
        i, j = 1, n
        if is_possible(1):
            return 1
        while j-i>1:
            k = (i+j)//2
            if is_possible(k):
                j = k
            else:
                i = k
        return j

