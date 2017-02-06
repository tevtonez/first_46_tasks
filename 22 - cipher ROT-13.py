# -*- coding: utf-8
'''
Task 22
Your task in this exercise is to implement an encoder/decoder of ROT-13. Once
you're done, you will be able to read the following secret message:

"Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"

Note that since English has 26 characters, your ROT-13 program will be able to
both encode and decode texts written in English..
'''

key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

def decoder(s):
  """this prints decoded ROT-13 string 's' that is written in Eng"""

  s_encoded_list = list(s.split())

  splitted_encoded_list = []
  for item in s_encoded_list:
    splitted_encoded_list.append(list(item))


  for n, item in enumerate(splitted_encoded_list):
    for n2, item2 in enumerate(item):
      for real, coded in key.iteritems():
        if item2 == coded:
          splitted_encoded_list[n][n2] = real

    splitted_encoded_list[n] = ''.join(item)

  decoded_s = ' '.join(splitted_encoded_list)
  print decoded_s

decoder("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!")


def encoder(s):
  """this encodes passed string 's' that is written in Eng with ROT-13
  algorithm"""
  coded_s = ''

  for char in s:
    if char in key:
      for real, coded in key.iteritems():
        if char == real:
          coded_s += coded
    else:
      coded_s += char

  print coded_s

encoder('test Test!')




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
# 60 min      #
###############

