# -*- coding: utf-8
'''
Task 28
Write a function find_longest_word() that takes a list of words and returns the
length of the longest one. Use only higher order functions.
'''

import functools

def find_longest_word(l):
  """this takes a list 'l' of words and returns the length of the longest one."""


  lam = lambda a,b: a if (a > b) else b
  result = len(functools.reduce(lam, l))
  print result


# testing
list_ = ['INCLUDING', 'BUT', 'NOT', 'tiruvanantapuram', 'LIMITED', 'TO', 'THE', 'WARRANTIES']
find_longest_word(list_)


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
# 5 min       #
###############

