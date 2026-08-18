'''
=== 1502. Can Make Arithmetic Progression From Sequence ===

Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.

Example 1:
    Input: arr = [3,5,1]
    Output: true
    Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
Example 2:
    Input: arr = [1,2,4]
    Output: false
    Explanation: There is no way to reorder the elements to obtain an arithmetic progression.
 
Constraints:
    1. 2 <= arr.length <= 1000
    2. -10^6 <= arr[i] <= 10^6
'''
# === 80ms && 13.9MB === #
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2:
            return True
        arr = sorted(arr)
        delta = arr[1] - arr[0]
        return all(arr[i+1]-arr[i] == delta for i in range(1, len(arr)-1))