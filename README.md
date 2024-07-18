# Battleship game

Battleship game is a Python terminal game, wich runs in the Code Institute mock terminal on Heroku.
Users can try to beat the computer by find all of the computer's battleships. Each battleship occupies one square on the board.

Below is attached screen how it looks on different screen sizes

![Header](https://github.com/Yups11/battleship-game/blob/main/media/readme-photo-1.png)

## How to play
Battleship game is based on the classic pen-and-paper game. 
You can read more about it on wikipedia.org
In this version the computer(player 2) batleships is randomly generated. 
The player can't see where they are.
Guesses are marked on the board with an X. Hits are marked with an *.
The player can chose point on game area to try to sink battleship's.
The player win when all battleships are sink.

## Features
### Existing features
- Ships are random placed on computer boards
- The player cannot see where the computer's ships are
- 
![Header](https://github.com/Yups11/battleship-game/blob/main/media/readme-photo-2.png)

- Accept user input
- Maintains scores
- 
![Header](https://github.com/Yups11/battleship-game/blob/main/media/readme-photo-3.png)

- __Input validation and error-checking__
- You cannot enter coordinates outside the size of the grid
- 
![Header](https://github.com/Yups11/battleship-game/blob/main/media/readme-photo-4.png)

- You cannot enter the same guess twice
- 
![Header](https://github.com/Yups11/battleship-game/blob/main/media/readme-photo-5.png)


### Future features
- __Allows player to select the board size__
- __Allows player to have own ships and computer hit him to__

## Testing

- __I have manually tested this project by doing the following__
- Passed the code throw PEP8 linter and confirmed there is no problem wich can cause error
- Given invalid inputs: out of bounds inputs, same input twice
- Tested by my local terminal and the Code Institute Heroku terminal

### Bugs
- __Solved bugs__
- I comment the code on line 31-37 because random point on game area can be the same for both
players because is random for computer.

- __Remain bugs__
- No bugs remaining

- __Validator testing__
- PEP8 no errors were returned from PEP8online.com

## Deployment
### This project was deployed using Code Institute's mock terminal for Heroku.

- __Remain bugs__
- Fork or clone this repository
- Create a new Heroku app
- Set the buildbacks to Python and NodeJS in that order
- Link the Heroku app to the repository
- Click on DEPLOY

### Credits
- Code Institute for the deployment terminal
- Wikipedia for the details of the Battleships game
