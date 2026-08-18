'''
=== 3766. Minimum Operations to Make Binary Palindrome ===

You are given an integer array nums.
For each element nums[i], you may perform the following operations any number of times (including zero):
    - Increase nums[i] by 1, or
    - Decrease nums[i] by 1.
A number is called a binary palindrome if its binary representation without leading zeros reads the same forward and backward.
Your task is to return an integer array ans, where ans[i] represents the minimum number of operations required to convert nums[i] into a binary palindrome.

Example 1:
    Input: nums = [1,2,4]
    Output: [0,1,1]
    Explanation:
    One optimal set of operations:
    nums[i]	Binary(nums[i])	Nearest
    Palindrome	Binary
    (Palindrome)	Operations Required	ans[i]
    1	1	1	1	Already palindrome	0
    2	10	3	11	Increase by 1	1
    4	100	3	11	Decrease by 1	1
    Thus, ans = [0, 1, 1].
Example 2:
    Input: nums = [6,7,12]
    Output: [1,0,3]
    Explanation:
    One optimal set of operations:
    nums[i]	Binary(nums[i])	Nearest
    Palindrome	Binary
    (Palindrome)	Operations Required	ans[i]
    6	110	5	101	Decrease by 1	1
    7	111	7	111	Already palindrome	0
    12	1100	15	1111	Increase by 3	3
    Thus, ans = [1, 0, 3].

Constraints:
    1. 1 <= nums.length <= 5000
    ​2. ​​​​​​1 <= nums[i] <= 5000
'''
# === 27ms && 18.38MB === #
def get_binary_palindromes(n):
    binary_palindromes = []
    for i in range(1, n+1):
        s = bin(i)[2:]
        if s == s[::-1]:
            binary_palindromes.append(i)
    return binary_palindromes

binary_palindromes = get_binary_palindromes(8192)

class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        
        def query(num):
            i = bisect.bisect_left(binary_palindromes, num)
            if binary_palindromes[i] == num:
                return 0
            return min(num-binary_palindromes[i-1], binary_palindromes[i]-num)
        return [query(num) for num in nums]
        