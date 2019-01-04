# Poker-Odds-Calculator
This Python program calculates the winning percentage of 2 hands (modifiable to include more hands) pre-flop, post-flop, post-turn and post-river.
A card is represented in the format of '<value><suit', eg.- 'As' represents Ace of Spades, 'Td' represents Ten of Diamond,etc.
Initially, a deck is generated and the two hole cards are inputted (can be modifed to take from user).
From itertools library, combinations function is used to generate list of all combinations of 5 cards from deck.
Since the possible combinations is very huge, rather than iterating through every hand, 1000 random hands are collected and a get_best_hand() function is generated to find the best hand from the hole cards are found and compared against each other and the winning hand is given a point or else the split gets the point.
A flop is geenrated and the process repeats of finding the winning percentage.
Similarly, turn and river cards are drawn with the updated winning percentages and finally the winning hand is printed.
