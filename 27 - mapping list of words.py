# -*- coding: utf-8
'''
Task 27
Write a program that maps a list of words into a list of integers representing
the lengths of the correponding words. Write it in three different ways:
1) using a for-loop,
2) using the higher order function map(), and
3) using list comprehensions.
'''


# given list
list_ = ['INCLUDING', 'BUT', 'NOT', 'LIMITED', 'TO', 'THE', 'WARRANTIES']


# 1) using a for-loop
def Map_1(l):
  """this maps a given list of words 'l' into a list of integers representing the lengths of the correponding words using FOR loop."""

  result = []
  for item in l:
    result.append(len(item))

  print result

print "using FOR:", Map_1(list_)


# 2) using map() HOF
def Map_2(l):
  """this maps a given list of words 'l' into a list of integers representing the lengths of the correponding words using 'map()' HOF loop."""

  result = map(lambda x: len(x), l)
  print result

print "using 'map()':", Map_2(list_)


# 3) using list comprehension
def Map_3(l):
  """this maps a given list of words 'l' into a list of integers representing the lengths of the correponding words using 'map()' HOF loop."""

  result = [len(item) for item in l]
  return result


print "using comprehension:", Map_3(list_)


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
# 25 min      #
###############

