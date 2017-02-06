# -*- coding: utf-8
'''
Task 43
An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse. Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that finds the sets of words that share the same characters that contain the most words in them.
'''


from itertools import permutations

"""# removing all weird words from dictionary (with & ' " and other chars in them)
with open('files/ex43.txt') as orig_file:

  new_file_text = [line for line in orig_file if "&" not in line and "'" not in line ]

with open('files/ex43clean.txt', mode='w') as new_file:
  for item in new_file_text:
    new_file.write(item)
"""



text_f_file = open('files/ex43clean.txt')

words = [line.rstrip() for line in text_f_file]

for word in words:
  if len(word) > 2:

    print "\nworking on word {}".format(word)

    perms_with_dups = [''.join(p) for p in permutations(word)]
    perms = list(set(perms_with_dups))

    for perm in perms:
      if perm in words and perm != word:
        print word, '==>', perm


"""
words = []
anagrams = {}

with open('files/ex43clean.txt', 'r') as file:
    for line in file:
        words.append(line.rstrip())

for word in words:
    anagram = "".join(sorted(word)) # 'hello' -> 'ehllo'
    if anagram in anagrams:
        anagrams[anagram].append(word)
    else:
        anagrams[anagram] = [word]

anagr_lengths = {}
for a in anagrams:
    l = len(anagrams[a])
    if l in anagr_lengths:
        anagr_lengths[l].append(a)
    else:
        anagr_lengths[l] = [a]

lengths = list(anagr_lengths)
max_length = max(lengths)
longest_anagrams = anagr_lengths[max_length]

for a in longest_anagrams:
    print(a + ": " + str(anagrams[a]))


"""





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
#   50min     #
###############

