# -*- coding: utf-8
'''
Task 24
The third person singular verb form in English is distinguished by the suffix
-s, which is added to the stem of the infinitive form: run -> runs. A simple set
of rules can be given as follows:

If the verb ends in y, remove it and add ies
If the verb ends in o, ch, s, sh, x or z, add es
By default just add s

Your task in this exercise is to define a function make_3sg_form() which given a
 verb in infinitive form returns its third person singular form. Test your
 function with words like try, brush, run and fix. Note however that the rules
 must be regarded as heuristic, in the sense that you must not expect them to
 work for all cases. Tip: Check out the string method endswith().
'''

import re

def endings(s):
  """this adds endings to the endlish words accrdingly to the next heuristic rules:
        If the verb ends in y, remove it and add ies
        If the verb ends in o, ch, s, sh, x or z, add es
        By default just add s
        Note:
        this doesn't work for all cases."""


  patt_ies = re.compile('y$')

  def Es_Ending(s):
    """this returns TRUE if the word ends with 'o', 'ch', 's', 'sh', 'x', 'z' """

    endings_list = ['o', 'ch', 's', 'sh', 'x', 'z']

    for i in endings_list:
      if s.endswith(i):
        return True



  if s.endswith('y'):
    s = re.sub(patt_ies, 'ies', s)
    print s

  elif Es_Ending(s):
    print s + 'es'

  else:
    print s + 's'


endings('party')






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
