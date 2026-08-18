'''
=== 3664. Two-Letter Card Game ===

You are given a deck of cards represented by a string array cards, and each card displays two lowercase letters.
You are also given a letter x. You play a game with the following rules:
    - Start with 0 points.
    - On each turn, you must find two compatible cards from the deck that both contain the letter x in any position.
    - Remove the pair of cards and earn 1 point.
    - The game ends when you can no longer find a pair of compatible cards.
Return the maximum number of points you can gain with optimal play.
Two cards are compatible if the strings differ in exactly 1 position.

Example 1:
    Input: cards = ["aa","ab","ba","ac"], x = "a"
    Output: 2
    Explanation:
    On the first turn, select and remove cards "ab" and "ac", which are compatible because they differ at only index 1.
    On the second turn, select and remove cards "aa" and "ba", which are compatible because they differ at only index 0.
    Because there are no more compatible pairs, the total score is 2.
Example 2:
    Input: cards = ["aa","ab","ba"], x = "a"
    Output: 1
    Explanation:
    On the first turn, select and remove cards "aa" and "ba".
    Because there are no more compatible pairs, the total score is 1.
Example 3:
    Input: cards = ["aa","ab","ba","ac"], x = "b"
    Output: 0
    Explanation:
    The only cards that contain the character 'b' are "ab" and "ba". However, they differ in both indices, so they are not compatible. Thus, the output is 0.

Constraints:
    1. 2 <= cards.length <= 105
    2. cards[i].length == 2
    3. Each cards[i] is composed of only lowercase English letters between 'a' and 'j'.
    4. x is a lowercase English letter between 'a' and 'j'.
'''
# === 68ms && 36.24MB === #
class Solution:
    def score(self, cards: List[str], x: str) -> int:
        cnt = Counter(cards)
        st = [it for it in cnt.items() if it[0][0] == x and it[0] != x+x]
        st = sorted(st, key=lambda x: x[1])
        st_tot = sum(it[1] for it in st)
        ed = [it for it in cnt.items() if it[0][1] == x and it[0] != x+x]
        ed = sorted(ed, key=lambda x: x[1])
        ed_tot = sum(it[1] for it in ed)
        bo = cnt[x+x]

        ans = 0
        if len(st) > 0 and st[-1][1] > st_tot // 2:
            ex = min(bo, st[-1][1]*2 - st_tot)
            st[-1] = (st[-1][0], st[-1][1]-ex)
        elif len(st) > 0 and st_tot % 2 == 1:
            ex = min(bo, 1)
            st[-1] = (st[-1][0], st[-1][1]-ex)
        else:
            ex = 0
        ans += ex
        bo -= ex
        st_tot -= ex
        if len(ed) > 0 and ed[-1][1] > ed_tot // 2:
            ex = min(bo, ed[-1][1]*2 - ed_tot)
            ed[-1] = (ed[-1][0], ed[-1][1]-ex)
        elif len(ed) > 0 and ed_tot % 2 == 1:
            ex = min(bo, 1)
            ed[-1] = (ed[-1][0], ed[-1][1]-ex)
        else:
            ex = 0
        ans += ex
        bo -= ex
        ed_tot -= ex

        def count(arr, bo):
            if len(arr) == 0:
                return 0, bo
            arr = sorted(arr, key=lambda x: x[1])
            tot = sum(it[1] for it in arr)
            if tot // 2 >= arr[-1][1]:
                ans = tot // 2
                delta = 0
                if bo > 0 and tot % 2 == 1:
                    delta = 1
                    bo -= delta
            else:
                ans = tot - arr[-1][1]
                delta = arr[-1][1] - ans
                delta = min(delta, bo)
                bo -= delta
            if bo > 0 and bo <= 2 * ans:
                ns = (2*ans + bo) // 2
                bo = bo - (ns-ans)*2
                ans = ns
            ans += delta
                
            return ans, bo

        def fn(arr1, arr2, bo):
            s1, bo = count(arr1, bo)
            # print(arr1, bo, s1)
            s2, bo = count(arr2, bo)
            # print(arr2, bo, s2)
            # print(s1+s2)
            return s1 + s2

        return ans + max(fn(st, ed, bo), fn(ed, st, bo))
