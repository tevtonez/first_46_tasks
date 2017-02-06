# -*- coding: utf-8
'''
Task 31
Implement the higher order functions map(), filter() and reduce(). (They are
built-in but writing them yourself may be a good exercise.)
'''


# a simple map(function, sequence)
def CustomMap(func, seq):
  """this is a simplified HOF 'map(function, sequence)' map(func, *iterables) --> map object.
  Doesn't raise any exclusions and doesn't validate input variables"""

  return [func(x) for x in seq]



def CustomFilter(func, seq):
  """this is a simplified reduce(func, *iterables) function"""

  return [x for x in seq if func(x)]



def CustomReduce(func, seq):
  """this is a simplified filter(func, *iterables) function"""

  res = seq[0]

  for x in seq[1::]:
    res = func(res, x)

  return res


# test
numbers = [1, 2, 3, 4, 5]

print CustomMap(lambda x: x * 2, numbers)
print CustomFilter(lambda x: x>3, numbers)
print CustomReduce(lambda x, y: x + y, numbers)




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

