'''
# === 1207. Unique Number of Occurrences === #

Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example 1:
    Input: arr = [1,2,2,1,1,3]
    Output: true
    - Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:
    Input: arr = [1,2]
    Output: false
Example 3:
    Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
    Output: true
 
Constraints:
    1. 1 <= arr.length <= 1000
    2. -1000 <= arr[i] <= 1000
'''
# === 48ms & 13.8MB === #
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for it in arr:
            if it in count.keys():
                count[it] += 1
            else:
                count[it] = 1
        tmp = sorted(count.items(), key=lambda x: x[1])
        for i in range(len(tmp)-1):
            if tmp[i][1] == tmp[i+1][1]:
                return False
        return True