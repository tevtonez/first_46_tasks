# -*- coding: utf-8

'''
Task 14
Write a program that maps a list of words into a list of integers representing
the lengths of the correponding words.
'''

###############
# TIME SPENT: #
# 8 min       #
###############

def MapWords(l):
  """This maps words from given list 'l' into integers epresenting the lengths
   of the correponding words"""

  #check if the arg is a list
  if isinstance(l, list):

    #setting resulting list
    res_list = []

    #iterating throug a given list
    for item in l:
      res_list.append(len(item))

    print res_list

  else:
    print "The argument should be a list"


MapWords(['a', 'list', 'of', 'integers', 'representing'])


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
