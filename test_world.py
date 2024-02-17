import random as r
from time import sleep


questions = ["red", "green", "yellow", "orange", "purple"]
letters = ["A.", "B.", "C.", "D."]


while len(questions) > 0:
    answers = ["apple", "pear", "banana", "orange", "grape"]
    rand_index = r.randint(0,4)
    correct_pos = r.randint(0,3)
    correct_ans = answers[rand_index]
    answers.remove(correct_ans)
    print(questions[rand_index])
    count = 0
    index_limit = 3
    for x in letters:
        other_ans = r.randint(0,index_limit)
        if count == correct_pos:
            print(f"{x} {correct_ans}")
        else:
            print(f"{x} {answers[other_ans]}")
            answers.remove(answers[other_ans])
            index_limit -= 1
        count += 1
        sleep(.5)
    break
