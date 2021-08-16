# A program to get a working calculator application on the desktop.

import tkinter as tk
import math as math

# from functools import partial // written for reference


def calculate(output_result, operator, value1, value2):
    """
    A function to get the value of an operation on two integers. Only takes addition,
    Subtraction, multiplication, Integer division.

    :param operator: The desired operation by the user. Can be addition, subtraction,
    multiplication or integer division

    :param output_result: The output display in ui

    :param value1: The first input value. Should be an integer.

    :param value2: The second input value. should be an integer. Should not be zero for division
    """
    ans = 0
    num1 = float(value1.get())
    num2 = float(value2.get())
    opr = operator
    if opr == '+':
        ans = num1 + num2
        output_result.config(text=f"result is {ans}")
        return

    elif opr == '-':
        ans = num1 - num2
        output_result.config(text=f"result is {ans}")
        return

    elif opr == '*':
        ans = num1*num2
        output_result.config(text=f"result is {ans}")
        return

    elif opr == '/':
        if value2 != 0:
            ans = num1/num2
            output_result.config(text=f"result is {ans}")
            return

        else:
            output_result.config(text=f"result is not defined")
            return

    elif opr == "sqrt":
        ans = math.sqrt(num1)
        output_result.config(text=f"result is {ans}")

    else:
        output_result.config(text=f'there is no result for operation {opr} on numbers {num1}, {num2}')


calc_window = tk.Tk()
calc_window.title("Simple Calculator")
calc_window.geometry('300x200')
number1 = tk.StringVar()
number2 = tk.StringVar()
operator1 = None

# number input
input_no_1 = tk.Entry(calc_window, textvariable=number1, width=20).place(x=90, y=20)
input_no_2 = tk.Entry(calc_window, textvariable=number2, width=20).place(x=90, y=40)

# Result output
output_result = tk.Label(calc_window, text="result will be displayed here", width=20)
output_result.grid(padx=80)
output_result.config(text="result will be displayed here")

# for reference only
# calculate = partial(calculate, output_result, operator1, number1, number2)

# Operator buttons
add_btn = tk.Button(calc_window, text='+', command=lambda: calculate(output_result, "+", number1, number2))\
    .place(x=90, y=60)
sub_btn = tk.Button(calc_window, text='-', command=lambda: calculate(output_result, "-", number1, number2))\
    .place(x=110, y=60)
pro_btn = tk.Button(calc_window, text='*', command=lambda: calculate(output_result, "*", number1, number2)) \
    .place(x=130, y=60)
div_btn = tk.Button(calc_window, text='/', command=lambda: calculate(output_result, "/", number1, number2)) \
    .place(x=150, y=60)
sqrt_btn = tk.Button(calc_window, text='sqrt', command=lambda: calculate(output_result, "sqrt", number1, number2)) \
    .place(x=170, y=60)


calc_window.mainloop()




