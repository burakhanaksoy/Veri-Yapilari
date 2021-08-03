class Node:

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    _arr = []

    def __init__(self, root=None):
        self.root = root

    def insert(self, val, node=None):
        if self.root == None:
            self.root = Node(val)
        else:
            if node is None:
                node = self.root
            if val < node.val:
                if node.left == None:
                    node.left = Node(val)
                    return
                self.insert(val, node=node.left)

            if val > node.val:
                if node.right == None:
                    node.right = Node(val)
                    return
                self.insert(val, node=node.right)

    def traverse(self, node=None):
        # Traverse using "prefix" L, N, R
        if node is None:
            pass
        else:
            self.traverse(node.left)  # L
            self._arr.append(node.val)  # N
            self.traverse(node.right)  # R

    def display(self):
        self._arr = []
        self.traverse(self.root)
        print(self._arr)

    def search(self, node, val):
        # Base Cases: root is null or key is present at root
        if node is None or node.val == val:
            if not node:
                return False
            return True

        # Key is greater than root's key
        if node.val < val:
            return self.search(node.right, val)

        # Key is smaller than root's key
        return self.search(node.left, val)

    def find_min(self, node=None):
        if not node.left:
            return node.val
        return self.find_min(node.left)

    def find_max(self, node=None):
        if not node.right:
            return node.val
        return self.find_max(node.right)

    def delete(self, val, node):
        if node is None:
            return node
        if val < node.val:
            node.left = self.delete(val, node.left)
        elif val > node.val:
            node.right = self.delete(val, node.right)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.find_min(node.right)
            node.val = temp
            node.right = self.delete(temp, node.right)

        return node


def main():
    bst = BST()
    bst.insert(8)
    bst.insert(3)
    bst.insert(10)
    bst.insert(1)
    bst.insert(6)
    bst.insert(4)
    bst.insert(7)
    bst.insert(14)
    bst.insert(13)
    bst.display()
    print(bst.search(bst.root, 13))
    print(bst.find_min(bst.root))
    print(bst.find_max(bst.root))
    bst.delete(6, bst.root)
    bst.display()


if __name__ == '__main__':
    main()
