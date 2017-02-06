# -*- coding: utf-8

'''
Task 19
"99 Bottles of Beer" is a traditional song in the United States and Canada. It
is popular to sing on long trips, as it has a very repetitive format which is
easy to memorize, and can take a long time to sing. The song's simple lyrics are
 as follows:

"99 bottles of beer on the wall, 99 bottles of beer.
Take one down, pass it around, 98 bottles of beer on the wall.""

The same verse is repeated, each time with one fewer bottle. The song is
completed when the singer or singers reach zero.
Your task here is write a Python program capable of generating all the verses of
 the song.
'''

def Song99(s):
  """This replaces 'bottles of beer' in 99 botlles of beer  song and sings it"""

  count = 99
  for i in range(1, 100):

    print ("{} {} on the wall, {} {}. \nTake one down, pass it around, {} {} on \
            the wall.\n".format(count, s, count, s, count-1, s))
    count -= 1

    if count == 0: print "The end of song!"

Song99('flies')



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
# 8 min       #
###############
