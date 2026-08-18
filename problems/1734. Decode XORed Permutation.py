'''
=== 1734. Decode XORed Permutation ===

There is an integer array perm that is a permutation of the first n positive integers, where n is always odd.
It was encoded into another integer array encoded of length n - 1, such that encoded[i] = perm[i] XOR perm[i + 1]. For example, if perm = [1,3,2], then encoded = [2,1].
Given the encoded array, return the original array perm. It is guaranteed that the answer exists and is unique.

Example 1:
    Input: encoded = [3,1]
    Output: [1,2,3]
    Explanation: If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]
Example 2:
    Input: encoded = [6,5,4,6]
    Output: [2,4,1,5,3]
 
Constraints:
    1. 3 <= n < 105
    2. n is odd.
    3. encoded.length == n - 1
'''
# === 1492ms && 35MB === #
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded)
        x1 = 0
        for i in range(1, n+2):
            x1 = x1 ^ i
        # print(x1)
        for i in range(1, n, 2):
            x1 = x1 ^ encoded[i]
        # print(x1)
        s = deepcopy(encoded)
        for i in range(n-1):
            s[i+1] = s[i] ^ s[i+1]
        res = [x1] + [x1 ^ x for x in s]
        return res