if __name__ == '__main__':
    # 初期値の入力
    input_shape = int(input('解くナンプレの大きさ（縦または横のマスの数）:'))
    l_answer = []
    i = 0
    while True:
        user_input = input('%s行目の初期値をカンマ区切りで入力してください：' % i)
        l_answer.append([int(j) for j in user_input.split(',')])
        i += 1
        if i == input_shape:
            break

    # 答えの候補を管理するリストを作成
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

    # l_answerを用いてl_selectを更新
    for row in range(input_shape):
        for column in range(input_shape):
            if l_answer[row][column] != 0:
                i = 0
                while True:
                    if i != l_answer[row][column] - 1:
                        l_select[row][column][i] = 0
                    i += 1
                    if i == 9:
                        break

    # 縦を見て、l_selectを更新
    for column in range(input_shape):
        l_check = [0] * input_shape
        for row in range(input_shape):
            num_select = l_select[row][column].count(1)
            if num_select == 1:
                l_check[l_select[row][column].index(1)] = 1
        for num in range(input_shape):
            if l_check[num] != 0:
                for row in range(input_shape):
                    num_select = l_select[row][column].count(1)
                    if num_select != 1:
                        l_select[row][column][num] = 0

    # 横を見て、l_selectを更新
    for row in range(input_shape):
        l_check = [0] * input_shape
        for column in range(input_shape):
            num_select = l_select[row][column].count(1)
            if num_select == 1:
                l_check[l_select[row][column].index(1)] = 1
        for num in range(9):
            if l_check[num] != 0:
                for column in range(input_shape):
                    num_select = l_select[row][column].count(1)
                    if num_select != 1:
                        l_select[row][column][num] = 0

    # 3 * 3のボックスを見て、l_selectを更新
    for row in range(int(input_shape / 3)):
        for column in range(int(input_shape / 3)):
            l_check = [0] * input_shape
            i = row * 3
            while True:
                j = column * 3
                while True:
                    num_select = l_select[i][j].count(1)
                    if num_select == 1:
                        l_check[l_select[i][j].index(1)] = 1

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
                        if l_answer[i][j] == 0:
                            l_select[i][j][num] = 0
                        j += 1
                        if j == (column + 1) * 3:
                            break
                    i += 1
                    if i == (row + 1) * 3:
                        break
