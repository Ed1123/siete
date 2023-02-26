import random
from dataclasses import dataclass

NUMBER_OF_PLAYERS = 6
MONEY_NUMBER = 7
POT_INCREMENT = 0.1


@dataclass
class Player:
    order: int
    hand: set = set()

    def won(self):
        return len(self.hand) == 0


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
        self.pot = 0
        self.players = {order: Player(order) for order in range(self.number_of_players)}

    def turn(self, current_player: Player, next_player: Player) -> Player | None:
        '''Simulates a round and returns the next player. Returns None if there is a winner.'''
        if current_player.won:
            self.winner = current_player
            return

        dice = roll_two_dice()
        if dice == MONEY_NUMBER:
            self.pot += POT_INCREMENT
            return next_player
        if dice not in current_player.hand and dice in next_player.hand:
            next_player.hand.remove(dice)
            return next_player
        else:
            # Dice number in current player hand
            current_player.hand.remove(dice)
            return current_player

    def start(self):
        first_player = self.players[1]
        second_player = self.players[2]
        next_player = self.turn(first_player, second_player)
        while next_player is not None:
            next_player = self.turn(first_player, second_player)

    def print_results(self):
        print(f'Player {self.winner.order} won {self.pot}!')


def main():
    game = Game(NUMBER_OF_PLAYERS)


if __name__ == '__main__':
    main()
