# -*- coding: utf-8
'''
Task 38
Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).'''

import re

f_name = 'files/ex36.txt'

with open(f_name) as file:

  words = []
  statistic = dict()

  avg = 0
  total_words_len = 0

  print 'Working...'

  for line in file:

    # strip, split, drop spaces
    line = re.sub("[^\w]", " ",  line)
    line = line.split()

    # add words from whole line to words list
    for word in line:
      words.append(word)
      total_words_len += len(word)

  # calculate avg
  avg = float(total_words_len) / len(words)

  # print words
  print 'Done!\n', 'Average word length for this text is: ', avg





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
#  20 min     #
###############
