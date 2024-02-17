#
# Gavin McKenzie, Nuno Handem Ribero
# 2/16/24
# Input for question and checks if its right printing and returning "Correct" or "Incorrect"
from time import sleep

def input_and_checking(answer, index):
    user_answer = input("Enter answer (A, B, C, or D): ")
    user_answer = user_answer.upper()
    sleep(1)
    if user_answer != ('A' or 'B' or 'C' or 'D'):
        if user_answer == answer:
            print("Correct!!")
        else:
            print("Incorrect")
    else:
        input_and_checking(answer, index)