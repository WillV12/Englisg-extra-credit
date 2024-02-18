#
# Gavin McKenzie, Nuno Handem Ribero
# 2/16/24
# Input for question and checks if its right printing and returning "Correct" or "Incorrect"
import random as r
from time import sleep

<<<<<<< Updated upstream
def question_format(questions, answers):
    letters = ["A.", "B.", "C.", "D."]

    while len(questions) > 0:
        # questions_changed = questions[:]
        rand_index = r.randint(0,4)
=======

def question_format(questions, answers, mode):
    letters = ["A", "B", "C", "D"]
    answer_choices = answers[:]
    Q_counter = 1
    num_right = 0
    num_wrong = []
    correct = 0
    for length in range(7):
        answer_indexs = []
        correct_ans = r.choice(answers)
        correct_index = answers.index(correct_ans)
>>>>>>> Stashed changes
        correct_pos = r.randint(0,3)
        correct_ans = answers[rand_index]
        answers.remove(correct_ans)
<<<<<<< Updated upstream
        print(questions[rand_index])
        count = 0
        index_limit = len(answers) - 1
=======
        print(f"{mode} Q{Q_counter}: {questions[correct_index]}")
        questions.pop(correct_index)
        count = 0
        print("--------------------------------------------------")
        count2 = 0
        Q_counter += 1
>>>>>>> Stashed changes
        for x in letters:
            other_ans = r.randint(0, index_limit)
            if count == correct_pos:
                print(f"{x} {correct_ans}")
            else:
<<<<<<< Updated upstream
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
=======
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
        user_answer = input_and_checking(letters)
        if user_answer == correct_ans:
            print("Correct!!!\n")
            correct += 1
            print(num_right)
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

>>>>>>> Stashed changes
