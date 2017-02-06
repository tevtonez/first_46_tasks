# -*- coding: utf-8
'''
Task 23
Define a simple "spelling correction" function correct() that takes a string
and sees to it that 1) two or more occurrences of the space character is
compressed into one, and 2) inserts an extra space after a period if the period
is directly followed by a letter. E.g. correct("This   is  very funny  and
cool.Indeed!") should return "This is very funny and cool. Indeed!" Tip: Use
regular expressions!"
'''

import re

def correct(s):
  """this corrects spaces typos in the passed string 's'."""

  # defining the patterns
  patt_many_spaces = re.compile('\s{2,}')
  patt_space_after_dot = re.compile('\.')

  # putting patterns into a dict
  pattern_dic = dict()
  pattern_dic[patt_many_spaces] = " "
  pattern_dic[patt_space_after_dot] = ". "

  s_result = s

  for patt, repl in pattern_dic.iteritems():
    s_result = re.sub( patt, repl, s_result)

  print s_result


# testing
correct("This   is  very funny.  And  cool.Indeed!")


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
# 30 min      #
###############

