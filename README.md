# Hangman Word Guessing Game

## introduction

Hangman is CLI based game. Guess the letters in the secret word to solve the puzzle. You'll score points for each solved word; if you reach 3 points you'll win the game.

It can be played alone in single player mode and with your friends in multiplayer mode.

> If you are not satisfied with list of words that this game provides, why don't you challange your friends with custom words? _Check out [features](#features) section below for more information._

## rules

- You need to **guess given word** each round.
- There are **6 chances** to make a mistake. After 6th mistake you lose current round.
- There is **no time limit** to guess the word.

## features

- basic functionalities
  - automatic word (from list of words) provision for user to guess
  - checker for provided letter
  - providing 6 chances to guess the word and continue guessing until finding word
    or using all chances
- providing emotions based on status of guess, i.e. supporting or praising the user
- alerting about repeatedly typed letters (for one letter guess)
- typing "show" keyword to get previously typed letters
- multiplayer feature
  - collecting names of player(s)
  - leaderboard
  - challenging the opponent by providing custom word
- different points for normal words (1) and custom words (2 pts)
- chance to get 3 hints during one game
- ask how many rounds players want to play
- prompt for providing hint when 2 chances are left

<hr>

## potential features

> maybe in the next versions :)

- [ ] not selecting previously provided words (yes, words are totally random now. Don't judge my laziness...)
- [ ] add detailed guideline (long version)

## no way features

> this features will never be implemented.

- drawing a hangman :)
- colored messages
- adding provided words to word list
