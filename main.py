#
# Gavin McKenzie, Abram Head, Brandon Lehmann
# 2/16/24
# Main function for AP lang extra credit
import #NUnos file
from time import sleep

def main():
    print("Welcome to Kaboose.the!\nThe rules are simple...\n\tEnter the correct answer (A, B, C, or D)")
    print("Beginning Wave 1 (easy mode)")
    game(easy)
    sleep(1)
    print("Beginning Wave 2 (intermidiate mode)")
    game(medium)
    sleep(1)
    print("Beginning Wave 3 (HARD mode)")
    game(hard)
    sleep(1)


main()