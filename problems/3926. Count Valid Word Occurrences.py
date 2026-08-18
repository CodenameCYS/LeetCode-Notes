'''
=== 3926. Count Valid Word Occurrences ===

You are given an array of strings chunks. The strings are concatenated in order to form a single string s.
You are also given an array of strings queries.
A word is defined as a substring of s that:
    - consists of lowercase English letters ('a' to 'z'),
    - may include hyphens ('-') only if each hyphen is surrounded by lowercase English letters, and
    - is not part of a longer substring that also satisfies the above conditions.
Any character that is not a lowercase English letter or a valid hyphen acts as a separator.
Return an integer array ans such that ans[i] is the number of occurrences of queries[i] as a word in s.
A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
    Input: chunks = ["hello wor","ld hello"], queries = ["hello","world","wor"]
    Output: [2,1,0]
    Explanation:
    Concatenating all strings in chunks gives s = "hello world hello".
    The valid words in s are "hello" which appears twice and "world" which appears once.
    Thus, the ans = [2, 1, 0].
Example 2:
    Input: chunks = ["a--b a-","-c"], queries = ["a","b","c"]
    Output: [2,1,1]
    Explanation:
    Concatenating all strings in chunks gives s = "a--b a--c".
    The valid words in s are "a" which appears twice, "b" which appears once, and "c" which appears once.
    Thus, the ans = [2, 1, 1].
Example 3:
    Input: chunks = ["hello"], queries = ["hello","ell"]
    Output: [1,0]
    Explanation:
    The valid word in s is "hello" which appears once.
    Thus, the ans = [1, 0].
 
Constraints:
    1. 1 <= chunks.length <= 105
    2. 1 <= chunks[i].length <= 105​​​​​​​
    3. chunks[i] may consist of lowercase English letters, spaces, and hyphens.
    4. The total length of all strings in chunks does not exceed 105
    5. 1 <= queries.length <= 105
    6. 1 <= queries[i].length <= 105​​​​​​​
    7. queries[i] is a valid word
    8. The total length of all strings in queries does not exceed 105
'''
# ===  === #
class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        s = "".join(chunks)
        cnt = defaultdict(int)
        cache = []
        for ch in s:
            if ch not in string.ascii_lowercase and ch != "-":
                word = "".join(cache).strip("-")
                cnt[word] += 1
                cache = []
            elif ch == "-":
                if cache == []:
                    continue
                elif cache[-1] == "-":
                    word = "".join(cache).strip("-")
                    cnt[word] += 1
                    cache = []
                else:
                    cache.append(ch)
            else:
                cache.append(ch)
        word = "".join(cache).strip("-")
        cnt[word] += 1
        cache = []

        return [cnt[w] for w in queries]