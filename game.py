#
# Gavin McKenzie, Nuno Handem Ribero
# 2/16/24
# Input for question and checks if its right printing and returning "Correct" or "Incorrect"
import random as r
from time import sleep


def question_format(questions, answers, mode):
    letters = ["A", "B", "C", "D"]
    answer_choices = answers[:]
    Q_counter = 1
    num_wrong = []
    correct = 0
    for length in range(7):
        answer_indexs = []
        correct_ans = r.choice(answers)
        correct_index = answers.index(correct_ans)
        correct_pos = r.randint(0,3)
        answers.remove(correct_ans)
        print(f"{mode} Q{Q_counter}: {questions[correct_index]}")
        questions.pop(correct_index)
        count = 0
        print("--------------------------------------------------")
        count2 = 0
        Q_counter += 1
        for i in range(3):
            other_ans = r.choice(answer_choices)
            while other_ans in answer_indexs:
                other_ans = r.choice(answer_choices)
                if other_ans == correct_ans:
                    other_ans = r.choice(answer_choices)
            if other_ans == correct_ans:
                other_ans = r.choice(answer_choices)
            answer_indexs.append(other_ans)
        for x in letters:
            if count == correct_pos:
                print(f"{x} {correct_ans}")
            else:
                print(f"{x} {answer_indexs[count2]}")
                count2 += 1
            count += 1
            sleep(.5)
        user_answer = input_and_checking(letters)
        if user_answer == letters[correct_pos]:
            print("Correct!!!\n")
            correct += 1
        else:
            print("Incorrect 🥺🥺🥺🥺🥺\n")
            num_wrong.append(correct_ans)
    return correct, num_wrong


def input_and_checking(letters):
    user_answer = input("Enter answer (A, B, C, or D): ")
    user_answer = user_answer.upper()
    sleep(1)
    while user_answer not in letters:
        print("TRY AGAIN 😈😈😈😈😈😈😈😈😈😈😈")
        user_answer = input("Enter answer (A, B, C, or D): ")
        user_answer = user_answer.upper()

    return user_answer

