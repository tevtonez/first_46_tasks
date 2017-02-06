# -*- coding: utf-8
'''
Task 41
In a game of Lingo, there is a hidden word, five characters long. The object of the game is to find this word by guessing, and in return receive two kinds of clues: 1) the characters that are fully correct, with respect to identity as well as to position, and 2) the characters that are indeed present in the word, but which are placed in the wrong position. Write a program with which one can play Lingo. Use square brackets to mark characters correct in the sense of 1), and ordinary parentheses to mark characters correct in the sense of 2). Assuming, for example, that the program conceals the word "tiger", you should be able to interact with it in the following way:'''


from random import choice

#with open('files/ex40.txt') as file:

# selecting a word from file
word = 'snake' #choice(file.readlines()).rstrip()



guess = str(raw_input('\nGuess 5 chars long word.\n')).lower()

while True:

  while len(guess) != 5:
    guess = str(raw_input('\nThe guess shoul be 5 chars long! Try again.\n')).lower()

  if guess == word:
    print "\nYou win!"
    break

  clue = ''
  for i in range(5):

    if guess[i] == word[i]:
      clue += '[' + guess[i] + ']'

    elif guess[i] in word:
      clue += '(' + guess[i] + ')'

    else:
      clue +=  guess[i]

  print "\nClue:", clue
  guess = str(raw_input('\nTry again.\n')).lower()




# Copyright (c) 2016, Konstantin Chernukhin, All rights reserved.
# Created as a part of learning and practicing process.
#
# Author's url: http://octogear.com
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# IABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


###############
# TIME SPENT: #
#   120min    #
###############

