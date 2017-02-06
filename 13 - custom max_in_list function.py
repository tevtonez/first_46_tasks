# -*- coding: utf-8

'''
Task 13
The function max() from exercise 1) and the function max_of_three() from
exercise 2) will only work for two and three numbers, respectively. But suppose
we have a much larger number of numbers, or suppose we cannot tell in advance
how many they are? Write a function max_in_list() that takes a list of numbers
and returns the largest one.
'''

###############
# TIME SPENT: #
# 15min       #
###############

def max_in_list(l):
  """This returns a max number in a given list"""

  max_item = None
  prev_item = None
  curr_item = None

  for item in l:

    curr_item = item

    if curr_item > max_item:

      print "this is current prev_item:", prev_item
      print "this is current curr_item:", curr_item

      max_item = curr_item
      print "this is current max_item:", max_item

      prev_item = curr_item
      curr_item = None

    else:
      prev_item = curr_item
      curr_item = None

  return max_item




#testing
print(max_in_list([4, 19, 27, 1, 22, 3]))     # returns 27


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
