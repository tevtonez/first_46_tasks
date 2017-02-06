# -*- coding: utf-8
'''
Task 34
Write a procedure char_freq_table() that, when run in a terminal, accepts a file
name from the user, builds a frequency listing of the characters contained in
the file, and prints a sorted and nicely formatted character frequency table to
the screen.
'''

file_name = raw_input('Enter a file name: ')

with open(file_name) as a_file:

  # fillig int 'freq' dictionary with data
  freq = dict()

  for line in a_file:

    line = line.lower().rstrip()

    char_holder = ''

    for char in line:

      #decorating spaces
      if char == ' ':
        char = ' _sp'

      if char in freq:
        freq[char] += 1

      else:
        freq.update({char : 1})

  # build a grid
  def Grid_Builder( freq_list, rowdivider ):

    sep_dashes = '---------' * rowdivider
    separator = sep_dashes
    i = 0
    cell_row1 = ''
    cell_row2 = ''

    # printing the header
    print separator
    print '|' , 'Unique chars found in the file:'.center(rowdivider * 9 - 4, ' '), '|'
    print '|', str(len(freq_list)).center(rowdivider * 9 - 4, ' '), '|'


    # assembling the rows
    for k in sorted(freq_list):

      row_k = []
      row_v = []
      s_val = str(freq_list[k])
      row_k = '|' + k.center(7, ' ') + '|'
      row_v = '|' + s_val.center(7, ' ') + '|'

      cell_row1 = cell_row1 + ''.join(row_k)
      cell_row2 = cell_row2 + ''.join(row_v)
      i += 1

      # breaking the row after 'rowdivider' cells
      if i == rowdivider:
        print separator, '\n', cell_row1, '\n', cell_row2, '\n', separator
        i = 0
        cell_row1 = ''
        cell_row2 = ''

    # if there is not full row of cells:
    if len(freq_list) % rowdivider != 0:

      keys_l = sorted(freq_list.keys())
      keys_offset = len(freq_list) % rowdivider + 1
      missing_pairs_l = keys_l[-1 : -keys_offset : -1]
      missing_pairs_l_rev = missing_pairs_l[::-1]

      cell_row1 = ''
      cell_row2 = ''

      for k in missing_pairs_l_rev:

        row_k = []
        row_v = []
        s_val = str(freq_list[k])
        row_k = '|' + k.center(7, ' ') + '|'
        row_v = '|' + s_val.center(7, ' ') + '|'

        cell_row1 = cell_row1 + ''.join(row_k)
        cell_row2 = cell_row2 + ''.join(row_v)

      print separator, '\n', cell_row1, '\n', cell_row2, '\n', separator


Grid_Builder(freq, 6)
print "\nDone!".upper(), '\n', 'proudly go to sleep :p\n'

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
# 180 min     #
###############

