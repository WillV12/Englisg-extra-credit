import matplotlib.pyplot as plt

# Constants
NUM_QUESTIONS = 17

SECTIONS = ("Easy", "Medium", "Hard")

YELLOW = int(NUM_QUESTIONS * .8)

RED = int(NUM_QUESTIONS * .5)


def transition(sec_1, sec_2, sec_3):
    color = []
    elist = [sec_1, sec_2, sec_3]
    for section in elist:
        if section > YELLOW:
            color.append("green")
        elif section > RED:
            color.append("yellow")
        else:
            color.append("red")
    minimum = min(elist)
    maximum = max(elist)
    return elist, minimum, maximum, color




def graph():
    stats, min_sec, max_sec, sec_color = transition(12, 8, 17)
    print(f"Your weakest section was {min_sec}\n")
    print(f"Your strongest section was {max_sec}\n\n")

    section1 = stats[0] / NUM_QUESTIONS
    section2 = stats[1] / NUM_QUESTIONS
    section3 = stats[2] / NUM_QUESTIONS

    print(f"Section 1 (easy) accuracy = {section1:.2f}%\n")
    print(f"Section 2 (medium) accuracy = {section2:.2f}%\n")
    print(f"Section 3 (Hard) accuracy = {section3:.2f}%\n")
    print(f"Total accuracy = {sum(stats) / (NUM_QUESTIONS * 3):.2f}%")

    fig, ax = plt.subplots()
    ax.bar(SECTIONS, stats, color=sec_color)
    plt.title("Stats")
    plt.xlabel("Section Difficulty")
    plt.ylabel("# Correct")
    plt.show()