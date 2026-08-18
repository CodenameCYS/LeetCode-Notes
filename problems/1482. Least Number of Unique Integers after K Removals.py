'''
=== 1482. Least Number of Unique Integers after K Removals ===

Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

Example 1:
    Input: arr = [5,5,4], k = 1
    Output: 1
    Explanation: Remove the single 4, only 5 is left.
Example 2:
    Input: arr = [4,3,1,1,3,3,2], k = 3
    Output: 2
    Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
 
Constraints:
    1. 1 <= arr.length <= 10^5
    2. 1 <= arr[i] <= 10^9
    3. 0 <= k <= arr.length
'''
# === 1596ms && 31MB === #
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = {}
        for i in arr:
            counter[i] = 1 if i not in counter.keys() else counter[i] + 1
        counter = sorted(counter.items(), key=lambda x:x[1])
        while counter != []:
            if counter[0][1] <= k:
                k -= counter[0][1]
                counter.pop(0)
            else:
                break
        return len(counter)