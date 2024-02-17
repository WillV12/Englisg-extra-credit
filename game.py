#
# Gavin McKenzie, Nuno Handem Ribero
# 2/16/24
# Input for question and checks if its right printing and returning "Correct" or "Incorrect"
import random as r
from time import sleep


def question_format(questions, answers):
    letters = ["A", "B", "C", "D"]
    answer_choices = answers[:]
    while len(questions) > 3:
        answer_indexs = []
        correct_ans = r.choice(answers)
        correct_index = answers.index(correct_ans)
        correct_pos = r.randint(0,3)
        answers.remove(correct_ans)
        print(questions[correct_index])
        questions.pop(correct_index)
        count = 0
        print("--------------------------------------------------")
        count2 = 0
        for x in letters:
            if count == correct_pos:
                print(f"{x} {correct_ans}")
            else:
                other_ans = r.choice(answer_choices)
                while other_ans in answer_indexs:
                    other_ans = r.choice(answer_choices)
                    if other_ans == correct_ans:
                        other_ans = r.choice(answer_choices)
                if other_ans == correct_ans:
                    other_ans = r.choice(answer_choices)
                answer_indexs.append(other_ans)
                print(f"{x} {answer_indexs[count2]}")
                count2 += 1

            count += 1
            sleep(.5)
        right, wrong = input_and_checking(letters[correct_pos])
    return right, wrong


def input_and_checking(answer):
    letters = ["A", "B", "C", "D"]
    num_wrong = 0
    num_right = 0
    user_answer = input("Enter answer (A, B, C, or D): ")
    user_answer = user_answer.upper()
    print(user_answer)
    sleep(1)
    while user_answer not in letters:
        print("TRY AGAIN 😈😈😈😈😈😈😈😈😈😈😈")
        user_answer = input("Enter answer (A, B, C, or D): ")
        user_answer = user_answer.upper()
    if user_answer == answer:
        print("Correct!!!\n")
        num_right += 1
    else:
        print("Incorrect 🥺🥺🥺🥺🥺\n")
        num_wrong += 1
    return num_right, num_wrong
