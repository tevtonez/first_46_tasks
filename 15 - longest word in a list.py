# -*- coding: utf-8

'''
Task 15
Write a function find_longest_word() that takes a list of words and returns the
length of the longest one.
'''

###############
# TIME SPENT: #
# 6 min       #
###############

def find_longest_word(l):
  """This finds and returns the longest words in a given list 'l' """

  #check if the arg is a list
  if isinstance(l, list):

    #setting resulting var
    prev_res = None
    curr_res = None
    max_res = ''

    #iterating throug a given list
    for item in l:

      curr_res = len(item)

      if curr_res > len(max_res):
        max_res = item
        prev_res = curr_res
        curr_res = None

      else:
        prev_res = curr_res
        curr_res = None


    return max_res

  else:
    print "The argument should be a list"


print (find_longest_word(['a', 'list', 'of', 'tiruvanantapuram', 'integers', 'representing']))


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
