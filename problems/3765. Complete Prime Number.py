'''
=== 3765. Complete Prime Number ===

You are given an integer num.
A number num is called a Complete Prime Number if every prefix and every suffix of num is prime.
Return true if num is a Complete Prime Number, otherwise return false.
Note:
    - A prefix of a number is formed by the first k digits of the number.
    - A suffix of a number is formed by the last k digits of the number.
    - A prime number is a natural number greater than 1 with only two factors, 1 and itself.
    - Single-digit numbers are considered Complete Prime Numbers only if they are prime.
 

Example 1:
    Input: num = 23
    Output: true
    Explanation:
    ​​​​​​​Prefixes of num = 23 are 2 and 23, both are prime.
    Suffixes of num = 23 are 3 and 23, both are prime.
    All prefixes and suffixes are prime, so 23 is a Complete Prime Number and the answer is true.
Example 2:
    Input: num = 39
    Output: false
    Explanation:
    Prefixes of num = 39 are 3 and 39. 3 is prime, but 39 is not prime.
    Suffixes of num = 39 are 9 and 39. Both 9 and 39 are not prime.
    At least one prefix or suffix is not prime, so 39 is not a Complete Prime Number and the answer is false.
Example 3:
    Input: num = 7
    Output: true
    Explanation:
    7 is prime, so all its prefixes and suffixes are prime and the answer is true.

Constraints:
    1. 1 <= num <= 109
'''
# === 4ms && 18.87MB === #
def get_primes(n):
    primes = set()
    status = [0 for _ in range(n+1)]
    for i in range(2, n+1):
        if status[i] == 1:
            continue
        primes.add(i)
        for j in range(i, n+1, i):
            status[j] = 1
    return primes

PRIMES = get_primes(10**5)

def is_prime(num):
    if num == 1:
        return False
    if num in PRIMES:
        return True
    return all(num % x != 0 for x in PRIMES)

class Solution:
    def completePrime(self, num: int) -> bool:
        s = str(num)
        n = len(s)
        for i in range(n):
            l = int(s[:i+1])
            if not is_prime(l):
                return False
            r = int(s[-i-1:])
            if not is_prime(r):
                return False
        return True

        