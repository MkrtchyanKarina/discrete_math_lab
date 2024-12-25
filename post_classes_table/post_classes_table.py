from prettytable import PrettyTable


class PostClasses:
    def __init__(self) -> None:
        truth_table = sorted(
            ([0, 0, 0, 0],
             [0, 0, 1, 0],
             [0, 1, 0, 0],
             [0, 1, 1, 1],
             [1, 0, 0, 0],
             [1, 0, 1, 1],
             [1, 1, 0, 1],
             [1, 1, 1, 1]))

        self.values_count = len(truth_table[0]) - 1
        self.lines_count = len(truth_table)

        self.arguments = [tuple(s[:-1]) for s in truth_table]
        self.results = [s[-1] for s in truth_table]

    def zero_class(self) -> bool:
        if self.results[0] == 0:
            return True
        else:
            return False


    def unit_class(self) -> bool:
        if self.results[-1] == 1:
            return True
        else:
            return False

    def self_dual_class(self) -> bool:
        for i in range(self.lines_count // 2):
            if self.results[i] != self.results[self.lines_count - i - 1]:
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
            k1, v1 = self.arguments[ind1], self.results[ind1]
            for ind2 in range(ind1 + 1, self.lines_count):
                k2, v2 = self.arguments[ind2], self.results[ind2]
                if self.comparison(k1, k2, v1, v2):
                    pass
                else:
                    return False
        return True


    def lineal_class(self):
        results = self.results.copy()
        for i in range(self.lines_count - 1):
            res = results.copy()
            for j in range(self.lines_count - 1 - i):
                res[j] = (results[j] + results[j + 1]) % 2
            results = res.copy()
            if results[0] == 1:
                if self.arguments[i + 1].count(1) > 1:
                    return False
        return True

    def post_classes(self):
        table = PrettyTable()
        table.field_names = ['0', "1",  "L", "M", "S"]
        table.hrules = 1
        classes = [self.zero_class(), self.unit_class(), self.lineal_class(), self.monotone_class(), self.self_dual_class()]
        classes = ["+" if i else "-" for i in classes]
        table.add_row(classes)
        print(table)

if __name__ == "__main__":
    PostClasses().post_classes()