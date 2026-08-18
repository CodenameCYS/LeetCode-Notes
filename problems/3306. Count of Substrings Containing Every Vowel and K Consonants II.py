'''
=== 3306. Count of Substrings Containing Every Vowel and K Consonants II ===

You are given a string word and a non-negative integer k.
Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

Example 1:
    Input: word = "aeioqq", k = 1
    Output: 0
    Explanation:
    There is no substring with every vowel.
Example 2:
    Input: word = "aeiou", k = 0
    Output: 1
    Explanation:
    The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".
Example 3:
    Input: word = "ieaouqqieaouqq", k = 1
    Output: 3
    Explanation:
    The substrings with every vowel and one consonant are:
    word[0..5], which is "ieaouq".
    word[6..11], which is "qieaou".
    word[7..12], which is "ieaouq".
 
Constraints:
    1. 5 <= word.length <= 2 * 105
    2. word consists only of lowercase English letters.
    3. 0 <= k <= word.length - 5
'''
# === 6407ms && 25MB === #
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        
        next_consonants = [n for _ in range(n)]
        idx = n
        for i in range(n-1, -1, -1):
            next_consonants[i] = idx
            if word[i] not in "aeiou":
                idx = i
        
        i, j = 0, 0
        cnt = defaultdict(int)
        ans = 0
        while j < n:
            while j < n and (any(cnt[ch] <= 0 for ch in "aeiou") or cnt["c"] < k):
                if word[j] in "aeiou":
                    cnt[word[j]] += 1
                else:
                    cnt["c"] += 1
                j += 1
            
            while all(cnt[ch] > 0 for ch in "aeiou") and cnt["c"] >= k:
                if cnt["c"] == k and all(cnt[ch] > 0 for ch in "aeiou"):
                    # print(f"i={i}, j={j-1}, next_consonants={next_consonants[j-1]}, n={n}, cnt={cnt}")
                    ans += (next_consonants[j-1] - (j-1))
                if word[i] in "aeiou":
                    cnt[word[i]] -= 1
                else:
                    cnt["c"] -= 1
                i += 1
        # print("=" * 10)
        return ans