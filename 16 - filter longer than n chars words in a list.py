# -*- coding: utf-8

'''
Task 16
Write a function filter_long_words() that takes a list of words and an integer n
 and returns the list of words that are longer than n.
'''

###############
# TIME SPENT: #
# 5 min       #
###############

def filter_long_words(l, n):
  """This returns the list of words that are longer than 'n' in a given list 'l'."""

  long_words_list = []

  for item in l:
    if len(item) >= n:
      long_words_list.append(item)

  return long_words_list


print (filter_long_words(['a', 'list', 'of', 'tiruvanantapuram', 'integers', 'representing', 'one'], 5))


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
