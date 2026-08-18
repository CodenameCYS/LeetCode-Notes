'''
=== 3389. Minimum Operations to Make Character Frequencies Equal ===

You are given a string s.
A string t is called good if all characters of t occur the same number of times.
You can perform the following operations any number of times:
    - Delete a character from s.
    - Insert a character in s.
    - Change a character in s to its next letter in the alphabet.
Note that you cannot change 'z' to 'a' using the third operation.
Return the minimum number of operations required to make s good.

Example 1:
    Input: s = "acab"
    Output: 1
    Explanation:
    We can make s good by deleting one occurrence of character 'a'.
Example 2:
    Input: s = "wddw"
    Output: 0
    Explanation:
    We do not need to perform any operations since s is initially good.
Example 3:
    Input: s = "aaabc"
    Output: 2
    Explanation:
    We can make s good by applying these operations:
    Change one occurrence of 'a' to 'b'
    Insert one occurrence of 'c' into s

Constraints:
    1. 3 <= s.length <= 2 * 104
    2. s contains only lowercase English letters.
'''
# === 1115ms && 19.8MB === #
class Solution:
    def makeStringGood(self, s: str) -> int:
        cnt = Counter(s)
        # print(cnt)
        
        @lru_cache(None)
        def count_op(tgt):
            nums = [cnt[ch] for ch in string.ascii_lowercase]
            # need_show = (cnt['a'] == 4 and cnt['x'] == 8 and cnt['z'] == 1 and tgt >= cnt['a'])
            
            @lru_cache(None)
            def dfs(idx, nxt):
                if idx == 25:
                    current = nums[idx] + nxt
                    return min(current, abs(tgt-current))
                ans = math.inf
                
                current = nums[idx] + nxt
                nxt = nums[idx+1]
                if current == 0 or current == tgt:
                    return dfs(idx+1, 0)
                # if need_show:
                #     print(f"dfs :: idx={idx}, current={current}, nxt={nxt}")
                
                if nxt == 0 or nxt >= tgt:
                    ans = min(ans, min(current, abs(current-tgt)) + dfs(idx+1, 0))
                elif current > tgt:
                    ans = min(
                        ans, 
                        current-tgt + dfs(idx+1, 0),
                        current-tgt + dfs(idx+1, min(tgt-nxt, current-tgt))
                    )
                else:
                    ans = min(
                        ans, 
                        tgt-current + dfs(idx+1, 0),
                        current + dfs(idx+1, 0),
                        current + dfs(idx+1, min(tgt-nxt, current))
                    )
                # if need_show:
                #     print(f"dfs :: idx={idx}, current={current}, next={nxt}, ans={ans}")
                return ans
            
            ans = dfs(0, 0)
            # print(f"tgt = {tgt}, op num = {ans}")
            return ans              
            
        ans = min(count_op(i) for i in range(1, max(cnt.values())+1))
        # print("=" * 10)
        return ans
        