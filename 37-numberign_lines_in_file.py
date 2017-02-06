# -*- coding: utf-8
'''
Task 37
Write a program that given a text file will create a new text file in which all the lines from the original file are numbered from 1 to n (where n is the number of lines in the file).'''



file_name = 'files/ex37.txt'

with open(file_name) as file:

  line_num = 0
  new_lines = []

  for line in file:

    line_num += 1
    new_line = str(line_num) + '. ' + line
    new_lines.append(new_line)


# writing to the new file
new_file_name = 'files/ex37-updated.txt'
with open (new_file_name, mode = 'w') as updated_file:

  for item in new_lines:
    updated_file.write(item)

  print 'Done!'





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
# 20 min      #
###############
