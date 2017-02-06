# -*- coding: utf-8

'''
Task 17
Write a version of a palindrome recognizer that also accepts phrase palindromes
such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on
no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan,
oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
"Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation
, capitalization, and spacing are usually ignored.
'''

###############
# TIME SPENT: #
# 22min       #
###############

import re

def Palindrome2(s):
  """This returns TRUE if a given phrase 's' is a palindrome."""

  # splitting 's' into a list stripping the punctuation and spaces
  s_split = re.sub("[^\w]", " ", s).split()

  # putting all 's_split' list items in into one string, no spaces, no
  # punctuation
  s_stripped = ''
  for item in s_split:
    s_stripped += str(item).lower()

  # iterating through original stripped string and getting reversed string
  # then comparing with original string
  res = ''

  for i in reversed(s_stripped):
    res += i

  if res == s_stripped:

    return True
  else:
    return False


print (Palindrome2('Was it a rat I saw?'))
print (Palindrome2("Dammit, I'm mad!"))
print (Palindrome2("NoT a< pal ! indrommee23"))

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
