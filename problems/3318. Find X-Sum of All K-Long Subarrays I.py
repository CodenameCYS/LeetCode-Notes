'''
=== 3318. Find X-Sum of All K-Long Subarrays I ===

You are given an array nums of n integers and two integers k and x.
The x-sum of an array is calculated by the following procedure:
    - Count the occurrences of all elements in the array.
    - Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
    - Calculate the sum of the resulting array.
Note that if an array has less than x distinct elements, its x-sum is the sum of the array.
Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].

Example 1:
    Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2
    Output: [6,10,12]
    Explanation:
    For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
    For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
    For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.
Example 2:
    Input: nums = [3,8,7,8,7,5], k = 2, x = 2
    Output: [11,15,15,15,12]
    Explanation:
    Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].

Constraints:
    1. 1 <= n == nums.length <= 50
    2. 1 <= nums[i] <= 50
    3. 1 <= x <= k <= nums.length
'''
# === 77ms && 16.8MB === #
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        cnt = Counter(nums[:k])
        q = sorted([(-v, -k) for k, v in cnt.items()])
        s = sum(it[0] * it[1] for it in q[:x])

        ans = [s]
        for i in range(k, n):
            key, val = nums[i-k], cnt[nums[i-k]]
            idx = bisect.bisect_left(q, (-val, -key))
            q.pop(idx)
            if idx < x:
                s -= val * key
                if x <= len(q):
                    s += q[x-1][0] * q[x-1][1]
                    
            cnt[key] -= 1
            if cnt[key] > 0:
                bisect.insort(q, (-val+1, -key))
                nidx = bisect.bisect_left(q, (-val+1, -key))
                if nidx < x:
                    s += key * (val-1)
                    if x < len(q):
                        s -= q[x][0] * q[x][1]

            key, val = nums[i], cnt[nums[i]]
            cnt[key] += 1
            if val == 0:
                bisect.insort(q, (-val-1, -key))
                idx = bisect.bisect_left(q, (-val-1, -key))
                if idx < x:
                    s += (val+1) * key
                    if x < len(q):
                        s -= q[x][0] * q[x][1]
            else:
                idx = bisect.bisect_left(q, (-val, -key))
                q.pop(idx)
                if idx < x:
                    s -= val * key
                    if x <= len(q):
                        s += q[x-1][0] * q[x-1][1]

                bisect.insort(q, (-val-1, -key))
                idx = bisect.bisect_left(q, (-val-1, -key))
                if idx < x:
                    s += (val+1) * key
                    if x < len(q):
                        s -= q[x][0] * q[x][1]
                        
            ans.append(s)
        return ans