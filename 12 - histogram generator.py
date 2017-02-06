# -*- coding: utf-8

'''
Task 12
Define a procedure histogram() that takes a list of integers and prints a
histogram to the screen. For example, histogram([4, 9, 7]) should print the
following:
****
*********
*******
'''

###############
# TIME SPENT: #
# 8 min       #
###############

def histogram(l):
  """This generates a histogram made of '*' symbols repeated 'n' times
  accordingly to the number in list 'l1' passed as the argument"""

  #check if arg "a" is a list
  if isinstance(l, list):

      for i in l:
        print '*' * i

  else:
    print "The argument of 'histogram' function should be a list!"




#testing
histogram([4, 19, 27])     # as per spec

print

histogram(34)              # warning

print

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
