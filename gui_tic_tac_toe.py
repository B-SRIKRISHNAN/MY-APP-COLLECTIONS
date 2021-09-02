import tkinter as tk
import random as rd

turn = 1
result = 0


def game():

    global btn_list
    global turn
    board = [0 for i in range(9)]
    win_sets = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    global result
    num_places = 0
    for btn in btn_list:
        if btn['text'] == '':
            pass
        else:
            num_places += 1
    if num_places == 9:
        turn_label.config(text='The game has ended in a draw')
        turn_label.place(x=110)
        # return ()

    if btn_list[4]['text'] == 'X' and turn == 1:
        btn_list[6]['text'] = 'O'
        turn += 1
        return ()
    else:
        if turn == 1:
            btn_list[4]['text'] = 'O'
            turn += 1
            return ()
    if turn >= 2:
        set_pos = []
        for i in win_sets:
            n_x = 0
            n_o = 0
            n_none = 0
            temp = []
            for j in i:
                if btn_list[j]['text'] == 'X':
                    n_x += 1
                elif btn_list[j]['text'] == 'O':
                    n_o += 1
                elif btn_list[j]['text'] == '':
                    n_none += 1
            temp.append(n_x)
            temp.append(n_o)
            temp.append(n_none)
            set_pos.append(temp)

        print(set_pos)
        print(turn)
        if [3, 0, 0] in set_pos:
            turn_label.config(text='User is the winner!!')
            turn_label.place(x=150)
            result = 1
            return ()

        elif [0, 2, 1] in set_pos:
            pos = set_pos.index([0, 2, 1])
            for i in win_sets[pos]:
                if btn_list[i]['text'] == '':
                    btn_list[i]['text'] = 'O'
                    turn_label.config(text="System wins the game")
                    turn_label.place(x=150)
                    result = 1
                    return ()
        elif [2, 0, 1] in set_pos:
            pos = set_pos.index([2, 0, 1])
            for i in win_sets[pos]:
                if btn_list[i]['text'] == '':
                    btn_list[i]['text'] = 'O'
                    turn += 1
                    return()

        else:

            if (set_pos[1] == [1, 1, 1] or set_pos[4] == [1, 1, 1]) and (set_pos[7] == [1, 1, 1] or set_pos[6]
                                                                         == [1, 1, 1]) and turn == 2:
                if btn_list[7]['text'] == '' and set_pos[1] == [1, 1, 1]:
                    btn_list[7]['text'] = 'O'
                    turn += 1
                    return()
                elif btn_list[5]['text'] == '' and set_pos[4] == [1, 1, 1]:
                    btn_list[5]['text'] = 'O'
                    turn += 1
                    return()
                else:
                    for k in range(9):
                        if btn_list[k]['text'] == '':
                            btn_list[k]['text'] = 'O'
                            turn += 1
                            return()
            elif set_pos[4] == [0, 1, 2] and turn == 2:
                if btn_list[3]['text'] == '':
                    btn_list[3]['text'] = 'O'
                    turn += 1
                    return()

                else:
                    for k in range(9):
                        if btn_list[k]['text'] == '':
                            btn_list[k]['text'] = 'O'
                            turn += 1
                            return()

            elif set_pos[4] == [1, 1, 1] and set_pos[1] == [1, 1, 1] and turn == 2:
                if btn_list[2]['text'] == "" and set_pos[0] == [1, 0, 2] and set_pos[5] == [1, 0, 2]:
                    btn_list[2]['text'] = 'O'
                    turn += 1
                    return ()
                elif set_pos[0] == [1, 0, 2] and set_pos[3] == [1, 0, 2] and btn_list[0]["text"] == '':
                    btn_list[0]['text'] = 'O'
                    turn += 1
                    return ()
                elif set_pos[2] == [1, 0, 2] and set_pos[5] == [1, 0, 2] and btn_list[8]["text"] == '':
                    btn_list[8]['text'] = 'O'
                    turn += 1
                    return ()
                elif set_pos[2] == [1, 0, 2] and set_pos[3] == [1, 0, 2] and btn_list[6]["text"] == '':
                    btn_list[6]['text'] = 'O'
                    turn += 1
                    return ()
                else:
                    for k in range(9):
                        if btn_list[k]['text'] == '':
                            btn_list[k]['text'] = 'O'
                            turn += 1
                            return()

            # elif btn_list[0]['text'] == '':
            #     btn_list[0]['text'] = 'o'
            #     turn += 1
            #     return()
            else:
                for k in range(9):
                    if btn_list[k]['text'] == '':
                        btn_list[k]['text'] = 'O'
                        turn += 1
                        return()


def click1():
    if result != 1:
        if btn1['text'] == '':
            btn1['text'] = 'X'
            turn_label.config(text='user\'s turn')
            turn_label.place(x=200)
            game()
        else:
            turn_label.config(text='invalid choice')
            turn_label.place(x=190)


def click2():

    if result != 1:
        if btn2['text'] == '':
            btn2['text'] = 'X'
            turn_label.config(text='user\'s turn')
            turn_label.place(x=200)
            game()
        else:
            turn_label.config(text='invalid choice')
            turn_label.place(x=190)


def click3():

    if result != 1:
        if btn3['text'] == '':
            btn3['text'] = 'X'
            turn_label.config(text='user\'s turn')
            turn_label.place(x=200)
            game()
        else:
            turn_label.config(text='invalid choice')
            turn_label.place(x=190)


def click4():

    if result != 1:
        if btn4['text'] == '':
            btn4['text'] = 'X'
            turn_label.config(text='user\'s turn')
            turn_label.place(x=200)
            game()
        else:
            turn_label.config(text='invalid choice')
            turn_label.place(x=190)


def click5():

    if result != 1:
        if btn5['text'] == '':
            btn5['text'] = 'X'
            turn_label.config(text='user\'s turn')
            turn_label.place(x=200)
            game()
        else:
            turn_label.config(text='invalid choice')
            turn_label.place(x=190)


def click6():

    if result != 1:
        if btn6['text'] == '':
            btn6['text'] = 'X'
            turn_label.config(text='user\'s turn')
            turn_label.place(x=200)
            game()
        else:
            turn_label.config(text='invalid choice')
            turn_label.place(x=190)


def click7():

    if result != 1:
        if btn7['text'] == '':
            btn7['text'] = 'X'
            turn_label.config(text='user\'s turn')
            turn_label.place(x=200)
            game()
        else:
            turn_label.config(text='invalid choice')
            turn_label.place(x=190)


def click8():

    if result != 1:
        if btn8['text'] == '':
            btn8['text'] = 'X'
            turn_label.config(text='user\'s turn')
            turn_label.place(x=200)
            game()
        else:
            turn_label.config(text='invalid choice')
            turn_label.place(x=190)


def click9():

    if result != 1:
        if btn9['text'] == '':
            btn9['text'] = 'X'
            turn_label.config(text='user\'s turn')
            turn_label.place(x=200)
            game()
        else:
            turn_label.config(text='invalid choice')
            turn_label.place(x=190)


def refresh():
    global turn
    global result
    turn = 1
    result = 0
    for i in range(9):
        btn_list[i]['text'] = ''
    turn_label.config(text='first move from user')
    turn_label.place(x=160)
    return()


tic_tac_toe = tk.Tk()
tic_tac_toe.title('Tic-Tac-toe')
tic_tac_toe.geometry('500x500')
label = tk.Label(tic_tac_toe, text='TIC-TAC-TOE', font=("times new roman", 25), fg='blue', bg='red').place(x=150, y=0)
rules = tk.Label(tic_tac_toe, text='User will be x, System is o', font=10).place(x=130, y=80)
turn_label = tk.Label(tic_tac_toe, text='first move from user', font=10)
turn_label.place(x=160, y=400)
btn1 = tk.Button(tic_tac_toe, text="", command=click1, width=10, height=5)
btn1.place(x=125, y=120)
btn2 = tk.Button(tic_tac_toe, text="", command=click2, width =10, height =5)
btn2.place(x=205, y=120)
btn3 = tk.Button(tic_tac_toe, text="", command=click3, width =10, height =5)
btn3.place(x=285, y=120)
btn4 = tk.Button(tic_tac_toe, text="", command=click4, width =10, height =5)
btn4.place(x=125, y=205)
btn5 = tk.Button(tic_tac_toe, text="", command=click5, width =10, height =5)
btn5.place(x=205, y=205)
btn6 = tk.Button(tic_tac_toe, text="", command=click6, width =10, height =5)
btn6.place(x=285, y=205)
btn7 = tk.Button(tic_tac_toe, text="", command=click7, width =10, height =5)
btn7.place(x=125, y=290)
btn8 = tk.Button(tic_tac_toe, text="", command=click8, width =10, height =5)
btn8.place(x=205, y=290)
btn9 = tk.Button(tic_tac_toe, text="", command=click9, width =10, height =5)
btn9.place(x=285, y=290)
refresh_btn = tk.Button(tic_tac_toe, text='Refresh', command=refresh, width=10, height=2).place(x=210, y=450)
btn_list = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]
# print(btn_list[0]['text'])
# btn2 =

tic_tac_toe.mainloop()