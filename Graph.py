# Will Vanderploeg
import matplotlib.pyplot as plt
from time import sleep
# Constants
NUM_QUESTIONS = 7

SECTIONS = ("Easy", "Medium", "Hard")

YELLOW = int(NUM_QUESTIONS * .8)

RED = int(NUM_QUESTIONS * .5)


def transition(sec_1, sec_2, sec_3):
    color = []
    elist = [sec_1, sec_2, sec_3]
    for section in elist:
        print(section)
        if section > YELLOW:
            color.append("green")
        elif section > RED:
            color.append("yellow")
        else:
            color.append("red")
    minimum = min(elist)
    maximum = max(elist)
    return elist, minimum, maximum, color


<<<<<<< Updated upstream:Graph.py
def graph():
    stats, min_sec, max_sec, sec_color = transition(12, 8, 17)
=======
def graph(sec_1, sec_2, sec_3):
    stats, min_sec, max_sec, sec_color = transition(sec_1, sec_2, sec_3)
>>>>>>> Stashed changes:graph.py
    print(f"Your weakest section was {min_sec}\n")
    sleep(.5)
    print(f"Your strongest section was {max_sec}\n\n")
    sleep(.5)

    section1 = stats[0] / NUM_QUESTIONS
    section2 = stats[1] / NUM_QUESTIONS
    section3 = stats[2] / NUM_QUESTIONS

    print(f"Section 1 (easy) accuracy = {section1*100:.2f}%\n")
    sleep(.5)
    print(f"Section 2 (medium) accuracy = {section2*100:.2f}%\n")
    sleep(.5)
    print(f"Section 3 (Hard) accuracy = {section3*100:.2f}%\n")
    sleep(.5)
    print(f"Total accuracy = {(sum(stats) / (NUM_QUESTIONS * 3))*100:.2f}%")
    sleep(.5)

    plt.subplot(2, 1, 1)
    plt.bar(SECTIONS, stats, color=sec_color)
    plt.title("Stats")
    plt.xlabel("Section Difficulty")
    plt.ylabel("# Correct")
    plt.subplot(2, 1, 2)
    plt.plot(SECTIONS, [section1, section2, section3], color="orange")
    plt.ylim(0)
    plt.show()

