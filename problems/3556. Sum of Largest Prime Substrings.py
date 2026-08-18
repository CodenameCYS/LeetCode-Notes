'''
=== 3556. Sum of Largest Prime Substrings ===

Given a string s, find the sum of the 3 largest unique prime numbers that can be formed using any of its substrings.
Return the sum of the three largest unique prime numbers that can be formed. If fewer than three exist, return the sum of all available primes. If no prime numbers can be formed, return 0.
A prime number is a natural number greater than 1 with only two factors, 1 and itself.
A substring is a contiguous sequence of characters within a string.
Note: Each prime number should be counted only once, even if it appears in multiple substrings. Additionally, when converting a substring to an integer, any leading zeros are ignored.

Example 1:
    Input: s = "12234"
    Output: 1469
    Explanation:
    The unique prime numbers formed from the substrings of "12234" are 2, 3, 23, 223, and 1223.
    The 3 largest primes are 1223, 223, and 23. Their sum is 1469.
Example 2:
    Input: s = "111"
    Output: 11
    Explanation:
    The unique prime number formed from the substrings of "111" is 11.
    Since there is only one prime number, the sum is 11.
 
Constraints:
    1. 1 <= s.length <= 10
    2. s consists of only digits.
'''
# === 1560ms && 18.7MB === #
class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        
        def is_prime(num):
            if num == 1:
                return False
            m = min(ceil(math.sqrt(num)) + 1, num)
            status = [0 for _ in range(m)]
            for i in range(2, m):
                if status[i] == 1:
                    continue
                if num % i == 0:
                    return False
                for j in range(i, m, i):
                    status[j] = 1
            return True
        
        primes = set()
        n = len(s)
        for i in range(n):
            for j in range(i+1, n+1):
                num = int(s[i:j])
                if is_prime(num):
                    primes.add(num)
        primes = sorted(primes, reverse=True)[:3]
        return sum(primes) if len(primes) > 0 else 0
        
# === 797ms && 23.9MB === #
def get_primes(n):
    primes = set()
    status = [0 for _ in range(n+1)]
    for i in range(2, n+1):
        if status[i] == 0:
            primes.add(i)
        for j in range(i, n+1, i):
            status[j] = 1
    return primes

PRIMES = get_primes(400000)

class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        
        def is_prime(num):
            if num == 1:
                return False
            if num in PRIMES:
                return True
            for p in PRIMES:
                if num % p == 0:
                    return False
            return True
        
        primes = set()
        n = len(s)
        seen = set()
        for i in range(n):
            for j in range(i+1, n+1):
                num = int(s[i:j])
                if num in seen:
                    continue
                seen.add(num)
                if is_prime(num):
                    primes.add(num)
        primes = sorted(primes, reverse=True)[:3]
        return sum(primes) if len(primes) > 0 else 0
        