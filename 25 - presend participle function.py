# -*- coding: utf-8
'''
Task 25
In English, the present participle is formed by adding the suffix -ing to the
infinite form: go -> going. A simple set of heuristic rules can be given as
follows:

If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
If the verb ends in ie, change ie to y and add ing
For words consisting of consonant-vowel-consonant, double the final letter before adding ing
By default just add ing

Your task in this exercise is to define a function make_ing_form() which given a
 verb in infinitive form returns its present participle form. Test your function
 with words such as lie, see, move and hug. However, you must not expect such
 simple rules to work for all cases.
'''

import re

def make_ing_form(s):
  """this generates present participle form of a passed Eng verb 's' in infinitive form.

        Heuristic rules are:
        If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
        If the verb ends in ie, change ie to y and add ing
        For words consisting of consonant-vowel-consonant, double the final letter before adding ing
        By default just add ing

        Don't expect such simple rules to work for all cases."""

  patt_ie  = re.compile('ie$')                      # ends with ie pattern

  patt_e   = re.compile('e$')                       # ends with e pattern
  exclusions_e = ['be', 'see', 'flee', 'knee']

  patt_cvc = re.compile('[^aeiouy][aeiouy][^aeiouy]$')                                       # ends with consonant-vowel-consonant pattern

  if  s.endswith('ie') :                            # ends with ie
    s = re.sub(patt_ie, 'y', s)                     # change ie to y and add ing
    s = s + 'ing'

  elif s.endswith('e') and s not in exclusions_e :  # ends in e
    s = re.sub(patt_e, 'ing', s)                    # drop the e and add ing (if not exception: be, see, flee, knee, etc.)

  elif re.search(patt_cvc, s) :                     # consonant-vowel-consonant
    s = s+ s[-1] + 'ing'                            # double the final letter before adding ing

  else:                                             # add ing
    s = s + 'ing'

  print s


make_ing_form('hug')



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
# 30 min      #
###############
