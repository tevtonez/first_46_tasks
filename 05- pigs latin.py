# -*- coding: utf-8

'''
TASK 05
Write a function translate() that will translate a text into "rövarspråket"
(Swedish for "robber's language"). That is, double every consonant and place an
occurrence of "o" in between. For example, translate("this is fun") should
return the string "tothohisos isos fofunon".
'''

def Translate(s):
  """This returns Swedish \"robbers' language\" """

  #the list of vowels
  vows = ['a', 'e', 'i', 'o', 'u', 'y', ' ']

  #converting the string into a list
  string_list = list(s)

  #iterating though list and concatenating a new string
  result = ''

  for char in string_list:
    if char not in vows:
      result += char + 'o' + char
    else:
      result += char

  return result

check = 'tothohisos isos fofunon'
print check

print Translate('this is fun')


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
