# A program to get a working calculator application on the desktop.

import tkinter as tk
import math as math

# from functools import partial // written for reference

expression = ""


def button(expn):
    global expression
    expression = expression + str(expn)
    inputexp.set(expression)


def result():
    try:

        global expression
        value = str(eval(expression))
        outputexp.set(value)
        expression = value

    except:

        outputexp.set("error")
        expression = ""


def clear():
    global expression
    expression = ""
    outputexp.set("")
    inputexp.set("")


calc_window = tk.Tk()
calc_window.title("Simple Calculator")
calc_window.geometry('300x200')

inputexp = tk.StringVar()
outputexp = tk.StringVar()


# Result output
input_no_1 = tk.Entry(calc_window, textvariable=outputexp, width=16).place(x=90, y=20)


# number input
input_no_2 = tk.Entry(calc_window, textvariable=inputexp, width=16).place(x=90, y=40)

# Operator buttons

add_btn = tk.Button(calc_window, text=' + ', command=lambda: button("+"), width=2, height=1).place(x=165, y=80)
sub_btn = tk.Button(calc_window, text=' -  ', command=lambda: button("-"), width=2, height=1).place(x=165, y=105)
mul_btn = tk.Button(calc_window, text=' *  ', command=lambda: button("*"), width=2, height=1).place(x=165, y=130)
div_btn = tk.Button(calc_window, text=' /  ', command=lambda: button("/"), width=2, height=1).place(x=165, y=155)
num1_btn = tk.Button(calc_window, text=' 1 ', command=lambda: button(1), width=2, height=1).place(x=90, y=80)
num2_btn = tk.Button(calc_window, text=' 2 ', command=lambda: button(2), width=2, height=1).place(x=115, y=80)
num3_btn = tk.Button(calc_window, text=' 3 ', command=lambda: button(3), width=2, height=1).place(x=140, y=80)
num4_btn = tk.Button(calc_window, text=' 4 ', command=lambda: button(4), width=2, height=1).place(x=90, y=105)
num5_btn = tk.Button(calc_window, text=' 5 ', command=lambda: button(5), width=2, height=1).place(x=115, y=105)
num6_btn = tk.Button(calc_window, text=' 6 ', command=lambda: button(6), width=2, height=1).place(x=140, y=105)
num7_btn = tk.Button(calc_window, text=' 7 ', command=lambda: button(7), width=2, height=1).place(x=90, y=130)
num8_btn = tk.Button(calc_window, text=' 8 ', command=lambda: button(8), width=2, height=1).place(x=115, y=130)
num9_btn = tk.Button(calc_window, text=' 9 ', command=lambda: button(9), width=2, height=1).place(x=140, y=130)
num0_btn = tk.Button(calc_window, text=' 0 ', command=lambda: button(0), width=2, height=1).place(x=115, y=155)
eql_btn = tk.Button(calc_window, text=" = ", command=lambda: result(), width=2, height=1).place(x=140, y=155)
clr_btn = tk.Button(calc_window, text="AC", command=lambda: clear(), width=2, height=1).place(x=90, y=155)


calc_window.mainloop()


# for reference only (from previous method used)

# def calculate(out_opn, output_result, operator, value1, value2):
#     """
#     A function to get the value of an operation on two integers. Only takes addition,
#     Subtraction, multiplication, Integer division.
#
#     :param operator: The desired operation by the user. Can be addition, subtraction,
#     multiplication or integer division
#
#     :param output_result: The output display in ui
#
#     :param value1: The first input value. Should be an integer.
#
#     :param value2: The second input value. should be an integer. Should not be zero for division
#     """
#     ans = 0
#     num1 = float(value1.get())
#     num2 = float(value2.get())
#     opr = operator
#     out_opn.insert('1.0', f"{num1} {opr} {num2}")
#     if opr == '+':
#         ans = num1 + num2
#         output_result.config(text=f"result is {ans}")
#         return
#
#     elif opr == '-':
#         ans = num1 - num2
#         output_result.config(text=f"result is {ans}")
#         return
#
#     elif opr == '*':
#         ans = num1*num2
#         output_result.config(text=f"result is {ans}")
#         return
#
#     elif opr == '/':
#         if value2 != 0:
#             ans = num1/num2
#             output_result.config(text=f"result is {ans}")
#             return
#
#         else:
#             output_result.config(text=f"result is not defined")
#             return
#
#     elif opr == "sqrt":
#         ans = math.sqrt(num1)
#         output_result.config(text=f"result is {ans}")
#
#     else:
#         output_result.config(text=f'there is no result for operation {opr} on numbers {num1}, {num2}')
#     out_opn.delete("1.0",)

# for reference only
# calculate = partial(calculate, output_result, operator1, number1, number2)

