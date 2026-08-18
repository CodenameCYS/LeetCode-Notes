'''
# === 655. Print Binary Tree === #

Print a binary tree in an m*n 2D string array following these rules:
1. The row number m should be equal to the height of the given binary tree.
2. The column number n should always be an odd number.
3. The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
4. Each unused space should contain an empty string "".
5. Print the subtrees following the same rules.

Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]

Example 2:
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]

Example 3:
Input:
      1
     / \
    2   5
   / 
  3 
 / 
4 
Output:
[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]

- Note: The height of binary tree is in the range of [1, 10].
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# === 36ms(29.68%) && 12.7MB(100%) === #
class Solution:
    def align_print_tree(self, p1, p2):
        def expand(line, delta):
            delta = [""]*delta
            ans = []
            for it in line:
                ans.extend(delta+[it])
            ans.extend(delta)
            return ans
        
        l1 = len(p1); l2 = len(p2)
        l = max(l1, l2)
        if l1 < l:
            delta = 2**(l-l1) -1
            p1 = [expand(it, delta) for it in p1]
            p1 += [[""]*(2**l-1)] * (l-l1)
        if l2 < l:
            delta = 2**(l-l2) - 1
            p2 = [expand(it, delta) for it in p2]
            p2 += [[""]*(2**l-1)] * (l-l2)
        return p1,p2
    
    def printTree(self, root: TreeNode) -> List[List[str]]:
        if root is None:
            return []
        p1 = self.printTree(root.left)
        p2 = self.printTree(root.right)
        p1,p2 = self.align_print_tree(p1, p2)
        if p1 == []:
            return [[str(root.val)]]
        else:
            l = 2**len(p1)-1
            ans = [[""]*l + [str(root.val)] + [""]*l]
            ans += [it1 + [""] + it2 for it1,it2 in zip(p1,p2)]
            return ans