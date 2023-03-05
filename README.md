# siete
A simulation for a family bet game.

## Game
The game consist in a number of players with **10 cards (from 2 to 12 except from 7)** facing up so all players can see them. In each turn a player rolls **a pair of dices**. If the number he/she gets is **7**, the player has to **increase the pot** by a given amount (usually **10 cents**). If the number is one of the cards in his hand, he can turn that card and keep playing. If the number is not in his hand, he/she will have to check in the next player's hand. If the next player doesn't have the card, the current player can roll again, but if the next player has the card the turn is over and the next player can turn his card and roll the dices again.

The **game ends** when one player has **no cards left**. The winner takes the jackpot.

## Simulation
Given the random nature of the game I wanted to simulate it and see if any pattern emerges. And indeed, there are (unless they are because of the pseudorandomness).

## Run a simulated game
```console
python3 siete.py
```

## Multithreading vs Multiprocessing
In the code I experimented with both multithreading and multiprocessing functions and, as expected, only the multiprocessing approach had speed improvements. You can check the analyze notebook.

## Exploring patterns
I recommend using the included analyze notebook to perform analytics on the simulations. A remarkable one is that with 11 players the first player has an incredible higher probability of winning the jackpot.