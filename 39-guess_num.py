# -*- coding: utf-8
'''
Task 39
Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20. (Source: http://inventwithpython.com) This is how it should work when run in a terminal:
'''


from random import randrange

number = randrange(1, 20)
guessess = 0


name = raw_input('Hello! What is your name? ')
print "Well, {}, I am thinking of a number between 1 and 20.".format(name)


while True:
  guess = int(raw_input('Take a guess: '))
  guessess += 1

  if guess < number:
    print "Your guess is too low."
  elif guess > number:
    print "Your guess is too hight."
  else:
    break


if number == guess and guessess == 1: print 'That\'s insane, {}! You guessed my number from the first guess!!!'.format(name)
else:
    print "Good job, {}! You guessed my number in {} guesses!".format(name, guessess)




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
#   30min     #
###############
