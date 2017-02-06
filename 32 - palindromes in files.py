# -*- coding: utf-8
'''
Task 32
Write a version of a palindrome recogniser that accepts a file name from the
user, reads each line, and prints the line to the screen if it is a palindrome.
'''

import re

file_address = raw_input('Enter file address/name: ')

with open(file_address) as a_file:

  stripped_line = ''

  for a_line in a_file:

    # splitting received line into a list stripping the punctuation and spaces
    line_split = re.sub("[^\w]", " ", a_line).split()

    # making a single string of a line_split
    line_stripped = ''.join(line_split)

    # lowering the case and reverting the line, then comparing with original
    reversed_line = ''
    for i in reversed(line_stripped.lower()):
      reversed_line += i

    if line_stripped.lower() == reversed_line:
      print "\"", a_line.rstrip(), "\" is a palindrome!"


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
# 20 min      #
###############

