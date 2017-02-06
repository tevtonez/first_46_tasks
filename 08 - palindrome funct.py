# -*- coding: utf-8

'''
Task 08
Define a function is_palindrome() that recognizes palindromes (i.e. words that
look the same written backwards). For example, is_palindrome("radar") should
return True.
'''

###############
# TIME SPENT: #
# 8 min       #
###############


def Palindrome(s):
  """This checks if given word is a palindrome"""

  if isinstance(s, str):

    s_list = list(s)

    res = ''
    for char in reversed(s):
      res += char

    if res == s:
      return True
    else:
      return False

  else:
    "Argument for Palindrome function should be a string!"


#testing
print Palindrome('dude')



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
