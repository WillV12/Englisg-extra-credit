#
# Gavin McKenzie, Nuno Handem Ribero
# 2/16/24
# Input for question and checks if its right printing and returning "Correct" or "Incorrect"
import random as r
from time import sleep

letters = ["A", "B", "C", "D"]


def question_format(questions, answers):
    letters = ["A", "B", "C", "D"]
    print(answers)
    while len(questions) > 0:
        answer_choices = answers[:]
        index_limit = len(answers) - 1
        correct_ans = r.choice(answers)
        correct_index = answers.index(correct_ans)
        correct_pos = r.randint(0,3)
        answers.remove(correct_ans)
        answer_choices
        print(questions[correct_index])
        count = 0
        for x in letters:
            other_ans = r.choice(answers)
            if count == correct_pos:
                print(f"{x} {correct_ans}")
            else:
                print(other_ans)
                print(f"{x} {answers[other_ans]}")
                answers.remove(answers[other_ans])

            count += 1
            sleep(.5)
        input_and_checking(letters[correct_pos])

def input_and_checking(answer):
    print(answer)
    user_answer = input("Enter answer (A, B, C, or D): ")
    print(user_answer)
    sleep(1)
    while user_answer not in letters:
        print("TRY AGAIN 😈😈😈😈😈😈😈😈😈😈😈")
        user_answer = input("Enter answer (A, B, C, or D): ")
    if user_answer == answer:
        print("Correct!!!\n")
    else:
        print("Incorrect 🥺🥺🥺🥺🥺\n")