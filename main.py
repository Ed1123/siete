import random
from dataclasses import dataclass

NUMBER_OF_PLAYERS = 6


@dataclass
class Player:
    order: int
    hand: set = set()


def roll_one_dice(faces: int = 6) -> int:
    '''Result from rolling one dice'''
    return random.randrange(1, 7)


def roll_two_dice() -> int:
    '''Result from rolling two dices'''
    return roll_one_dice() + roll_one_dice()


class Game:
    initial_hand = {2, 3, 4, 5, 6, 8, 9, 10, 11, 12}

    def __init__(self, number_of_players: int) -> None:
        self.number_of_players = number_of_players


def main():
    while True:
        print(roll_one_dice())


if __name__ == '__main__':
    main()
