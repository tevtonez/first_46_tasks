# -*- coding: utf-8
'''
Task 33
According to Wikipedia, a semordnilap is a word or phrase that spells a
different word or phrase backwards. ("Semordnilap" is itself "palindromes"
spelled backwards.) Write a semordnilap recogniser that accepts a file name
(pointing to a list of words) from the user and finds and prints all pairs of
words that are semordnilaps to the screen. For example, if "stressed" and
"desserts" is part of the word list, the the output should include the pair
"stressed desserts". Note, by the way, that each pair by itself forms a
palindrome!
'''


filename = raw_input ('Enter file path/name: ')

with open(filename) as a_file:

  # splitting lines into separate lists and words in the lines into list items
  lines_in_file = [a_line.rstrip().split() for a_line in a_file]


  for item in lines_in_file:

    #reverting the word #2 in line and comparing

    if item[0] == item[1][::-1]:
      print item[0],'and', item[1] , '- are Semordnilaps!!!'
    else:
      print 'no match.'


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
# 40 min      #
###############

