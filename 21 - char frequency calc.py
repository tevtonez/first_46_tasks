# -*- coding: utf-8
'''
Task 21
Write a function char_freq() that takes a string and builds a frequency listing
of the characters contained in it. Represent the frequency listing as a Python
dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").
'''

import re


def char_freq(s):
  """This returns a dictionary with characters and their frequency used in
  provided string 's'."""

  # splitting the string
  s_split = s.split(' ')

  # stripping the string
  s_stripped = ''
  for i in s_split: s_stripped += i
  s_stripped = s_stripped.lower()

  # the list of chars in string
  char_set = set(s_stripped)

  result_dict = dict()

  for char in char_set:
    result_dict[char] = s_stripped.count(char)

  return result_dict

print(char_freq("abbabcbdbabdbdbabababcbcbab"))


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
# 12 min      #
###############

