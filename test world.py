import random as r
from time import sleep

stuff = {"apple": "red", "pear": "green", "banana": "yellow", "orange": "orange", "grape": "purple"}
questions = ["apple", "pear", "banana", "orange", "purple"]
letters = ["A.", "B.", "C.", "D."]
count = 3

while len(questions) > 0:
    stuff_keys = ["apple", "pear", "banana", "orange", "grape"]
    print(stuff_keys)
    index = r.randint(0, count)
    print(stuff[questions[index]])
    count -= 1
    questions.remove(questions[index])
    for x in letters:
        other_count = 3
        other_index = r.randint(0, other_count)
        print(other_index)
        print(other_count)
        other_count -= 1
        print(f"{x} {stuff[stuff_keys[other_index]]}")
        stuff_keys.remove(stuff_keys[other_index])
        sleep(.5)
    break

# print(f"A. {stuff[stuff_keys[r.randint(0,3)]]}")
# print(f"B. {stuff[stuff_keys[r.randint(0,3)]]}")
# print(f"C. {stuff[stuff_keys[r.randint(0,3)]]}")
# print(f"D. {stuff[stuff_keys[r.randint(0,3)]]}")
