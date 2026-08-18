'''
=== 3748. Count Stable Subarrays ===

You are given an integer array nums.
A subarray of nums is called stable if it contains no inversions, i.e., there is no pair of indices i < j such that nums[i] > nums[j].
You are also given a 2D integer array queries of length q, where each queries[i] = [li, ri] represents a query. For each query [li, ri], compute the number of stable subarrays that lie entirely within the segment nums[li..ri].
Return an integer array ans of length q, where ans[i] is the answer to the ith query.​​​​​​​​​​​​​​

Note:
    - A single element subarray is considered stable.
 
Example 1:
    Input: nums = [3,1,2], queries = [[0,1],[1,2],[0,2]]
    Output: [2,3,4]
    Explanation:​​​​​
    For queries[0] = [0, 1], the subarray is [nums[0], nums[1]] = [3, 1].
    The stable subarrays are [3] and [1]. The total number of stable subarrays is 2.
    For queries[1] = [1, 2], the subarray is [nums[1], nums[2]] = [1, 2].
    The stable subarrays are [1], [2], and [1, 2]. The total number of stable subarrays is 3.
    For queries[2] = [0, 2], the subarray is [nums[0], nums[1], nums[2]] = [3, 1, 2].
    The stable subarrays are [3], [1], [2], and [1, 2]. The total number of stable subarrays is 4.
    Thus, ans = [2, 3, 4].
Example 2:
    Input: nums = [2,2], queries = [[0,1],[0,0]]
    Output: [3,1]
    Explanation:
    For queries[0] = [0, 1], the subarray is [nums[0], nums[1]] = [2, 2].
    The stable subarrays are [2], [2], and [2, 2]. The total number of stable subarrays is 3.
    For queries[1] = [0, 0], the subarray is [nums[0]] = [2].
    The stable subarray is [2]. The total number of stable subarrays is 1.
    Thus, ans = [3, 1].

Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 105
    3. 1 <= queries.length <= 105
    4. queries[i] = [li, ri]
    5. 0 <= li <= ri <= nums.length - 1
'''
# === 436ms && 52.62MB === #
class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        pre, idx, n = 0, 1, len(nums)
        groups, s = [], []
        while idx < n:
            if nums[idx] < nums[idx-1]:
                m = idx-pre
                groups.append([pre, idx-1])
                s.append(m*(m+1)//2)
                pre = idx
            idx += 1
        m = n-pre
        groups.append([pre, n-1])
        s.append(m*(m+1)//2)
        prefix = list(accumulate(s, initial=0))
        # print(groups, s, prefix)

        def query(l, r):
            lb = bisect.bisect_right(groups, [l, n])-1
            rb = bisect.bisect_right(groups, [r, n])-1
            # print(l, r, lb, rb)
            if lb >= rb:
                return (r-l+1) * (r-l+2)//2
            mid = prefix[rb] - prefix[lb+1]
            left = groups[lb][1] - l + 1
            right = r - groups[rb][0] + 1
            # print(mid, left, right)
            return mid + left * (left+1) // 2 + right * (right+1)//2

        return [query(l, r) for l, r in queries]
            


                
        
