'''
=== 3911. K-th Smallest Remaining Even Integer in Subarray Queries ===

You are given an integer array nums where nums is strictly increasing.
You are also given a 2D integer array queries, where queries[i] = [li, ri, ki].
For each query [li, ri, ki]:
    - Consider the subarray nums[li..ri]
    - From the infinite sequence of all positive even integers: 2, 4, 6, 8, 10, 12, 14, ...
    - Remove all elements that appear in the subarray nums[li..ri].
    - Find the kith smallest integer remaining in the sequence after the removals.
Return an integer array ans, where ans[i] is the result for the ith query.
A subarray is a contiguous non-empty sequence of elements within an array.
An array is said to be strictly increasing if each element is strictly greater than its previous one (if exists).

Example 1:
    Input: nums = [1,4,7], queries = [[0,2,1],[1,1,2],[0,0,3]]
    Output: [2,6,6]
    Explanation:
    i	queries[i]	nums[li..ri]	Removed
    Evens	Remaining
    Evens	ki	ans[i]
    0	[0, 2, 1]	[1, 4, 7]	[4]	2, 6, 8, ...	1	2
    1	[1, 1, 2]	[4]	[4]	2, 6, 8, ...	2	6
    2	[0, 0, 3]	[1]	[]	2, 4, 6, ...	3	6
    Thus, ans = [2, 6, 6].
Example 2:
    Input: nums = [2,5,8], queries = [[0,1,2],[1,2,1],[0,2,4]]
    Output: [6,2,12]
    Explanation:
    i	queries[i]	nums[li..ri]	Removed
    Evens	Remaining
    Evens	ki	ans[i]
    0	[0, 1, 2]	[2, 5]	[2]	4, 6, 8, ...	2	6
    1	[1, 2, 1]	[5, 8]	[8]	2, 4, 6, ...	1	2
    2	[0, 2, 4]	[2, 5, 8]	[2, 8]	4, 6, 10, 12, ...	4	12
    Thus, ans = [6, 2, 12].
Example 3:
    Input: nums = [3,6], queries = [[0,1,1],[1,1,3]]
    Output: [2,8]
    Explanation:
    i	queries[i]	nums[li..ri]	Removed
    Evens	Remaining
    Evens	ki	ans[i]
    0	[0, 1, 1]	[3, 6]	[6]	2, 4, 8, ...	1	2
    1	[1, 1, 3]	[6]	[6]	2, 4, 8, ...	3	8
    Thus, ans = [2, 8].

Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 109
    3. nums is strictly increasing
    4. 1 <= queries.length <= 105
    5. queries[i] = [li, ri, ki]
    6. 0 <= li <= ri < nums.length
    7. 1 <= ki <= 109​​​​​​​
'''
# === 1548ms && 55.16MB === #
class Solution:
    def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        cnt = [0 for _ in range(n+1)]
        for i, num in enumerate(nums):
            cnt[i+1] = cnt[i] + (num+1)%2
        
        def query(i, j, k):
            l, r = k-1, k+j-i+1
            while r-l > 1:
                m = (l+r) // 2
                if count(2*m, i, j) >= k:
                    r = m
                else:
                    l = m
            return 2*r

        def count(num, i, j):
            if num < nums[i]:
                return num // 2
            elif num >= nums[j]:
                return num // 2 - (cnt[j+1] - cnt[i])
            right = nums[j]
            nj = bisect.bisect_right(nums, right)
            # print(f"count({num}) = {num // 2 - (cnt[nj] - cnt[i])}")
            return num // 2 - (cnt[nj] - cnt[i])
        
        return [query(i,j,k) for i, j, k in queries]

'''
=== 3911. K-th Smallest Remaining Even Integer in Subarray Queries ===

You are given an integer array nums where nums is strictly increasing.
You are also given a 2D integer array queries, where queries[i] = [li, ri, ki].
For each query [li, ri, ki]:
    - Consider the subarray nums[li..ri]
    - From the infinite sequence of all positive even integers: 2, 4, 6, 8, 10, 12, 14, ...
    - Remove all elements that appear in the subarray nums[li..ri].
    - Find the kith smallest integer remaining in the sequence after the removals.
Return an integer array ans, where ans[i] is the result for the ith query.
A subarray is a contiguous non-empty sequence of elements within an array.
An array is said to be strictly increasing if each element is strictly greater than its previous one (if exists).

Example 1:
    Input: nums = [1,4,7], queries = [[0,2,1],[1,1,2],[0,0,3]]
    Output: [2,6,6]
    Explanation:
    i	queries[i]	nums[li..ri]	Removed
    Evens	Remaining
    Evens	ki	ans[i]
    0	[0, 2, 1]	[1, 4, 7]	[4]	2, 6, 8, ...	1	2
    1	[1, 1, 2]	[4]	[4]	2, 6, 8, ...	2	6
    2	[0, 0, 3]	[1]	[]	2, 4, 6, ...	3	6
    Thus, ans = [2, 6, 6].
Example 2:
    Input: nums = [2,5,8], queries = [[0,1,2],[1,2,1],[0,2,4]]
    Output: [6,2,12]
    Explanation:
    i	queries[i]	nums[li..ri]	Removed
    Evens	Remaining
    Evens	ki	ans[i]
    0	[0, 1, 2]	[2, 5]	[2]	4, 6, 8, ...	2	6
    1	[1, 2, 1]	[5, 8]	[8]	2, 4, 6, ...	1	2
    2	[0, 2, 4]	[2, 5, 8]	[2, 8]	4, 6, 10, 12, ...	4	12
    Thus, ans = [6, 2, 12].
Example 3:
    Input: nums = [3,6], queries = [[0,1,1],[1,1,3]]
    Output: [2,8]
    Explanation:
    i	queries[i]	nums[li..ri]	Removed
    Evens	Remaining
    Evens	ki	ans[i]
    0	[0, 1, 1]	[3, 6]	[6]	2, 4, 8, ...	1	2
    1	[1, 1, 3]	[6]	[6]	2, 4, 8, ...	3	8
    Thus, ans = [2, 8].

Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 109
    3. nums is strictly increasing
    4. 1 <= queries.length <= 105
    5. queries[i] = [li, ri, ki]
    6. 0 <= li <= ri < nums.length
    7. 1 <= ki <= 109​​​​​​​
'''
# === 1548ms && 55.16MB === #
'''
=== 3911. K-th Smallest Remaining Even Integer in Subarray Queries ===

You are given an integer array nums where nums is strictly increasing.
You are also given a 2D integer array queries, where queries[i] = [li, ri, ki].
For each query [li, ri, ki]:
    - Consider the subarray nums[li..ri]
    - From the infinite sequence of all positive even integers: 2, 4, 6, 8, 10, 12, 14, ...
    - Remove all elements that appear in the subarray nums[li..ri].
    - Find the kith smallest integer remaining in the sequence after the removals.
Return an integer array ans, where ans[i] is the result for the ith query.
A subarray is a contiguous non-empty sequence of elements within an array.
An array is said to be strictly increasing if each element is strictly greater than its previous one (if exists).

Example 1:
    Input: nums = [1,4,7], queries = [[0,2,1],[1,1,2],[0,0,3]]
    Output: [2,6,6]
    Explanation:
    i	queries[i]	nums[li..ri]	Removed
    Evens	Remaining
    Evens	ki	ans[i]
    0	[0, 2, 1]	[1, 4, 7]	[4]	2, 6, 8, ...	1	2
    1	[1, 1, 2]	[4]	[4]	2, 6, 8, ...	2	6
    2	[0, 0, 3]	[1]	[]	2, 4, 6, ...	3	6
    Thus, ans = [2, 6, 6].
Example 2:
    Input: nums = [2,5,8], queries = [[0,1,2],[1,2,1],[0,2,4]]
    Output: [6,2,12]
    Explanation:
    i	queries[i]	nums[li..ri]	Removed
    Evens	Remaining
    Evens	ki	ans[i]
    0	[0, 1, 2]	[2, 5]	[2]	4, 6, 8, ...	2	6
    1	[1, 2, 1]	[5, 8]	[8]	2, 4, 6, ...	1	2
    2	[0, 2, 4]	[2, 5, 8]	[2, 8]	4, 6, 10, 12, ...	4	12
    Thus, ans = [6, 2, 12].
Example 3:
    Input: nums = [3,6], queries = [[0,1,1],[1,1,3]]
    Output: [2,8]
    Explanation:
    i	queries[i]	nums[li..ri]	Removed
    Evens	Remaining
    Evens	ki	ans[i]
    0	[0, 1, 1]	[3, 6]	[6]	2, 4, 8, ...	1	2
    1	[1, 1, 3]	[6]	[6]	2, 4, 8, ...	3	8
    Thus, ans = [2, 8].

Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 109
    3. nums is strictly increasing
    4. 1 <= queries.length <= 105
    5. queries[i] = [li, ri, ki]
    6. 0 <= li <= ri < nums.length
    7. 1 <= ki <= 109​​​​​​​
'''
# === 1174ms && 55.51MB === #
class Solution:
    def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        cnt = [0 for _ in range(n+1)]
        for i, num in enumerate(nums):
            cnt[i+1] = cnt[i] + (num+1)%2
        
        def query(i, j, k):
            l, r = k-1, k+j-i+1
            while r-l > 1:
                m = (l+r) // 2
                if count(2*m, i, j) >= k:
                    r = m
                else:
                    l = m
            return 2*r

        def count(num, i, j):
            if num < nums[i]:
                return num // 2
            elif num >= nums[j]:
                return num // 2 - (cnt[j+1] - cnt[i])
            nj = bisect.bisect_right(nums, num)
            # print(f"count({num}) = {num // 2 - (cnt[nj] - cnt[i])}")
            return num // 2 - (cnt[nj] - cnt[i])
        
        return [query(i,j,k) for i, j, k in queries]
