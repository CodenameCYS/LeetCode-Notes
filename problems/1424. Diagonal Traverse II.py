'''
=== 1424. Diagonal Traverse II ===

Given a list of lists of integers, nums, return all elements of nums in diagonal order as shown in the below images.
 
Example 1:
    Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,4,2,7,5,3,8,6,9]
Example 2:
    Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
    Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
Example 3:
    Input: nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
    Output: [1,4,2,5,3,8,6,9,7,10,11]
Example 4:
    Input: nums = [[1,2,3,4,5,6]]
    Output: [1,2,3,4,5,6]
 
Constraints:
    1. 1 <= nums.length <= 10^5
    2. 1 <= nums[i].length <= 10^5
    3. 1 <= nums[i][j] <= 10^9
    4. There at most 10^5 elements in nums.
'''
# === 1008ms(99.46%) && 33.7MB === #
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n = max([i+len(it) for i,it in enumerate(nums)])
        arr_list = [[] for i in range(n)]
        for i in range(len(nums)-1, -1, -1):
            for j, val in enumerate(nums[i]):
                arr_list[i+j].append(val)
        ans = []
        for arr in arr_list:
            ans.extend(arr)
        return ans