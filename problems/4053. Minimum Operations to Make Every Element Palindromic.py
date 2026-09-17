'''
=== 4053. Minimum Operations to Make Every Element Palindromic ===

You are given an integer array nums.
In one operation, you may choose an index i and either increment or decrement nums[i] by 2.
Return the minimum number of operations required to make every element in nums a positive palindrome. Different elements may be changed into different palindromic integers.

Example 1:
    Input: nums = [10,12,14,16]
    Output: 9
    Explanation:
    One optimal sequence of operations is:
    Decrement nums[0] by 2 once to change it from 10 to 8.
    Decrement nums[1] by 2 twice to change it from 12 to 8.
    Decrement nums[2] by 2 three times to change it from 14 to 8.
    Increment nums[3] by 2 three times to change it from 16 to 22.
    After 1 + 2 + 3 + 3 = 9 operations, nums = [8, 8, 8, 22], and every element is a positive palindromic integer.
    It can be shown that fewer than 9 operations cannot achieve this.
Example 2:
    Input: nums = [9,10,11,10]
    Output: 2
    Explanation:
    Decrement nums[1] and nums[3] by 2 once each.
    After 2 operations, nums = [9, 8, 11, 8], and every element is a positive palindromic integer.
    At least one operation is needed for each of these two elements, so the minimum number of operations is 2.
Example 3:
    Input: nums = [125]
    Output: 2
    Explanation:
    Decrement nums[0] by 2 twice to change it from 125 to 121, which is a positive palindromic integer.
    A single operation would change it to 123 or 127, neither of which is palindromic. Thus, the minimum number of operations is 2.

Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 109
'''
# === 404ms && 42.64MB === #
def get_palindromic_int():
    ints = [i for i in range(1, 10)]
    for i in range(1, 10000):
        s = str(i)
        num = int(s + s[::-1])
        ints.append(num)
        for j in range(10):
            num = int(s + str(j) + s[::-1])
            ints.append(num)
    odds = sorted([x for x in ints if x % 2 == 1])
    even = sorted([x for x in ints if x % 2 == 0])
    return odds, even

OddPalindomicIntegers, EvenPalindomicIntegers = get_palindromic_int()
# print(len(PalindomicIntegers))
# print(PalindomicIntegers[:100])

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n, m = len(OddPalindomicIntegers), len(EvenPalindomicIntegers)

        def get_op_num(num):
            if num % 2 == 1:
                return _get_op_num(num, OddPalindomicIntegers, n)
            else:
                return _get_op_num(num, EvenPalindomicIntegers, m)

        def _get_op_num(num, PalindomicIntegers, n):
            idx = bisect.bisect_left(PalindomicIntegers, num)
            if idx == 0:
                return (PalindomicIntegers[idx] - num) // 2
            elif idx == n:
                return (num - PalindomicIntegers[idx-1]) // 2
            else:
                return min(PalindomicIntegers[idx]-num, num-PalindomicIntegers[idx-1]) // 2

        return sum(get_op_num(num) for num in nums)
        
        