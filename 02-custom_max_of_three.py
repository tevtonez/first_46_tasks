'''
TASK: 02
Define a function max_of_three() that takes three numbers as arguments and
returns the largest of them.
'''

def My_Three_Max( a, b, c ):

    #checking if all numbers are integers
    if not all(isinstance(i, int) for i in [a, b, c]):
        return 'Pass only INTEGERS to My_Three_Max function'

    # if all numbers are even
    elif a == b == c:
        return 'All arguments are even!'

    else:

        #comparing numbers
        if a > b  and a > c:
            return a

        elif b > a and b > c:
            return b

        elif c > a and c > b:
            return c


print My_Three_Max(2003, 2020, 2100)


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
