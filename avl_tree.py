class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self, array: list[int]):
        self.root = None
        for elem in array:
            self.root = self.push(self.root, elem)

    def push(self, root, value: int):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.push(root.left, value)
        else:
            root.right = self.push(root.right, value)


        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Левый правый случай
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Правый левый случай
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def right_rotate(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        # Обновляем высоты
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def left_rotate(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def result_in_order(self, root):
        if root:
            self.result_in_order(root.left)
            print(root.value, end=" ")
            self.result_in_order(root.right)

    def result_in_tree(self, root, level=0):
        if root:
            self.result_in_tree(root.left, level + 1)
            print(f'{" " * (4 * level)}-> {root.value}')
            self.result_in_tree(root.right, level + 1)

    def return_tree(self):
        self.result_in_tree(self.root)
        print()
        self.result_in_order(self.root)
        print()


def solve():
    answer = input("Введите элементы массива через пробел: ")
    try:
        array = list(map(int, answer.strip().split(" ")))
        tree = AVLTree(array)
        tree.return_tree()
        answer = input("Хотите продолжить? (Д/н): ").lower()
        if answer == "д" or answer == "l":
            return solve()
    except:
        answer = input("Неправильно введены данные. Хотите продолжить? (Д/н): ").lower()
        if answer == "д" or answer == "l":
            return solve()

if __name__ == "__main__":
    solve()