#
# Gavin McKenzie, Abram Head, Brandon Lehmann
# 2/16/24
# Main function for AP lang extra credit
# import NUnos file
from time import sleep
from colorama import Fore, Back, Style
DOTS = "....."

def main():
    title_picture = '''     )                  )      )   (                     )      
  ( /(   (       (   ( /(   ( /(   )\\ )        *   )  ( /(      
  )\\())  )\\    ( )\\  )\\())  )\\()) (()/( (    ` )  /(  )\\()) (   
|((_)\\((((_)(  )((_)((_)\\  ((_)\\   /(_)))\\    ( )(_))((_)\\  )\\  
|_ ((_))\\ _ )\\((_)_   ((_)   ((_) (_)) ((_)  (_(_())  _((_)((_) 
| |/ / (_)_\\(_)| _ ) / _ \\  / _ \\ / __|| __| |_   _| | || || __|
| ' <   / _ \\  | _ \\| (_) || (_) |\\__ \\| _|  _ | |   | __ || _| 
|_|\\_\\ /_/ \\_\\ |___/ \\___/  \\___/ |___/|___|(_)|_|   |_||_||___|'''

    for line in title_picture.splitlines():
        print(f"{Fore.LIGHTYELLOW_EX}{Back.LIGHTRED_EX}{Style.BRIGHT}{line}{Style.RESET_ALL}")
        sleep(.094)

    print("Welcome to Kaboose.the!\nThe rules are simple...\n\tEnter the correct answer (A, B, C, or D)")

    print("Beginning Wave 1 (easy mode)")

    for char in DOTS:
        print(char + "\t", end="")
        sleep(.34)
    print()

    print("Beginning Wave 2 (intermidiate mode)")
    for char in DOTS:
        print(char + "\t", end="")
        sleep(.34)
    print()

    print("Beginning Wave 3 (HARD mode)")
    for char in DOTS:
        print(char + "\t", end="")
        sleep(.34)
    print()


main()