import pathlib


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.balance_factor = 0
        self.height = 1
        self.value = value


class AVLTree:
    def __init__(self):
        self.result_in_order = ''
        self.result_in_tree = ''

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
            self.result_in_order += f'{root.value} '
            self.in_order(root.right)
        return self.result_in_order.strip()


class CreateAVLTree:
    def __init__(self, array):
        self.array = array
        self.tree = AVLTree()
        self.root = None
        self.push()

    def push(self):
        for elem in self.array:
            self.root = self.tree.push(self.root, elem)

    def return_res(self):
        return self.tree.in_order(self.root)


class File:
    def __init__(self):
        self.tree = None
        self.read()

    def read(self):
        file_input = open(pathlib.Path(pathlib.Path(__file__).parent, 'txtf', 'input.txt'))
        array = list(map(int, file_input.readline().split(" ")))
        file_input.close()
        self.tree = CreateAVLTree(array)

    def write(self):
        file_output = open(pathlib.Path(pathlib.Path(__file__).parent, 'txtf', 'output.txt'), 'w')
        file_output.write(self.tree.return_res())
        file_output.close()



def solve():
    answer = input("Ввод/вывод через файл/терминал [Ф/т]: ").lower()

    if answer == "ф":
        File().write()
    elif answer == "т":
        answer = input("Введите элементы массива через пробел: ")
        try:
            array = list(map(int, answer.split(" ")))
            tree = CreateAVLTree(array)
            print(tree.return_res())
        except:
            answer = input("Неправильно введены данные. Хотите продолжить? (Д/н): ").lower()
            if answer == "д":
                return solve()
    else:
        answer = input("Неправильно введены данные. Хотите продолжить? (Д/н): ").lower()
        if answer == "д":
            return solve()


if __name__ == "__main__":
    solve()