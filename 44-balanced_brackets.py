# -*- coding: utf-8
'''
Task 43
Your task in this exercise is as follows:
Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest.
Examples:

   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK
'''


from random import choice

# list of brackets
items = [ '[', ']']

def random_printer(num):

  # generating the string of brackets
  res_l = [choice(items) for i in range(num)]
  res = ''.join(res_l)

  # getting left and right halfs of the string
  half = num / 2
  left = ''.join(res[0:half:])
  right = ''.join(res[half::])

  # checking if the halfs of the string are mirrorred
  # flipping right side
  right_flip = ''
  for bracket in reversed(right):
    if bracket == '[':
      right_flip += ']'
    else:
      right_flip += '['

  if left == right_flip:
    print res, '   - OK!'
  else:
    print res, '   - NOT OK!'



random_printer(6)


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
#   20min     #
###############
