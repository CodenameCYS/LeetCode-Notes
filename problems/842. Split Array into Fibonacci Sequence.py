'''
=== 842. Split Array into Fibonacci Sequence ===

Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].
Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:
    - 0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
    - F.length >= 3;
    - and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.
Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:
    Input: "123456579"
    Output: [123,456,579]
Example 2:
    Input: "11235813"
    Output: [1,1,2,3,5,8,13]
Example 3:
    Input: "112358130"
    Output: []
    Explanation: The task is impossible.
Example 4:
    Input: "0123"
    Output: []
    Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:
    Input: "1101111"
    Output: [110, 1, 111]
    Explanation: The output [11, 0, 11, 11] would also be accepted.

Note:
    1. 1 <= S.length <= 200
    2. S contains only digits.
'''
MAX = 2**31
# === 112ms(38.03%) && 13.8MB(65.28%) === #
class Solution:
    def is_fibonacci(self, a, b, S):
        if S == "":
            return True
        s = str(a + b)
        if not S.startswith(s) or a+b >= MAX:
            return False
        l = len(s)
        return self.is_fibonacci(b, a+b, S[l:])
    
    def build_fibonacci(self, a, b, S):
        if S == "":
            return [a, b]
        n = len(str(a+b))
        return [a] + self.build_fibonacci(b, a+b, S[n:])
    
    def splitIntoFibonacci(self, S: str) -> List[int]:
        n = len(S)
        if S[0] == '0':
            if S[1] == '0':
                if self.is_fibonacci(0, 0, S[2:]):
                    return self.build_fibonacci(0, 0, S[2:])
            else:
                for i in range(2, (n+1)//2+1):
                    b = int(S[1:i])
                    # print(b)
                    if self.is_fibonacci(0, int(S[1:i]), S[i:]):
                        return self.build_fibonacci(0, int(S[1:i]), S[i:])
            return []
        for i in range(1, (n+1)//2):
            a = int(S[:i])
            if S[i] == '0':
                if self.is_fibonacci(a, 0, S[i+1:]):
                    return self.build_fibonacci(a, 0, S[i+1:])
            else:
                for j in range(i+1, i+(n-i)//2+1):
                    b = int(S[i:j])
                    # print(a, b)
                    if self.is_fibonacci(a, b, S[j:]):
                        return self.build_fibonacci(a, b, S[j:])
        return []
        