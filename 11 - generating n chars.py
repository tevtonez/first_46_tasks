# -*- coding: utf-8

'''
Task 11
Define a function generate_n_chars() that takes an integer n and a character c
and returns a string, n characters long, consisting only of c:s. For example,
generate_n_chars(5,"x") should return the string "xxxxx". (Python is unusual in
that you can actually write an expression 5 * "x" that will evaluate to "xxxxx".
For the sake of the exercise you should ignore that the problem can be solved in
this manner.)
'''

###############
# TIME SPENT: #
# 4 min       #
###############

def generate_n_chars(n, char):
  """This generates string of 'char' 'n' times"""

  #check if arg "a" is a list
  if isinstance(n, int):
    if isinstance(char, str):

      res = ''
      for i in range(n):
        res += char

      return res

    else:
      return "The 2nd argument should be a string!"

  else:
    return "The 1st argument should be an integer!"




#testing
print(generate_n_chars(3, 's'))     # 'sss'
print(generate_n_chars(3, 3))       # warning abut 2nd arg
print(generate_n_chars('3', 's'))   # warning about 1st arg


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
