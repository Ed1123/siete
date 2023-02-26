import random

NUMBER_OF_PLAYERS = 6


def roll_one_dice(faces: int = 6) -> int:
    '''Result from rolling one dice'''
    return random.randrange(1, 7)


def roll_two_dice() -> int:
    '''Result from rolling two dices'''
    return roll_one_dice() + roll_one_dice()


def main():
    while True:
        print(roll_one_dice())


if __name__ == '__main__':
    main()
