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


    def comparison(self, a: tuple, b: tuple, res_a: int, res_b: int) -> bool:
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


    def monotone_class(self) -> bool:
        for ind1 in range(self.lines_count):
            k1, v1 = self.arguments[ind1], self.values[ind1]
            print(k1)
            for ind2 in range(ind1 + 1, self.lines_count):
                k2, v2 = self.arguments[ind2], self.values[ind2]
                if self.comparison(k1, k2, v1, v2):
                    pass
                else:
                    return False
        return True


    def lineal_class(self) -> bool:
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

    def get_table(self) -> str:
        self.result = [self.zero_class(), self.unit_class(), self.lineal_class(), self.monotone_class(), self.self_dual_class()]
        self.result = ' '.join(self.classes) + '\n' + ' '.join(["+" if i else "-" for i in self.result])
        return self.result


def solve():
    print("Введите таблицу. В конце нажмите enter: ")
    line = input()
    try:
        array = []
        while line != "" and all(el in "01 " for el in line):
            new_line = list(map(int, line.strip().split(" ")))
            if all(el == 0 or el == 1 for el in new_line):
                array += [new_line]
                line = input()
            else:
                answer = input("Неправильно введены данные. Хотите продолжить? (Д/н): ").lower()
                if answer == "д" or answer == "l":
                    return solve()
        if len(array) != 2 ** (len(array[0]) - 1):
            answer = input("Неправильно введены данные. Хотите продолжить? (Д/н): ").lower()
            if answer == "д" or answer == "l":
                return solve()
        else:
            print(PostClasses(array).get_table())
        answer = input("Хотите продолжить? (Д/н): ").lower()
        if answer == "д" or answer == "l":
            return solve()
    except:
        answer = input("Неправильно введены данные. Хотите продолжить? (Д/н): ").lower()
        if answer == "д" or answer == "l":
            return solve()


if __name__ == "__main__":
    solve()