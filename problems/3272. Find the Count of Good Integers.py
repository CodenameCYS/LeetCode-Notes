'''
=== 3272. Find the Count of Good Integers ===

You are given two positive integers n and k.
An integer x is called k-palindromic if:
    - x is a palindrome.
    - x is divisible by k.
An integer is called good if its digits can be rearranged to form a k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a k-palindromic integer.
Return the count of good integers containing n digits.
Note that any integer must not have leading zeros, neither before nor after rearrangement. For example, 1010 cannot be rearranged to form 101.

Example 1:
    Input: n = 3, k = 5
    Output: 27
    Explanation:
    Some of the good integers are:
    - 551 because it can be rearranged to form 515.
    - 525 because it is already k-palindromic.
Example 2:
    Input: n = 1, k = 4
    Output: 2
    Explanation:
    The two good integers are 4 and 8.
Example 3:
    Input: n = 5, k = 6
    Output: 2468

Constraints:
    1. 1 <= n <= 10
    2. 1 <= k <= 9
'''
# === 1356ms && 46.9MB === #
@lru_cache(None)
def is_valid(sub):
    if sub == "":
        return True
    cnt = Counter(sub)
    s = [v%2 for v in cnt.values()]
    return sum(s) <= 1

@lru_cache(None)
def dp(idx, remain):
    if remain == 0:
        return [""]
    elif idx == 9:
        return ["9" * remain]
    ans = []
    for i in range(remain+1):
        subs = [str(idx) * i + sub for sub in dp(idx+1, remain-i)]
        subs = [sub for sub in subs if is_valid(sub)]
        ans += subs
    return ans

@lru_cache(None)
def is_possible_devide_by_k(sub, k):
    if len(sub) == 1:
        return int(sub) % k == 0 and sub != "0"
    if Counter(sub)["0"] >= len(sub)-1:
        return False
    if k == 1:
        return True
    if k == 3 or k == 9:
        return sum(int(ch) for ch in sub) % k == 0
    if k == 5:
        return Counter(sub)["5"] > 1
    cnt = Counter(sub)
    pair = "".join(ch * (v//2) for ch, v in cnt.items())
    unique = [ch for ch, v in cnt.items() if v % 2 == 1]
    unique = unique[0] if len(unique) > 0 else ""
    # print(pair, unique, k, type(pair), type(unique), type(k))
    return any(int("".join(sub) + unique + "".join(sub[::-1])) % k == 0 for sub in permutations(pair) if not ("".join(sub) + unique + "".join(sub[::-1])).startswith("0"))

@lru_cache(None)
def count_fn(sub, k):
    ans = 0
    if is_possible_devide_by_k(sub, k):
        # if k == 1:
        #     print(sub)
        n = len(sub)
        cnt = Counter(sub)
        c = (n-cnt["0"]) * math.factorial(n-1)
        for v in cnt.values():
            c = c // math.factorial(v)
        ans += c
    return ans
    

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        all_possible_substrings = dp(0, n)
        # print(all_possible_substrings)
        return sum(count_fn(sub, k) for sub in all_possible_substrings)
        
        
        