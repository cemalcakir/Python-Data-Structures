class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, val):
        "Inserting a value in bst."
        if val <= self.data:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BST(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BST(val)

    def contains(self, val):
        "Checks whether the given value is in BST or not."
        if self.data == val:
            return True
        elif val <= self.data:
            if self.left:
                return self.left.contains(val)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(val)
            else:
                return False

    def print_in_order(self):
        "Prints bst in order."
        if self.left:
            self.left.print_in_order()
        print(self.data)
        if self.right:
            self.right.print_in_order()


def sum_of_bst(bst):
    "Returns sum of BST."
    if not bst:
        return 0
    return bst.data + sum_of_bst(bst.left) + sum_of_bst(bst.right)


def is_bst_valid(node, mini=float('-inf'), maxi=float('inf')):
    "Check out whether the BST is valid or not."
    if not node:
        return True
    if node.data < mini or node.data > maxi:
        return False
    return is_bst_valid(node.left, mini, node.data - 1) and is_bst_valid(node.right, node.data + 1, maxi)


def trim_bst(bst, low, high):
    "Trims BST with given values."
    if not bst:
        return None
    if bst.data > high:
        return trim_bst(bst.right, low, high)
    if bst.data < low:
        return trim_bst(bst.left, low, high)
    bst.left = trim_bst(bst.left, low, high)
    bst.right = trim_bst(bst.right, low, high)
    return bst
