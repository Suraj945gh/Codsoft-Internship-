# -*- coding: utf-8 -*-
"""my_calculator.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T6kSWQ2Qq6p1vIZ2vDeZ9fL8xpaynxHc
"""

def simple_calculator(num1,num2,op):

  if num1.isnumeric() and num2.isnumeric():
    num1 = float(num1)
    num2 = float(num2)
    if op == 'add':
      result = float(num1 + num2)
    elif op == 'sub':
      result = num1 - num2
    elif op == 'mul':
      result = num1*num2
    elif op == 'divide':
      if num2 != 0:
        result = num1/num2
      else:
        result = "Cannot divide by zero"
    elif op == 'mod':
      result = num1 % num2
    else:
      result = "Operations supported add / sub / mul / divide / mod only"

  else:
    result = "Please enter valid inputs for the numbers"

  return result