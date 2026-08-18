'''
=== 839. Similar String Groups ===

Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.
For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".
Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.
We are given a list A of strings.  Every string in A is an anagram of every other string in A.  How many groups are there?

Example 1:
    Input: A = ["tars","rats","arts","star"]
    Output: 2
 
Constraints:
    1. 1 <= A.length <= 2000
    2. 1 <= A[i].length <= 1000
    3. A.length * A[i].length <= 20000
    4. All words in A consist of lowercase letters only.
    5. All words in A have the same length and are anagrams of each other.
    6. The judging time limit has been increased for this question.
'''
# === 3688ms(59.66%) && 17.3MB(38.20%) === #
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            if root1 != root2:
                if rank[root1] < rank[root2]:
                    parent[root1] = root2
                elif rank[root2] < rank[root1]:
                    parent[root2] = root1 
                else:
                    parent[root1] = root2
                    rank[root2]  += 1
                    
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def similar_words(word):
            s_words = set()
            for i in range(len(word)):
                for j in range(i + 1, len(word)):
                    s_words.add(word[:i] + word[j] + word[i+1:j] + word[i] + word[j+1:])
            return s_words
        
        def is_similar(word1, word2):
            diff, c1, c2 = 0, set(), set()
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1
                    c1.add(word1[i])
                    c2.add(word2[i])
                if diff > 2: return False
            return True if c1 == c2 else False
            
        parent, rank = {a:a for a in A}, {a:0 for a in A}
        if len(A) > len(A[0]):
            # O(N * K^2)
            cache = set(A)
            for a in A:
                for s_word in similar_words(a):
                    if s_word in cache:
                        union(a, s_word)        
        else:
            # O(N^2 * K)
            for i, a in enumerate(A):
                for j in range(i + 1, len(A)):
                    if is_similar(A[i], A[j]):
                        union(A[i], A[j])
                            
        groups = collections.defaultdict(int)
        for word in parent:
            groups[find(word)] += 1
        return len(groups)