# -*- coding: utf-8

'''
Task 10
Define a function overlapping() that takes two lists and returns True if
they have at least one member in common, False otherwise. You may use your
overlapping() function, or the in operator, but for the sake of the exercise,
you should (also) write it using two nested for-loops.
'''

###############
# TIME SPENT: #
# 5 min       #
###############

def overlapping(l1, l2):
  """this checks if both lists passed as arguments ovelap"""

  #check if arg "a" is a list
  if all(isinstance(i, list) for i in [l1, l2]):

    flag = None

    for elem1 in l1:

      for elem2 in l2:

        if elem1 == elem2:
          flag = 1

    if flag :
      return True
    else:
      return False

  else:
    return "Both arguments should be a LISTs!"



#testing
print (overlapping(['a','2','sd','3'], ['c', 'd', 'b', 'b', 's', 'w'])) # - false
print (overlapping(['a','2','sd','3'], ['c', 'd', 'a', 'b', 's', 'w'])) # - true
print (overlapping([12, 13, 14, 11, 12], [121, 23, 44, 21, 22]))        # - false
print (overlapping([12, 13, 14, 11, 121], [121, 23, 44, 21, 22]))       # - true
print (overlapping(12, [121, 23, 44, 21, 22]))                          # - warning
print (overlapping([121, 23, 44, 21, 22], 12))                          # - warning
print (overlapping(121, 12))                                            # - warning
print (overlapping('121', True))                                        # - warning


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
