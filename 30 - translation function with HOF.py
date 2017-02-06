# -*- coding: utf-8
'''
Task 30
Represent a small bilingual lexicon as a Python dictionary in the following
fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott",
"new":"nytt", "year":"ar"} and use it to translate your Christmas cards from
English into Swedish.
Use the higher order function map() to write a function
translate() that takes a list of English words and returns a list of Swedish
words.
'''

dictionary = {
              "merry":"god", "christmas":"jul",
              "and":"och",   "happy":"gott",
              "new":"nytt",  "year":"ar"
              }

def Translate(l):
  """this takes a list of English words 'l' and returns a list of Swedish words."""

  result = map( lambda li,key: str(li).replace(li, dictionary[key]) if str(li) \
                in dictionary else 'no traslation', l, dictionary )
  print result



Translate(['merry', 'christmas', 'and', 'happy', 'new', 'year', 'to', 'you'])





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
# 120 min     #
###############

