'''
=== 558. Quad Tree Intersection ===

A quadtree is a tree data in which each internal node has exactly four children: topLeft, topRight, bottomLeft and bottomRight. Quad trees are often used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions.
We want to store True/False information in our quad tree. The quad tree is used to represent a N * N boolean grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same. Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

For example, below are two quad trees A and B:
A:
    +-------+-------+   T: true
    |       |       |   F: false
    |   T   |   T   |
    |       |       |
    +-------+-------+
    |       |       |
    |   F   |   F   |
    |       |       |
    +-------+-------+
    topLeft: T
    topRight: T
    bottomLeft: F
    bottomRight: F
B:               
    +-------+---+---+
    |       | F | F |
    |   T   +---+---+
    |       | T | T |
    +-------+---+---+
    |       |       |
    |   T   |   F   |
    |       |       |
    +-------+-------+
    topLeft: T
    topRight:
        topLeft: F
        topRight: F
        bottomLeft: T
        bottomRight: T
    bottomLeft: T
    bottomRight: F
Your task is to implement a function that will take two quadtrees and return a quadtree that represents the logical OR (or union) of the two trees.
    A:                 B:                 C (A or B):
    +-------+-------+  +-------+---+---+  +-------+-------+
    |       |       |  |       | F | F |  |       |       |
    |   T   |   T   |  |   T   +---+---+  |   T   |   T   |
    |       |       |  |       | T | T |  |       |       |
    +-------+-------+  +-------+---+---+  +-------+-------+
    |       |       |  |       |       |  |       |       |
    |   F   |   F   |  |   T   |   F   |  |   T   |   F   |
    |       |       |  |       |       |  |       |       |
    +-------+-------+  +-------+-------+  +-------+-------+

Note:
    1. Both A and B represent grids of size N * N.
    2. N is guaranteed to be a power of 2.
    3. If you want to know more about the quad tree, you can refer to its wiki.
    4. The logic OR operation is defined as this: "A or B" is true if A is true, or if B is true, or if both A and B are true.
'''
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
# === 224ms(63.64%) && 13.3MB(100%) === #
class Solution:
    def merge(self, quadTree: 'Node'):
        if quadTree is None or quadTree.isLeaf:
            return 
        self.merge(quadTree.topLeft)
        self.merge(quadTree.topRight)
        self.merge(quadTree.bottomLeft)
        self.merge(quadTree.bottomRight)
        if quadTree.topLeft.isLeaf and quadTree.topRight.isLeaf and quadTree.bottomLeft.isLeaf and quadTree.bottomRight.isLeaf:
            if quadTree.topLeft.val and quadTree.topRight.val and quadTree.bottomLeft.val and quadTree.bottomRight.val:
                quadTree.val = True
                quadTree.isLeaf = True
            elif not quadTree.topLeft.val and not quadTree.topRight.val and not quadTree.bottomLeft.val and not quadTree.bottomRight.val:
                quadTree.val = False
                quadTree.isLeaf = True
        
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf and quadTree2.isLeaf:
            return Node(quadTree1.val or quadTree2.val, True, None, None, None, None)
        elif quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        elif quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1
        else:
            ans = Node(
                val = None, isLeaf = False,
                topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft),
                topRight = self.intersect(quadTree1.topRight, quadTree2.topRight),
                bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft),
                bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
            )
            self.merge(ans)
            return ans