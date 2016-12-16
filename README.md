# Learning Sneaky Statues 

## About
"Help solve one of the greatest mysteries in history! In this game of sneaky strategy, players take turns moving eight “stone” Moai statues. Where do they move? How do they end up in a straight line? That’s up to you! Be the first to outwit your rival and arrange your four mysterious statues together in a straight line and win. But, wait! Your rival knows which statue you will move next. The question is…where will it go? Be careful, you might just unlock the secrets of Easter Island when you play Sneaky Statues!"
[More info here](http://marandagames.com/products/sneaky-statues-of-easter-island)

## How to play
1. Player one starts by places statue #1 on the board.
2. Player two continues with statue #2.
3. Once all 8 have been played, player one picks up #1 and replaces it.
4. The game ends once a player has all 4 pieces in a row

## Game.py 
Usage: running the command [python3 game.py] will launch a game against the computer.
The game only accepts input of the form 'x,y'. Do not include the quotes. If you mess up, the game will crash and you will lose. This will be fixed soon™. This file also contains the minimax and the focused minimax algorithms. 

## Board.py
The main class used to represent the game. Each board is a record of the locations of the players pieces. You can recursivly build and score a tree of boards, which is then used by the minimax search. 

## Network.py
Contains the layer class, which is used to build networks. Also includes the code used to evolve the networks, and save the best one.

## Piece.py 
Small class used to represent a statue on the board. 
