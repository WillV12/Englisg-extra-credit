import random as r
from time import sleep

stuff = {"apple": "red", "pear": "green", "banana": "yellow", "orange": "orange", "grape": "purple"}
questions = ["apple", "pear", "banana", "orange", "grape"]
letters = ["A.", "B.", "C.", "D."]
count = 4

while len(questions) > 0:
    index = r.randint(0, count)
    print(stuff[questions[index]])
    count -= 1
    questions.remove(questions[index])
    other_count = 3
    answers = []
    for x in letters:
        other_index = r.randint(0, other_count)
        other_count -= 1
        print(f"{x} {questions[other_index]}")
        questions.remove(questions[other_index])
        sleep(.5)

    # correct_answer = r.randint(4)

    break

# print(f"A. {stuff[stuff_keys[r.randint(0,3)]]}")
# print(f"B. {stuff[stuff_keys[r.randint(0,3)]]}")
# print(f"C. {stuff[stuff_keys[r.randint(0,3)]]}")
# print(f"D. {stuff[stuff_keys[r.randint(0,3)]]}")
