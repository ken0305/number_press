from collections import Counter


# 答えの候補を管理するリストl_selectを作成
class NumberPressUpdate:
    def __init__(self, input_shape, l_select, l_answer):
        self.input_shape = input_shape
        self.l_select = l_select
        self.l_answer = l_answer

    # l_answerを用いてl_selectを更新
    def update_select(self):
        for row in range(self.input_shape):
            for column in range(self.input_shape):
                if self.l_answer[row][column] != 0:
                    i = 0
                    while True:
                        if i != self.l_answer[row][column] - 1:
                            self.l_select[row][column][i] = 0
                        i += 1
                        if i == 9:
                            break

    # 縦を見て、l_selectを更新
    def update_select_column(self):
        for column in range(self.input_shape):
            l_check = [0] * self.input_shape
            for row in range(self.input_shape):
                num_select = self.l_select[row][column].count(1)
                if num_select == 1:
                    l_check[self.l_select[row][column].index(1)] = 1
            for num in range(self.input_shape):
                if l_check[num] != 0:
                    for row in range(self.input_shape):
                        num_select = self.l_select[row][column].count(1)
                        if num_select != 1:
                            self.l_select[row][column][num] = 0

    # 横を見て、l_selectを更新
    def update_select_rows(self):
        for row in range(self.input_shape):
            l_check = [0] * self.input_shape
            for column in range(self.input_shape):
                num_select = self.l_select[row][column].count(1)
                if num_select == 1:
                    l_check[self.l_select[row][column].index(1)] = 1
            for num in range(9):
                if l_check[num] != 0:
                    for column in range(self.input_shape):
                        num_select = self.l_select[row][column].count(1)
                        if num_select != 1:
                            self.l_select[row][column][num] = 0

    # 3 * 3のボックスを見て、l_selectを更新
    def update_select_33(self):
        for row in range(int(self.input_shape / 3)):
            for column in range(int(self.input_shape / 3)):
                l_check = [0] * self.input_shape
                i = row * 3
                while True:
                    j = column * 3
                    while True:
                        num_select = self.l_select[i][j].count(1)
                        if num_select == 1:
                            l_check[self.l_select[i][j].index(1)] = 1

                        j += 1
                        if j == (column + 1) * 3:
                            break
                    i += 1
                    if i == (row + 1) * 3:
                        break
                for num in range(9):
                    i = row * 3
                    while True:
                        j = column * 3
                        while True:
                            if self.l_answer[i][j] == 0:
                                self.l_select[i][j][num] = 0
                            j += 1
                            if j == (column + 1) * 3:
                                break
                        i += 1
                        if i == (row + 1) * 3:
                            break

    # l_selectを使ってl_answerを更新する
    def update_answer(self):
        i = 0
        while True:
            j = 0
            while True:
                if self.l_answer[i][j] == 0:
                    d_info = Counter(self.l_select[i][j])
                    if d_info[1] == 1:
                        self.l_answer[i][j] = self.l_select[i][j].index(1) + 1
                    j += 1
                if j == len(self.l_answer[i]):
                    break
            i += 1
            if i == len(self.l_select):
                break

    # ナンプレが完成したかどうかを判定
    def is_complete(self):
        i = 0
        while True:
            j = 0
            while True:
                if self.l_answer[i][j] == 0:
                    return False
                j += 1
                if j == len(self.l_answer[i]):
                    break
            i += 1
            if i == len(self.l_answer):
                return True

    def output(self):
        return self.l_answer

    def print_result(self):
        for row in self.l_answer:
            print(row)

    def print_complete_rate(self):
        total = self.input_shape * 2
        cnt = 0
        for row in self.l_answer:
            cnt += Counter(row)[0]
        print('\rin progress : %f' % (total - cnt) / total)
    

def init_select(input_shape):
    l_select = []
    i = 0
    while True:
        j = 0
        l_row = []
        while True:
            l_row.append([1] * 9)
            j += 1
            if j == input_shape:
                break
        l_select.append(l_row)
        i += 1
        if i == input_shape:
            break
    return l_select
