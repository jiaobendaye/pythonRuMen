class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def __iter__(self):
        # return TreeNodeIterator(self)
        return gen_tree_node(self)


class TreeNodeIterator():
    def __init__(self, tree: TreeNode):
        self._root = tree
        self._que = [self._root]

    def __next__(self):
        try:
            node = self._que.pop(0)
        except IndexError:
            raise StopIteration
        else:
            if node.left:
                self._que.append(node.left)
            if node.right:
                self._que.append(node.right)
        return node

    def __iter__(self):
        return self


def gen_tree_node(root: TreeNode):
    que = [root]
    while que:
        node = que.pop(0)
        yield node
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)


def make_simple_tree(rootVal, leftVal, rightVal):
    root = TreeNode(rootVal)
    root.left = TreeNode(leftVal)
    root.right = TreeNode(rightVal)
    return root


def make_basic_tree():
    """
        1
      /  \
     2    3
    / \  / \
   4   5 6  7
    """
    root = TreeNode(1)
    root.left = make_simple_tree(2, 4, 5)
    root.right = make_simple_tree(3, 6, 7)
    return root


def inorder_genrator(root: TreeNode):
    nodes = []

    def find_first(node: TreeNode):
        p = node
        while p:
            nodes.append(p)
            p = p.left
    find_first(root)
    while nodes:
        node = nodes.pop()
        yield node
        if node.right:
            find_first(node.right)


def inorder_traversal(root: TreeNode):
    out = []

    def inorder(branch: TreeNode):
        if not branch:
            return
        if branch.left:
            inorder(branch.left)
        out.append(branch.val)
        if branch.right:
            inorder(branch.right)
    inorder(root)
    return out


def test_inorder_traversal():
    t1 = make_basic_tree()
    print(inorder_traversal(t1))


def BFS(root: TreeNode):
    if not root:
        return None
    depth = 0
    que = []
    que.append(root)

    while que:
        for _ in range(len(que)):
            cur = que.pop(0)
            print(cur.val)
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
        depth += 1
        print('****', depth)
    return depth


def test_iter():
    root = make_basic_tree()
    # iterator = TreeNodeIterator(root)
    l1 = [node.val for node in root]
    print(l1)


def test_inorder_gen():
    t1 = make_basic_tree()
    assert [4, 2, 5, 1, 6, 3, 7] == [node.val for node in inorder_genrator(t1)]


def DFS(root: TreeNode):
    if not root:
        return 0
    stack = []
    stack.append((root, 1))
    ans_dep = 0
    while stack:
        curNode, curDep = stack.pop()
        print(curNode.val, curDep)
        if curDep > ans_dep:
            ans_dep = curDep
        if curNode.right:
            stack.append((curNode.left, curDep+1))
        if curNode.right:
            stack.append((curNode.right, curDep+1))
    return ans_dep


def depthOfTreeRecur(root: TreeNode):
    if not root:
        return 0
    return 1 + max(depthOfTreeRecur(root.left), depthOfTreeRecur(root.right))


class Solution():

    def _isleaf(self, node):
        if not node.left and not node.right:
            return True
        return False

    def _dfs(self, node: TreeNode, level):
        if not node:
            return

        if self._isleaf(node) and level > self.Max:
            self.Max = level
        self._dfs(node.left, level+1)
        self._dfs(node.right, level+1)

    def dpethOfDFS(self, root: TreeNode):
        if not root:
            return 0
        self.Max = 1
        self._dfs(root, 1)
        return self.Max


def preorder_traversal(root: TreeNode):
    out = []

    def preorder(branch: TreeNode):
        out.append(branch.val)
        if branch.left:
            preorder(branch.left)
        if branch.right:
            preorder(branch.right)
    preorder(root)
    return out


def test_preorder_traversal():
    t1 = make_basic_tree()
    assert [1, 2, 4, 5, 3, 6, 7] == preorder_traversal(t1)


def preorder_generator(root: TreeNode):
    visited = []
    nodes = [root]
    while nodes:
        node = nodes.pop()
        visited.append(node)
        yield node.val
        if node.left:
            nodes.append(node.left)

        while not nodes:
            if visited:
                vnode = visited.pop()
                if vnode.right:
                    nodes.append(vnode.right)
            else:
                break


def test_preorder_generator():
    t1 = make_basic_tree()
    assert [1, 2, 4, 5, 3, 6, 7] == [val for val in preorder_generator(t1)]


def post_traversal(root: TreeNode):
    out = []

    def postortder(branch: TreeNode):
        if not branch:
            return
        if branch.left:
            postortder(branch.left)
        if branch.right:
            postortder(branch.right)
        out.append(branch.val)
    postortder(root)
    return out


def test_postorder_traversal():
    t1 = make_basic_tree()
    assert [4, 5, 2, 6, 7, 3, 1] == post_traversal(t1)


def postorder_iter(root: TreeNode):
    """

    """
    if not root:
        return []
    out = []
    stack = [(root, False)]
    while stack:
        cur, visited = stack.pop()
        if visited:
            out.append(cur.val)
        else:
            stack.append((cur, True))
            if cur.right:
                stack.append((cur.right, False))
            if cur.left:
                stack.append((cur.left, False))
    return out


def test_postorder_iter():
    t1 = make_basic_tree()
    assert [4, 5, 2, 6, 7, 3, 1] == postorder_iter(t1)


def main():
    root = make_basic_tree()
    BFS(root)
    # print('dfs', DFS(root))
    test_iter()
    print('depthOfTreeRecur: ', depthOfTreeRecur(root))
    s = Solution()
    print(s.dpethOfDFS(root))
    test_inorder_gen()
    test_inorder_traversal()


if __name__ == "__main__":
    main()
