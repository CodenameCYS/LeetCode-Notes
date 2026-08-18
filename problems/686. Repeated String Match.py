'''
=== 686. Repeated String Match ===

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.
For example, with A = "abcd" and B = "cdabcdab".
Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
    - The length of A and B will be between 1 and 10000.
'''
# === 28ms(97.06%) && 12.9MB(100%) === #
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if A.find(B) != -1:
            return 1
        s = B.split(A)
        if len(s) == 1:
            return 2 if (A+A).find(B) != -1 else -1
        ans = 0
        ed = s.pop()
        if ed != "":
            if A.startswith(ed):
                ans += 1
            else:
                return -1
        st = s.pop(0)
        if st != "":
            if A.endswith(st):
                ans += 1
            else:
                return -1
        if all(it == "" for it in s):
            return ans + len(s) + 1
        else:
            return -1
            