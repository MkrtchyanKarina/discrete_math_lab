class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.balance_factor = 0
        self.height = 1  # Добавляем высоту узла
        self.value = value


class AVLTree:
    def push(self, root, value: int):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.push(root.left, value)
        else:
            root.right = self.push(root.right, value)

        # Обновление высоты узла
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Обновляем баланс
        root.balance_factor = self.get_balance(root)

        # Проверка на дисбаланс и выполнение поворотов, если необходимо
        if root.balance_factor > 1:  # Левый поддерево превышает
            if value < root.left.value:  # Левый левый случай
                return self.right_rotate(root)
            else:  # Левый правый случай
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if root.balance_factor < -1:  # Правый поддерево превышает
            if value > root.right.value:  # Правый правый случай
                return self.left_rotate(root)
            else:  # Правый левый случай
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def right_rotate(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        # Обновление высот
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        # Обновление баланса
        root.balance_factor = self.get_balance(root)
        new_root.balance_factor = self.get_balance(new_root)

        return new_root

    def left_rotate(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root

        # Обновление высот
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        # Обновление баланса
        root.balance_factor = self.get_balance(root)
        new_root.balance_factor = self.get_balance(new_root)

        return new_root

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)




    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.value, end=' ')
            self.in_order(root.right)

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.print_tree(node.left, level + 1)

if __name__ == "__main__":
    tree = AVLTree()
    root = None

    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        root = tree.push(root, key)

    print("In-order Traversal:")
    tree.in_order(root)
    print("\nTree Structure:")
    tree.print_tree(root)


