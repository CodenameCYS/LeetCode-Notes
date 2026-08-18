'''
=== 433. Minimum Genetic Mutation ===

A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".
Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.
For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.
Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.
Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:
    1. Starting point is assumed to be valid, so it might not be included in the bank.
    2. If multiple mutations are needed, all mutations during in the sequence must be valid.
    3. You may assume start and end string is not the same.
 
Example 1:
    start: "AACCGGTT"
    end:   "AACCGGTA"
    bank: ["AACCGGTA"]
    return: 1
Example 2:
    start: "AACCGGTT"
    end:   "AAACGGTA"
    bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    return: 2
Example 3:
    start: "AAAAACCC"
    end:   "AACCCCCC"
    bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    return: 3
'''
# === 24ms(86.25%) && 12.7MB(100%) === #
class Solution:
    def diff(self, s1, s2):
        ans = 0
        for c1,c2 in zip(s1, s2):
            if c1 != c2:
                ans += 1
        # print("{} & {} == {}".format(s1, s2, ans))
        return ans
    
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        stack = [start]
        have_seen = {start:0}
        while stack != []:
            tmp = stack[0]
            stack = stack[1:]
            for s in bank:
                if s in have_seen.keys():
                    continue
                if self.diff(tmp, s) == 1:
                    if s == end:
                        return have_seen[tmp] + 1
                    else:
                        have_seen[s] = have_seen[tmp] + 1
                        stack.append(s)
        return -1