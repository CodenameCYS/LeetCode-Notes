'''
=== 4039. Sum of Decoded Numbers ===

You are given an integer array nums.
Each nums[i] is an encoded integer representing two positive integers xi and yi. To decode nums[i], define:
    - widthi = nums[i] % 10.
    - di = floor(nums[i] / 10).
    - xi as the integer formed by the first widthi digits of the decimal representation of di.
    - yi as the integer formed by all remaining digits of the decimal representation of di.
It is guaranteed that the decimal representation of di contains more than widthi digits. Therefore, both xi and yi contain at least one digit.
The decoded value of nums[i] is xiyi.
Return the sum of the decoded values of all elements in nums, modulo 109 + 7.
The floor() function returns the integer part of the division.

Example 1:
    Input: nums = [231]
    Output: 8
    Explanation:
    For 231, we have width = 1, d = 23, x = 2, and y = 3.
    The decoded value of 231 is 23 = 8.
    Since there is only one element in nums, the sum of the decoded values is 8.
Example 2:
    Input: nums = [2522,2101]
    Output: 1649
    Explanation:
    For 2522, we have width = 2, d = 252, x = 25, and y = 2.
    The decoded value of 2522 is 252 = 625.
    For 2101, we have width = 1, d = 210, x = 2, and y = 10.
    The decoded value of 2101 is 210 = 1024.
    The sum of the decoded values is 625 + 1024 = 1649.
Example 3:
    Input: nums = [2301]
    Output: 73741817
    Explanation:
    For 2301, we have width = 1, d = 230, x = 2, and y = 30.
    The decoded value is 230 = 1073741824.
    Therefore, the answer is 1073741824 modulo (109 + 7) = 73741817.
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 100 < nums[i] < 1015
    3. 1 <= widthi <= 9
    4. 1 <= xi, yi < 109
    5. The digit sequences used to form xi and yi do not have leading zeros.
    6. It is guaranteed that every element in nums is a valid encoded integer.
'''
MOD = 10**9+7
# === 446ms && 32.22MB === #
class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        
        def decode(num):
            w = num % 10
            d = str(num // 10)
            x = int(d[:w])
            y = int(d[w:])
            return pow(x, y, mod=MOD)
        
        return sum(decode(num) for num in nums) % MOD