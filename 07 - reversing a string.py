# -*- coding: utf-8

'''
Task 07
Define a function reverse() that computes the reversal of a string. For example,
reverse("I am testing") should return the string "gnitset ma I".
'''

###############
# TIME SPENT: #
# 13 min      #
###############


def MyRev(s):
  """This returns reverted string """

  if isinstance(s, str):

    res = ''
    s_list = list(s)

    for n in range( len(s_list) ):
      res += s_list.pop()

    return res

  else:
    "Argument for MyRev function should be a string!"


#testing
print MyRev('I am testing')



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
