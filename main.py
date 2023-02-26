import random
from dataclasses import dataclass, field

NUMBER_OF_PLAYERS = 6
MONEY_NUMBER = 7
POT_INCREMENT = 0.1


@dataclass
class Player:
    order: int
    hand: set = field(default_factory=lambda: {2, 3, 4, 5, 6, 8, 9, 10, 11, 12})

    def won(self):
        return len(self.hand) == 0


def roll_one_dice(faces: int = 6) -> int:
    '''Result from rolling one dice'''
    return random.randrange(1, 7)


def roll_two_dice() -> int:
    '''Result from rolling two dices'''
    return roll_one_dice() + roll_one_dice()


class Game:
    def __init__(self, number_of_players: int) -> None:
        self.number_of_players = number_of_players
        self.pot = 0
        self.players = {
            order: Player(order) for order in range(1, self.number_of_players + 1)
        }

    def turn(
        self, current_player: Player, next_player: Player
    ) -> tuple[Player, Player] | None:
        '''Simulates a round and returns the next pair of players. Returns None if there is a winner.'''
        if current_player.won():
            self.winner = current_player
            return

        dice = roll_two_dice()
        print(f'Dices marked: {dice}')
        if dice == MONEY_NUMBER:
            print(f'Player {current_player.order} has to increase the pot.')
            self.pot += POT_INCREMENT
            return next_player, self._get_next_player(next_player)
        elif dice not in current_player.hand:
            # Player has not the number in hand
            if dice in next_player.hand:
                # Next player has it
                print(
                    f'Player {current_player.order} has not the card and next player have it. Turn ended.'
                )
                next_player.hand.remove(dice)
                return next_player, self._get_next_player(next_player)
            else:
                # Next player doesn't have it
                print(
                    f'Player {current_player.order} has not the card, but neither next player. Plays again.'
                )
        else:
            # Player has the number in hand
            print(f'Player {current_player.order} has the card. Plays again.')
            current_player.hand.remove(dice)
        return current_player, next_player

    def _get_next_player(self, player: Player):
        order = player.order % self.number_of_players + 1
        return self.players[order]

    def start(self):
        current_player = self.players[1]
        next_player = self.players[2]
        self.round_number = 1
        print(f'Round {self.round_number}')
        print(f'Pot {self.pot:.2f}')
        next_turn = self.turn(current_player, next_player)
        self.round_number += 1
        while next_turn is not None:
            current_player, next_player = next_turn
            print(f'\nRound {self.round_number}')
            print(f'Pot {self.pot:.2f}')
            next_turn = self.turn(current_player, next_player)
            self.round_number += 1

    def print_results(self):
        print(f'Player {self.winner.order} won {self.pot:.2f}!')


def main():
    game = Game(NUMBER_OF_PLAYERS)
    game.start()
    game.print_results()


if __name__ == '__main__':
    main()
