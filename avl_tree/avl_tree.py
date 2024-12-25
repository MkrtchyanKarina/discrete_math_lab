
import pathlib
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.balance_factor = 0
        self.height = 1
        self.value = value



class AVLTree:
    def push(self, root, value: int):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.push(root.left, value)
        else:
            root.right = self.push(root.right, value)


        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))


        root.balance_factor = self.get_balance(root)


        if root.balance_factor > 1:
            if value < root.left.value:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if root.balance_factor < -1:
            if value > root.right.value:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def right_rotate(self, root):
        new_root = root.left
        root.left = None
        new_root.right = root

        root.height = 1 + self.get_height(root.right)
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        root.balance_factor = self.get_balance(root)
        new_root.balance_factor = self.get_balance(new_root)

        return new_root

    def left_rotate(self, root):
        new_root = root.right
        new_root.left = root
        root.right = None


        root.height = 1 + self.get_height(root.left)
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

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


def return_tree(array):
    tree = AVLTree()
    root = None

    for elem in array:
        root = tree.push(root, elem)

    print("В виде списка:")
    tree.in_order(root)
    print("\nВ виде дерева:")
    tree.print_tree(root)


def solve():
    answer = input("Ввод/вывод через файл/терминал: ").lower()
    if answer == "файл":
        file = open(pathlib.Path(pathlib.Path(__file__).parent, 'txtf', 'input.txt'))
        array = list(map(int, file.readline().split(" ")))
        return_tree(array)
    elif answer == "терминал":
        answer = input("Введите элементы массива через пробел: ")
        try:
            array = list(map(int, answer.split(" ")))
            return_tree(array)

        except:
            answer = input("Неправильно введены данные. Хотите продолжить? (Д/н): ").lower()
            if answer == "д":
                return solve()
            else:
                pass
    else:
        answer = input("Неправильно введены данные. Хотите продолжить? (Д/н): ").lower()
        if answer == "д":
            return solve()
        else:
            pass


if __name__ == "__main__":
    solve()
