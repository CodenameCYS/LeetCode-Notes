'''
=== 179. Largest Number ===

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:
    Input: [10,2]
    Output: "210"
Example 2:
    Input: [3,30,34,5,9]
    Output: "9534330"

Note: The result may be very large, so you need to return a string instead of an integer.
'''
# === 40ms(69.37%) && 14.3MB(5.29%) === #
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def is_greater(x, y):
            if x == y:
                return True
            n, m = len(x), len(y)
            i = 0
            while i<n and i<m:
                if x[i] > y[i]:
                    return True
                elif x[i] < y[i]:
                    return False
                i += 1
            if i == n:
                return is_greater(x, y[n:])
            else:
                return is_greater(x[m:], y)
            
        def quicksort(nums, st, ed):
            if st >= ed:
                return
            i = st
            j = ed
            flag = nums[st]
            while i<j:
                while i<j and is_greater(flag, nums[j]):
                    j -= 1
                if i<j:
                    nums[i] = nums[j]
                    i += 1
                while i < j and is_greater(nums[i], flag):
                    i += 1
                if i<j:
                    nums[j] = nums[i]
                    j -= 1
            nums[i] = flag
            quicksort(nums, st, i-1)
            quicksort(nums, i+1, ed)
                    
        l = len(nums)  
        ans = [str(n) for n in nums]
        # print(ans)
        quicksort(ans, 0, l-1)
        # print(ans)
        ans = "".join(ans).lstrip('0')
        return '0' if not ans else ans
        