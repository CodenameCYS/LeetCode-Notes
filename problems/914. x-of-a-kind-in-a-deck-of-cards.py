'''
=== 914. x-of-a-kind-in-a-deck-of-cards ===

In a deck of cards, each card has an integer written on it.
Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:
- Each group has exactly X cards.
- All the cards in each group have the same integer.
 
Example 1:
Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]

Example 2:
Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.

Example 3:
Input: [1]
Output: false
Explanation: No possible partition.

Example 4:
Input: [1,1]
Output: true
Explanation: Possible partition [1,1]

Example 5:
Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]
'''
class Solution:
    def gcd(self, a,b):
        # a作为除数 必须大于b
        a, b = (a, b) if a >=b else (b, a)
        while b:
            a,b = b,a%b
        return a
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        g = {}
        for x in deck:
            if x in g.keys():
                g[x] += 1
            else:
                g[x] = 1
        minimum = len(deck)
        for x in g.keys():
            minimum = self.gcd(g[x], minimum)
        if minimum == 1:
            return False
        else:
            return True