# -*- coding: utf-8
'''
Task 29
Using the higher order function filter(), define a function filter_long_words()
that takes a list of words and an integer n and returns the list of words that
are longer than n.
'''

def filter_long_words(l, n):
  """this takes a list of words 'l' and an integer 'n' and returns the list of words that are longer than n"""



  res = filter(lambda a: len(a) > n, l)
  print res


# testing
list_ = ['INCLUDING', 'BUT', 'NOT', 'tiruvanantapuram', 'LIMITED', 'TO', 'THE', 'WARRANTIES']
filter_long_words(list_, 2)




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
# 15 min      #
###############
