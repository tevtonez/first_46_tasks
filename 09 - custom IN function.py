# -*- coding: utf-8

'''
Task 09
Write a function is_member() that takes a value (i.e. a number, string, etc) x
and a list of values a, and returns True if x is a member of a, False otherwise.
(Note that this is exactly what the in operator does, but for the sake of the
exercise you should pretend Python did not have this operator.)
'''

###############
# TIME SPENT: #
# 16min       #
###############

def is_member(x, a):
  """this checks if the first argument 'x' is in list passed as the 2nd argument
  'a'"""

  #check if arg "a" is a list
  if isinstance(a, list):

    flag = None

    for elem in a:

      if str(elem) == str(x):
        flag = 1

    if flag :
      return True
    else:
      return False

  else:
    return "The second argument should be a LIST!"



#testing
print (is_member('a', ['c', 'd', 'b', 'b', 's', 'w']))
print (is_member('a', ['c', 'd', 'a', 'b', 's', 'w']))
print (is_member(21, [121, 23, 44, 21, 22]))
print (is_member(21, 121))



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
