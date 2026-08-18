'''
=== 2213. Longest Substring of One Repeating Character ===

You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.
The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].
Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.

Example 1:
    Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
    Output: [3,3,4]
    Explanation: 
    - 1st query updates s = "bbbacc". The longest substring consisting of one repeating character is "bbb" with length 3.
    - 2nd query updates s = "bbbccc". 
    The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
    - 3rd query updates s = "bbbbcc". The longest substring consisting of one repeating character is "bbbb" with length 4.
    Thus, we return [3,3,4].
Example 2:
    Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
    Output: [2,3]
    Explanation:
    - 1st query updates s = "abazz". The longest substring consisting of one repeating character is "zz" with length 2.
    - 2nd query updates s = "aaazz". The longest substring consisting of one repeating character is "aaa" with length 3.
    Thus, we return [2,3].
 
Constraints:
    1. 1 <= s.length <= 105
    2. s consists of lowercase English letters.
    3. k == queryCharacters.length == queryIndices.length
    4. 1 <= k <= 105
    5. queryCharacters consists of lowercase English letters.
    6. 0 <= queryIndices[i] < s.length
'''
# === 2058ms && 34MB === #
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        pre = ""
        cnt = 0
        n = len(s)
        seq = []
        nums = []
        for i, ch in enumerate(s):
            if ch == pre:
                cnt += 1
            else:
                if pre != "":
                    nums.append(cnt)
                    seq.append((i-1, pre, cnt))
                pre = ch
                cnt = 1
        seq.append((n-1, pre, cnt))
        nums.append(cnt)
        nums = sorted(nums)
        # print(nums, seq)
        
        def query(idx, ch):
            nonlocal nums, seq
            loc = bisect.bisect_left(seq, (idx, "", 0))
            ed, ch0, cnt = seq[loc]
            
            if ch0 != ch and seq[loc][0] == idx:
                if cnt == 1:
                    seq[loc] = (idx, ch, 1)
                else:
                    seq[loc] = (ed-1, ch0, cnt-1)
                    seq.insert(loc+1, (idx, ch, 1))
                    nums.pop(bisect.bisect_left(nums, cnt))
                    bisect.insort(nums, cnt-1)
                    bisect.insort(nums, 1)
                    loc = loc + 1
            elif ch0 != ch and seq[loc][0] != idx:
                bg = 0 if loc == 0 else seq[loc-1][0]+1
                ed, ch0, cnt = seq[loc]
                # print("***", loc, bg, ed, ch0, cnt, ch, idx)
                if bg != idx:
                    seq.pop(loc)
                    seq.insert(loc, (ed, ch0, ed-idx))
                    seq.insert(loc, (idx, ch, 1))
                    seq.insert(loc, (idx-1, ch0, idx-bg))
                    nums.pop(bisect.bisect_left(nums, cnt))
                    bisect.insort(nums, ed-idx)
                    bisect.insort(nums, idx-bg)
                    bisect.insort(nums, 1)
                    loc = loc + 1
                else:
                    seq.pop(loc)
                    seq.insert(loc, (ed, ch0, ed-idx))
                    seq.insert(loc, (idx, ch, 1))
                    nums.pop(bisect.bisect_left(nums, cnt))
                    bisect.insort(nums, ed-idx)
                    bisect.insort(nums, 1)
            # print("***", idx, ch, loc, nums, seq)
            if loc + 1 < len(seq) and seq[loc+1][1] == ch:
                ed, _, cnt = seq[loc+1]
                seq.pop(loc+1)
                seq[loc] = (ed, ch, cnt+1)
                nums.pop(bisect.bisect_left(nums, cnt))
                nums.pop(bisect.bisect_left(nums, 1))
                bisect.insort(nums, cnt+1)
            if loc - 1 >= 0 and seq[loc-1][1] == ch:
                bg = seq[loc-2][0] + 1 if loc-2 >= 0 else 0
                _, _, cnt = seq[loc-1]
                ed, _, cnt2 = seq[loc]
                seq.pop(loc)
                seq[loc-1] = (ed, ch, ed-bg+1)
                nums.pop(bisect.bisect_left(nums, cnt))
                nums.pop(bisect.bisect_left(nums, cnt2))
                bisect.insort(nums, ed-bg+1)
            # print(idx, ch, nums, seq)
            # print("=" * 5)
            return nums[-1]
                
        k = len(queryIndices)
        return [query(queryIndices[i], queryCharacters[i]) for i in range(k)]
            
                
        