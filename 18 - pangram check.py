# -*- coding: utf-8

'''
Task 18
A pangram is a sentence that contains all the letters of the English alphabet at
least once, for example: The quick brown fox jumps over the lazy dog. Your task
here is to write a function to check a sentence to see if it is a pangram or not.
'''
import re

def PangramCheck(s):
  """this returns True if passed string 's' is a pangram or False if not."""

  #stripping given string
  s_split = re.split("[^\w]", s)

  #transforming list into a stripped string
  s_stripped = ''
  for i in s_split:
    s_stripped += i

  #making a set of chars
  s_set = set(s_stripped.lower())

  if len(s_set) == 26:
    return True

  else:
    return False



print (PangramCheck('The luck brown fox jumps over the lazy dog'))    #false
print(PangramCheck('The quick brown fox jumps over the lazy dog'))    #true
print(PangramCheck("Pack my box with five dozen liquor jugs."))       #true


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
# 17min       #
###############
