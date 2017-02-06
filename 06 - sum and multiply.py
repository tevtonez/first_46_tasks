# -*- coding: utf-8

'''
Task 06
Define a function sum() and a function multiply() that sums and multiplies
(respectively) all the numbers in a list of numbers. For example,
sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
'''
###############
# TIME SPENT: #
# 8 min       #
###############


def MySum( l ):
  """This adds all numbers in a list"""

  #checking if arg is a list
  if isinstance(l, list):

    #adding all numbs
    result = 0

    for numb in l:
      result = result + int(numb)

    return result

  else:
    return "Argument is not a list"



def MyMUlt( l ):
  """This multiplies all numbs in a list"""

  #checking if arg is a list
  if isinstance(l, list):

    #myltiplying all numbs
    result = 1

    for numb in l:
      result = result * numb

    return result

  else:
    return "Argument is not a list"



#testing
mylist = [1,3,4,5,5]

print ( MySum(mylist) )
print ( MyMUlt(mylist) )


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
