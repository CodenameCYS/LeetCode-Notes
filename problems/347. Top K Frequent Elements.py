'''
=== 347. Top K Frequent Elements ===

Given a non-empty array of integers, return the k most frequent elements.

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
Example 2:
    Input: nums = [1], k = 1
    Output: [1]

Note:
    1. You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    2. Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
    3. It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
    4. You can return the answer in any order.
'''
# === 112ms(67.40%) && 18.4MB(43.10%) === #
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in counter[:k]]