#
# Gavin McKenzie, Nuno Handem Ribero
# 2/16/24
# Input for question and checks if its right printing and returning "Correct" or "Incorrect"
import random as r
from time import sleep

def question_format(questions, answers):
    letters = ["A.", "B.", "C.", "D."]

    while len(questions) > 0:
        # questions_changed = questions[:]
        rand_index = r.randint(0,4)
        correct_pos = r.randint(0,3)
        correct_ans = answers[rand_index]
        answers.remove(correct_ans)
        print(questions[rand_index])
        count = 0
        index_limit = len(answers) - 1
        for x in letters:
            other_ans = r.randint(0, index_limit)
            if count == correct_pos:
                print(f"{x} {correct_ans}")
            else:
                print(f"{x} {answers[other_ans]}")
                answers.remove(answers[other_ans])
                index_limit -= 1
            count += 1
            sleep(.5)
        input_and_checking(letters[correct_pos])

def input_and_checking(answer):
    user_answer = input("Enter answer (A, B, C, or D): ")
    user_answer = user_answer.upper()
    sleep(1)
    if user_answer != ('A' or 'B' or 'C' or 'D'):
        if user_answer == answer:
            print("Correct!!")
        else:
            print("Incorrect")
    else:
        input_and_checking(answer)