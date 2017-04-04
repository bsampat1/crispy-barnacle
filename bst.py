#!/usr/bin/python


class Node:

    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class Tree:

    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif val < node.v and node.l is not None:
            self._find(val, node.l)
        elif val > node.v and node.r is not None:
            self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print str(node.v) + ' '
            self._printTree(node.r)

    def delete(self, x):
        '''Remove item x from the tree.'''
        p, q = self.__find_and_parent(x)
        if p is None: raise KeyError      # x not found

        # has two children
        if None not in (p.left, p.right):
            r, q = self.__find_min(p.right, p)
            p.data = r.data
            p = r    # Note: below we delete this new p

        # is leaf
        if (p.left, p.right) == (None,None):
            if q is None: self.root = None
            elif p.data < q.data: q.left = None
            else: q.right = None

        # has only one child
        elif None in (p.left, p.right):
            # c is the non-None child
            c = p.left
            if c is None: c = p.right

            if q is None: self.root = c
            elif p.data < q.data: q.left = c
            else: q.right = c

    def __find_min(self, p, q):
        '''Return the smallest element under node p, and its parent.
        q should be the parent of p'''
        if p is None: return None
        while p.left is not None:
            q = p
            p = p.left
        return p, q


    def __find_and_parent(self, x):
        '''Search for x, returning the node containing x and its parent.
        If x doesn't exist, we return None and x's would-be parent.'''
        q = None           # parent
        p = self.root      # current node
        while p is not None and p.data != x:
            q = p
            if x < p.data:
                p = p.left
            else:
                p = p.right
        return p, q


if __name__ == '__main__':
    #     3
    # 0     4
    #   2      8
    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.delete(4)
    tree.add(2)
    tree.printTree()
    print (tree.find(3)).v
    print tree.find(10)
    tree.deleteTree()
    tree.printTree()
