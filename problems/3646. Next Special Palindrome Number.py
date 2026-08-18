'''
=== 3646. Next Special Palindrome Number ===

You are given an integer n.
A number is called special if:
    - It is a palindrome.
    - Every digit k in the number appears exactly k times.
Return the smallest special number strictly greater than n.
An integer is a palindrome if it reads the same forward and backward. For example, 121 is a palindrome, while 123 is not.

Example 1:
    Input: n = 2
    Output: 22
    Explanation:
    22 is the smallest special number greater than 2, as it is a palindrome and the digit 2 appears exactly 2 times.
Example 2:
    Input: n = 33
    Output: 212
    Explanation:
    212 is the smallest special number greater than 33, as it is a palindrome and the digits 1 and 2 appear exactly 1 and 2 times respectively.

Constraints:
    1. 0 <= n <= 1015
'''
# === 0ms && 18.36MB === #
def get_special_palindrome():
    even = [2, 4, 6, 8]
    odd = [1, 3, 5, 7, 9]
    ans = set()

    def get_candidates(idx, candidates):
        nonlocal ans
        if len(candidates) > 8:
            return
        if idx < 4:
            get_candidates(idx+1, candidates)
            get_candidates(idx+1, candidates + [even[idx]] * (even[idx]//2))
        else:
            if len(candidates) > 0:
                for purb in permutations(candidates):
                    sub = "".join([str(x) for x in purb])
                    ans.add(int(sub + sub[::-1]))
            for num in odd:
                dup = [str(num)] * (num//2)
                candi = candidates + dup
                if len(candi) > 8:
                    break
                for purb in permutations(candi):
                    sub = "".join([str(x) for x in purb])
                    ans.add(int(sub + str(num) + sub[::-1]))
        return

    get_candidates(0, [])
    return sorted(ans)

SPECIAL_PALINDROME = get_special_palindrome()

class Solution:
    def specialPalindrome(self, n: int) -> int:
        # print(SPECIAL_PALINDROME)
        idx = bisect.bisect_right(SPECIAL_PALINDROME, n)
        return SPECIAL_PALINDROME[idx]
        