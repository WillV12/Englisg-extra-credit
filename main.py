#
# Gavin McKenzie, Abram Head, Brandon Lehmann
# 2/16/24
# Main function for AP lang extra credit
import Difficulties as difs
import Question_setup as Qs
from time import sleep
from colorama import Fore, Back, Style
import os

DOTS = "....."
TITLE_PICTURE = '''     )                  )      )   (                     )      
  ( /(   (       (   ( /(   ( /(   )\\ )        *   )  ( /(      
  )\\())  )\\    ( )\\  )\\())  )\\()) (()/( (    ` )  /(  )\\()) (   
|((_)\\((((_)(  )((_)((_)\\  ((_)\\   /(_)))\\    ( )(_))((_)\\  )\\  
|_ ((_))\\ _ )\\((_)_   ((_)   ((_) (_)) ((_)  (_(_())  _((_)((_) 
| |/ / (_)_\\(_)| _ ) / _ \\  / _ \\ / __|| __| |_   _| | || || __|
| ' <   / _ \\  | _ \\| (_) || (_) |\\__ \\| _|  _ | |   | __ || _| 
|_|\\_\\ /_/ \\_\\ |___/ \\___/  \\___/ |___/|___|(_)|_|   |_||_||___|'''


def main():
    # Prints the Title card
    for line in TITLE_PICTURE.splitlines():
        print(f"{Fore.LIGHTYELLOW_EX}{Back.LIGHTRED_EX}{Style.BRIGHT}{line}{Style.RESET_ALL}")
        sleep(.094)

    # Greeting/Game Rules/Getting player name
    print(f"Welcome to Kaboose.the!\n\
    The rules are simple...\
    \n\tEnter the correct answer (A, B, C, or D)\n")

    player_name = input("Enter your Nickname (or real it don't matter):\n\t")

    print(f"Get ready {player_name}, things are about to get a little bit \
    {Fore.LIGHTYELLOW_EX}{Back.LIGHTRED_EX}{Style.BRIGHT}WICKED{Style.RESET_ALL}\n\n")

    # EASY MODE
    print("Beginning Wave 1 (easy mode)")

    for char in DOTS:
        print(char + "\t", end="")
        sleep(.34)
    print()
    os.system('cls')
    word_bank, words = difs.easy()
    Qs.questions(words, word_bank)

    # MEDIUM MODE
    print("Beginning Wave 2 (intermidiate mode)")
    for char in DOTS:
        print(char + "\t", end="")
        sleep(.34)
    print()
    os.system('cls')
    word_bank, words = difs.medium()

    # AH IT'S SO HARD... SO HARD... IT'S SO HARD
    print("Beginning Wave 3 (HARD mode)")
    for char in DOTS:
        print(char + "\t", end="")
        sleep(.34)
    print()
    os.system('cls')
    word_bank, words = difs.hard()


main()
