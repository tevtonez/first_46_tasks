# -*- coding: utf-8
'''
Task 40
An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse, A decimal point = I'm a dot in place. Write a Python program that, when started 1) randomly picks a word w from given list of words, 2) randomly permutes w (thus creating an anagram of w), 3) presents the anagram to the user, and 4) enters an interactive loop in which the user is invited to guess the original word. It may be a good idea to work with (say) colour words only. The interaction with the program may look like so:'''


from random import choice, shuffle, sample

file_name = 'files/ex40.txt'
with open(file_name) as file:

  # selecting a random line in file and stripping \n
  orig_word = choice(file.readlines()).rstrip()
  clue = ''.join(sample(orig_word, len(orig_word))).upper()

  guess = raw_input("Let's play a color anagram game.\nCan you tell what color '{}' is?\n".format(clue))

  while True:

    if str(guess) != orig_word:
      guess = raw_input("Nope, guess again for the anagram '{}':\n".format(clue))

    else:
      print "Correct. You win!"
      break



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

