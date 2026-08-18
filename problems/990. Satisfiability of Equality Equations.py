'''
=== 990. Satisfiability of Equality Equations ===

Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.
Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

Example 1:
    Input: ["a==b","b!=a"]
    Output: false
    Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.
Example 2:
    Input: ["b==a","a==b"]
    Output: true
    Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
Example 3:
    Input: ["a==b","b==c","a==c"]
    Output: true
Example 4:
    Input: ["a==b","b!=c","c==a"]
    Output: false
Example 5:
    Input: ["c==c","b==d","x!=z"]
    Output: true
 
Note:
    1. 1 <= equations.length <= 500
    2. equations[i].length == 4
    3. equations[i][0] and equations[i][3] are lowercase letters
    4. equations[i][1] is either '=' or '!'
    5. equations[i][2] is '='
'''
# === 44 ms & 12.4 MB (53.35%) === #
class Solution:
    def findSet(self, a, sets):
        aloc = -1
        for i, s in sets.items():
            if a in s:
                aloc = i
                break
        return aloc
      
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        def findmax(sets):
            if len(sets) == 0:
                return 0
            else:
                return max(sets.keys()) + 1
            
        ansset = {}
        for equation in equations:
            a = equation[0]
            b = equation[3]
            relation = equation[1]
            if relation == '=':
                aloc = self.findSet(a, ansset)
                bloc = self.findSet(b, ansset)
                # print(aloc, bloc)
                if aloc == -1 and bloc == -1:
                    ansset[findmax(ansset)] = set([a,b])
                elif aloc == -1 and bloc != -1:
                    ansset[bloc].add(a)
                elif aloc != -1 and bloc == -1:
                    ansset[aloc].add(b)
                else:
                    if aloc != bloc:
                        ansset[aloc].update(ansset[bloc])
                        ansset.pop(bloc)
        # print(ansset)
        for equation in equations:
            a = equation[0]
            b = equation[3]
            relation = equation[1]
            if relation == '!':
                if a == b:
                    return False
                aloc = self.findSet(a, ansset)
                bloc = self.findSet(b, ansset)
                if aloc == bloc and not (aloc == -1 and bloc == -1):
                    return False
                if aloc == -1:
                    ansset[findmax(ansset)] = set(a)
                if bloc == -1:
                    ansset[findmax(ansset)] = set(b)
        return True
                