# PythonTraining
A bunch of exercices, personal project, tutorials ...

## Beginner Python Project FCC #

From Youtube : https://www.youtube.com/watch?v=8ext9G7xspg&t=7047s

Made : 
- **Madlibs** : A game of madlibs, use of string manipulation
- **Guess Nbr** : Implementation of function, and use of random library, we can guess a number and the computer can guess the number too
- **Rock Paper Scissors** : A game of rock paper scissor
- **Hangman** : Usage of a Json file full of word, to play the Hangman game with limited life in the CLI
- **Binary Search** : Implementation of binary search in python
- **TicTacToe** : Reproduction of TicTacToe game, using classes +  against a computer AI made with minimax algorithm, only win or draw

## Automation ##

From Youtube and improved for my usage : https://www.youtube.com/watch?v=vEQ8CXFWLZU&t=201s

Made : 
- **PhotoEditor** : With the pillow library and usage of file descriptors, modify pictures in batch, from the Edition directory to the Edited directory
- **YtbDownloader** : With pytube, enter a ytb video as an argument to download only its audio(a personnal choice)
- **Pdf Merger** : Put all your pdf files you want to merge in the tomerge directory, to find it merged in the merged directory

## Scrapping ##

**Writing Occurences :**

Personnal Project to familiarize myself with web scrapping and usage of matplot.

Usage of requests, beautiful soup, nltk, matplotlib.

Put as an argument the frontpage of a webpage, it'll request the html content, parse it, find the links, and get the content of theses pages (limit put to 30 links, otherwise issues is encountered).

Put all the raw text in a output.txt.

Then use nltk to tokenize, parse it, use stop word to lessen the number of non-interesting data then represent the data on a graph to look at with matplotlib.

For example, here is the program used on a french news website (bfmtv.com) :
![Schema](/Scrapping/ScrapWritingOccu/figure.png)
