# -*- coding: utf-8
'''
Task 36
A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a language, the works of an author, or in a single text. Define a function that given the file name of a text will return all its hapaxes. Make sure your program ignores capitalization.
'''

from string import maketrans

def Find_Hapaxes():
  """this returns all hapaxes legomenon in user defined file 'file'"""

  # create the table of replacement for the translate method
  intab =  ",.?!/@#$%^&*()_-+={}[]:;|`~§\'\""
  outtab = "                               "
  transtable = maketrans(intab, outtab)

  # creating words' dictionary
  words = dict()

  # getting file name from input
  file_name = raw_input('Enter file name: ')
  with open(file_name) as file:

    for line in file:

      # cleaning and stipping the line
      line = line.lower()
      line_trimmed = line.translate(transtable).strip()
      line_split = [word for word in line_trimmed.split(' ')]

      # loading words dictionary with the words from text and calculating frecuency
      for word in line_split:

          if word == '':
            pass

          if word in words:
            words[word] += 1

          else:
            words.update({word : 1})

  # checkign if words dictionary contains Hapaxes
  if 1 in words.values():

    print 'Hapaxes for the file:', file_name, 'are:'

    hapaxes = [k for k, v in words.items() if v == 1 in words.values()]
    print ', '.join(hapaxes)

  else:
    print 'No hapaxes in the text :('

Find_Hapaxes()


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
# 2 hrs       #
###############
