# Will Vanderploeg
import matplotlib.pyplot as plt
import os
# Constants
NUM_QUESTIONS = 7

SECTIONS = ("Easy", "Medium", "Hard", "Total Accuracy")

YELLOW = int(NUM_QUESTIONS * .8)

RED = int(NUM_QUESTIONS * .5)


def transition(sec_1, sec_2, sec_3):
    color = []
    section1 = (sec_1 / NUM_QUESTIONS) * 100
    section2 = (sec_2 / NUM_QUESTIONS) * 100
    section3 = (sec_3 / NUM_QUESTIONS) * 100
    elist = [section1, section2, section3]
    total = ((sec_1+sec_2+sec_3)/(NUM_QUESTIONS*3))*100
    sections = (sec_1, sec_2, sec_3, total)
    elist.append(total)
    for section in sections:
        if section > YELLOW:
            color.append("green")
        elif section > RED:
            color.append("yellow")
        else:
            color.append("red")
    minimum = min(elist)
    maximum = max(elist)
    return elist, minimum, maximum, color, section1, section2, section3, total, sections


def graph(sec_1, sec_2, sec_3, wrong1, wrong2, wrong3):
    os.system("cls")
    stats, min_sec, max_sec, sec_color, section1, section2, section3, total, section = transition(sec_1, sec_2, sec_3)
    print(f"{sec_color}\n{stats}")
    print(f"Your weakest section was {min_sec}\n")
    print(f"Your strongest section was {max_sec}\n\n")
    print("Section 1 (easy)\n_________________________________________")
    print(f"accuracy = {section[0]}/{NUM_QUESTIONS} or {section1:.2f}%\n")
    if len(wrong1) > 0:
        print(f"You need to work on these words:\n{wrong1}\n")
    print("Section 2 (Medium)\n_________________________________________")
    print(f"accuracy = {section[1]}/{NUM_QUESTIONS} or {section2:.2f}%\n")
    if len(wrong2) > 0:
        print(f"You need to work on these words:\n{wrong2}\n")
    print("Section 3 (Hard)\n_________________________________________")
    print(f"accuracy = {section[2]}/{NUM_QUESTIONS} or {section3:.2f}%\n")
    if len(wrong3) > 0:
        print(f"You need to work on these words:\n{wrong3}\n")
    print(f"accuracy = {section[0] + section[1] + section[2]}/{NUM_QUESTIONS*3} or {total:.2f}%\n")
    plt.bar(SECTIONS, stats, color=sec_color)
    plt.title("Stats")
    plt.xlabel("Section Difficulty")
    plt.ylabel("# Correct")
    plt.show()
