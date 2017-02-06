# -*- coding: utf-8
'''
Task 26
Using the higher order function reduce(), write a function max_in_list() that
takes a list of numbers and returns the largest one. Then ask yourself: why
define and call a new function, when I can just as well call the reduce()
function directly?
'''

import functools


def max_in_list(l):
  """this returns the lagest number from a passed list of numbers 'l' using HOF reduce()."""

  print functools.reduce(lambda a,b : a if (a > b) else b,  l)


max_in_list([47,11,42,102,13])





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
