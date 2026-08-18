'''
=== 3510. Minimum Pair Removal to Sort Array II ===

Given an array nums, you can perform the following operation any number of times:
    - Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
    - Replace the pair with their sum.
Return the minimum number of operations needed to make the array non-decreasing.
An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

Example 1:
    Input: nums = [5,2,3,1]
    Output: 2
    Explanation:
    The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
    The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
    The array nums became non-decreasing in two operations.
Example 2:
    Input: nums = [1,2,2]
    Output: 0
    Explanation:
    The array nums is already sorted.

Constraints:
    1. 1 <= nums.length <= 105
    2. -109 <= nums[i] <= 109
'''
# === Time Limit Exceeded === #
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        index = [i for i in range(n)]
        pairs = sorted([(nums[i] + nums[i+1], i) for i in range(n-1)])
        reverse_cnt = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                reverse_cnt += 1
                
        m = n
        while reverse_cnt > 0:
            s, idx = pairs.pop(0)
            i = bisect.bisect_left(index, idx)
            
            # replace element
            x, y = nums[i], nums[i+1]
            xi, yi = index[i], index[i+1]
            nums.pop(i+1)
            nums[i] = x+y
            index.pop(i+1)
            m -= 1
            if x > y:
                reverse_cnt -= 1
            
            # maintain pre element
            if i-1 >= 0:
                t, ti = nums[i-1], index[i-1]
                pairs.pop(bisect.bisect_left(pairs, (t+x, ti)))
                bisect.insort(pairs, (t+x+y, ti))
                if t > x:
                    reverse_cnt -= 1
                if t > x+y:
                    reverse_cnt += 1
                
            # maintain post element
            if i+1 < m:
                t, ti = nums[i+1], index[i+1]
                pairs.pop(bisect.bisect_left(pairs, (t+y, yi)))
                bisect.insort(pairs, (t+x+y, xi))
                if y > t:
                    reverse_cnt -= 1
                if x+y > t:
                    reverse_cnt += 1

        return n - m
    
# === 7765ms && 95.4MB === #
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        index = [i for i in range(n)]
        pairs = [(nums[i] + nums[i+1], i) for i in range(n-1)]
        heapq.heapify(pairs)
        remove = set()
        reverse_cnt = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                reverse_cnt += 1
                
        m = n
        while reverse_cnt > 0:
            s, idx = heapq.heappop(pairs)
            if (s, idx) in remove:
                continue
            remove.add((s, idx))
                
            i = bisect.bisect_left(index, idx)
            
            # replace element
            x, y = nums[i], nums[i+1]
            xi, yi = index[i], index[i+1]
            nums.pop(i+1)
            nums[i] = x+y
            index.pop(i+1)
            m -= 1
            if x > y:
                reverse_cnt -= 1
            
            # maintain pre element
            if i-1 >= 0:
                t, ti = nums[i-1], index[i-1]
                remove.add((t+x, ti))
                heapq.heappush(pairs, (t+x+y, ti))
                if (t+x+y, ti) in remove:
                    remove.remove((t+x+y, ti))
                if t > x:
                    reverse_cnt -= 1
                if t > x+y:
                    reverse_cnt += 1
                
            # maintain post element
            if i+1 < m:
                t, ti = nums[i+1], index[i+1]
                remove.add((t+y, yi))
                heapq.heappush(pairs, (t+x+y, xi))
                if (t+x+y, xi) in remove:
                    remove.remove((t+x+y, xi))
                if y > t:
                    reverse_cnt -= 1
                if x+y > t:
                    reverse_cnt += 1

        return n - m
        
        