class Node:
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        print("info -> membangun struktur gudang")
        self.root              = Node("A")
        self.root.left         = Node("B")
        self.root.right        = Node("C")
        self.root.left.left    = Node("D")
        self.root.left.right   = Node("E")
        self.root.right.right  = Node("F")
        print("info-> struktur berhasil dibuat")

    def traverse_preorder(self, node, result=[]):
        if node:
            result.append(node.data)
            self.traverse_preorder(node.left, result)
            self.traverse_preorder(node.right, result)
        return result

    def traverse_inorder(self, node, result=[]):
        if node:
            self.traverse_inorder(node.left, result)
            result.append(node.data)
            self.traverse_inorder(node.right, result)
        return result

    def traverse_postorder(self, node, result=[]):
        if node:
            self.traverse_postorder(node.left, result)
            self.traverse_postorder(node.right, result)
            result.append(node.data)
        return result

    def get_leaf_nodes(self, node, result=[]):
        if node:
            if not node.left and not node.right:
                result.append(node.data)
            self.get_leaf_nodes(node.left, result)
            self.get_leaf_nodes(node.right, result)
        return result


tree = BinaryTree()

print('\n SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI" ')

tree.insert_manual()

print("\nhasil audit:")
print("1. PreOrder  :", " - ".join(tree.traverse_preorder(tree.root, [])))
print("2. InOrder   :", " - ".join(tree.traverse_inorder(tree.root, [])))
print("3. PostOrder :", " - ".join(tree.traverse_postorder(tree.root, [])))
print("\n data -> gudang ujung (leaf nodes):", ", ".join(tree.get_leaf_nodes(tree.root, [])))

print("Audit Selesai!\n")