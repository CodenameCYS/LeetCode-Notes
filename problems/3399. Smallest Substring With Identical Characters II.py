'''
=== 3399. Smallest Substring With Identical Characters II ===

You are given a binary string s of length n and an integer numOps.
You are allowed to perform the following operation on s at most numOps times:
    - Select any index i (where 0 <= i < n) and flip s[i]. If s[i] == '1', change s[i] to '0' and vice versa.
You need to minimize the length of the longest substring of s such that all the characters in the substring are identical.
Return the minimum length after the operations.
A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
    Input: s = "000001", numOps = 1
    Output: 2
    Explanation: 
    By changing s[2] to '1', s becomes "001001". The longest substrings with identical characters are s[0..1] and s[3..4].
Example 2:
    Input: s = "0000", numOps = 2
    Output: 1
    Explanation: 
    By changing s[0] and s[2] to '1', s becomes "1010".
Example 3:
    Input: s = "0101", numOps = 0
    Output: 1

Constraints:
    1. 1 <= n == s.length <= 105
    2. s consists only of '0' and '1'.
    3. 0 <= numOps <= n
'''
# === 1101ms && 80MB === #
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        
        def is_possible_at1():
            cnt0, cnt1 = 0, 0
            for i, ch in enumerate(s):
                if i % 2 == 0:
                    if ch == '0':
                        cnt1 += 1
                    else:
                        cnt0 += 1
                else:
                    if ch == '1':
                        cnt1 += 1
                    else:
                        cnt0 += 1
            return (cnt0 <= numOps or cnt1 <= numOps)
        
        if is_possible_at1():
            return 1
        
        def flip(ch):
            return "1" if ch == "0" else "0"
                
        @lru_cache(None)
        def is_possible(idx, digit, max_len, ops):
            if idx >= n:
                return True
            if s[idx] != digit:
                if ops == 0:
                    return False
                else:
                    ops -= 1
            if ops == 0:
                pre, cnt = digit, 1
                for j in range(idx+1, n):
                    if s[j] == pre:
                        cnt += 1
                    else:
                        cnt = 1
                    if cnt > max_len:
                        return False
                    pre = s[j]
                return True
            i = idx+1
            while i < min(n, idx+max_len):
                if s[i] != digit:
                    return is_possible(i, s[i], max_len, ops)
                i += 1
            return is_possible(i, flip(digit), max_len, ops)
                    
        def get_binary_split_answer():
            q = []
            pre, cnt = s[0], 0
            for ch in s:
                if ch == pre:
                    cnt += 1
                else:
                    if cnt > 2:
                        q.append(-cnt)
                    cnt = 1
                pre = ch
            if cnt > 2:
                q.append(-cnt)
            # print(q)
            heapq.heapify(q)
            for _ in range(numOps):
                if len(q) == 0:
                    break
                m = - heapq.heappop(q)
                l, r = m // 2, m-1 - (m//2)
                if l > 2:
                    heapq.heappush(q, -l)
                if r > 2:
                    heapq.heappush(q, -r)
            return -q[0] if len(q) > 0 else 2
            
        l = 1
        r = get_binary_split_answer()
        # print(l, r)
        while r-l > 1:
            # break
            m = (l+r) // 2
            # if is_possible(0, m, s[0], 0, numOps):
            if is_possible(0, s[0], m, numOps):
                r = m
            else:
                l = m
        # print("=" * 10)
        return r
        
        