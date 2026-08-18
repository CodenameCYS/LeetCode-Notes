'''
=== 3591. Check if Any Element Has Prime Frequency ===

You are given an integer array nums.
Return true if the frequency of any element of the array is prime, otherwise, return false.
The frequency of an element x is the number of times it occurs in the array.
A prime number is a natural number greater than 1 with only two factors, 1 and itself.

Example 1:
    Input: nums = [1,2,3,4,5,4]
    Output: true
    Explanation:
    4 has a frequency of two, which is a prime number.
Example 2:
    Input: nums = [1,2,3,4,5]
    Output: false
    Explanation:
    All elements have a frequency of one.
Example 3:
    Input: nums = [2,2,2,4,4]
    Output: true
    Explanation:
    Both 2 and 4 have a prime frequency.

Constraints:
    1. 1 <= nums.length <= 100
    2. 0 <= nums[i] <= 100
'''
def get_primes(n):
    status = [0 for _ in range(n+1)]
    primes = set()
    for i in range(2, n+1):
        if status[i] != 0:
            continue
        primes.add(i)
        for j in range(i, n+1, i):
            status[j] = 1
    return primes

PRIMES = get_primes(100)
# === 2ms && 17.8MB === #
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        return any(n in PRIMES for n in freq.values())