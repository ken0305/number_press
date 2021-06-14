from functions import init_select, NumberPressUpdate

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
    l_select = init_select(input_shape=input_shape)
    numpre = NumberPressUpdate(input_shape=input_shape, l_select=l_select, l_answer=l_answer)
    numpre.update_select()
    while numpre.is_complete():
        numpre.update_select_column()
        numpre.update_select_rows()
        numpre.update_select_33()
        numpre.update_answer()
        numpre.print_complete_rate()
    numpre.print_result()
