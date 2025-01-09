from prettytable import PrettyTable
import pathlib

class PostClasses:
    def __init__(self, truth_table: list[list[int]]) -> None:
        truth_table.sort()

        self.values_count = len(truth_table[0]) - 1
        self.lines_count = len(truth_table)

        self.arguments = [tuple(s[:-1]) for s in truth_table]
        self.values = [s[-1] for s in truth_table]

        self.classes = ['0', "1", "L", "M", "S"]
        self.result = []

    def zero_class(self) -> bool:
        if self.values[0] == 0:
            return True
        else:
            return False


    def unit_class(self) -> bool:
        if self.values[-1] == 1:
            return True
        else:
            return False

    def self_dual_class(self) -> bool:
        for i in range(self.lines_count // 2):
            if self.values[i] != self.values[self.lines_count - i - 1]:
                pass
            else:
                return False
        return True


    def comparison(self, a, b, res_a, res_b):
        if all(a[i] >= b[i] for i in range(self.values_count)):
            if res_a >= res_b:
                return True
            else:
                return False
        elif all(a[i] <= b[i] for i in range(self.values_count)):
            if res_a <= res_b:
                return True
            else:
                return False
        else:

            return True


    def monotone_class(self):
        for ind1 in range(self.lines_count):
            k1, v1 = self.arguments[ind1], self.values[ind1]
            for ind2 in range(ind1 + 1, self.lines_count):
                k2, v2 = self.arguments[ind2], self.values[ind2]
                if self.comparison(k1, k2, v1, v2):
                    pass
                else:
                    return False
        return True


    def lineal_class(self):
        results = self.values.copy()
        for i in range(self.lines_count - 1):
            res = results.copy()
            for j in range(self.lines_count - 1 - i):
                res[j] = (results[j] + results[j + 1]) % 2
            results = res.copy()
            if results[0] == 1:
                if self.arguments[i + 1].count(1) > 1:
                    return False
        return True

    def get_table(self):
        self.result = [self.zero_class(), self.unit_class(), self.lineal_class(), self.monotone_class(), self.self_dual_class()]
        self.result = ["+" if i else "-" for i in self.result]


    def print_table(self):
        self.get_table()
        table = PrettyTable()
        table.field_names = self.classes
        table.hrules = 1
        table.add_row(self.result)
        print(table)


    def write_table_to_file(self):
        self.get_table()
        file = open(pathlib.Path(pathlib.Path(__file__).parent, 'txtf', 'output.txt'), 'w')
        file.write(" ".join(self.classes) + "\n" + " ".join(self.result))


def solve():
    answer = input("Ввод/вывод через файл/терминал [Ф/т]: ").lower()
    if answer == "ф":
        file = open(pathlib.Path(pathlib.Path(__file__).parent, 'txtf', 'input.txt'))
        data = file.read().split("\n")
        array = [list(map(int, d.split(" "))) for d in data]
        PostClasses(array).write_table_to_file()

    elif answer == "т":
        print("Введите таблицу. В конце нажмите enter: ")
        line = input()
        try:
            array = []
            while line != "" and all(el in "01 " for el in line):
                new_line = list(map(int, line.split(" ")))
                array += [new_line]
                line = input()
            PostClasses(array).print_table()
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
