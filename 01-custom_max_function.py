'''
TASK 01:
Define a function max() that takes two numbers as arguments and returns the
largest of them. Use the if-then-else construct available in Python. (It is
true that Python has the max() function built in, but writing it yourself is
nevertheless a good exercise.)
'''

def My_Max_Func( a, b ):
    """This prints a maximum number out of 2 given"""

    # check if the input is integer
    if not all(isinstance(i, int) for i in [a, b]):
        return 'Pass only INTEGERS to My_Max_Func function!'

    #if numbers are equal
    elif a == b:
        return 'Arguments are equal!'

    else:
        #comparing numbers
        if a > b:
            return a
        else:
            return b

print My_Max_Func(21, 23)


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
