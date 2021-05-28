if __name__ == '__main__':
    # 初期値の入力
    input_shape = int(input('解くナンプレの大きさ（縦または横のマスの数）:'))
    init_data = []
    i = 0
    while True:
        user_input = input('%s行目の初期値をカンマ区切りで入力してください：' % i)
        init_data.append([int(j) for j in user_input.split(',')])
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
            l_row.append([1] * 10)
            j += 1
            if j == input_shape:
                break
        l_select.append(l_row)
        i += 1
        if i == input_shape:
            break

    # 回答を管理するリストを作成
    l_answer = []
    i = 0
    while True:
        l_answer.append([0] * input_shape)
        i += 1
        if i == input_shape:
            break
