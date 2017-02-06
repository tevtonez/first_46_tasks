# -*- coding: utf-8
'''
Task 45
A certain childrens game involves starting with a word in a particular category. Each participant in turn says a word, but that word must begin with the final letter of the previous word. Once a word has been given, it cannot be repeated. If an opponent cannot give a word in the category, they fall out of the game. For example, with "animals" as the category,

Child 1: dog
Child 2: goldfish
Child 1: hippopotamus
Child 2: snake
...
Your task in this exercise is as follows: Take the following selection of 70 English Pokemon names (extracted from Wikipedia's list of Pokemon) and generate the/a sequence with the highest possible number of Pokemon names where the subsequent name starts with the final letter of the preceding name. No Pokemon name is to be repeated.

audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon
cresselia croagunk darmanitan deino emboar emolga exeggcute gabite
girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan
kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine
nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2
porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking
sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask
'''
'''
s = 'audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask'
'''

s = 'audi mazda mercedes iveco opel isuzu'
#mazda / audi / iveco / opel = 4

pokemons_l = s.split()


def Generate_Next_Nodes_dict(names_list):
  """this generates dictionary of the names as a keys and lists of the next nodes as values from given 'names_list'."""

  next_nodes = dict()

  for name in names_list:

    next_nodes_l = []

    for next_node in names_list:

      if next_node != name and next_node[0] == name[-1]:
        next_nodes_l.append(next_node)

    next_nodes[name] = next_nodes_l

    print next_nodes

  return next_nodes



global path, next_nodes_dict, used_items
path = []
used_items = []
next_nodes_dict = Generate_Next_Nodes_dict(pokemons_l)



def extract_name_from_list(name, names_list):
  reduced_list = names_list
  reduced_list.pop(reduced_list.index(name))

  return reduced_list



def Find_All_Paths(names_list):

  all_paths = []

  for name in names_list:

    all_paths.append(Generate_All_Paths_From_Name(name, names_list))

  return all_paths



def Generate_All_Paths_From_Name(name, names_list):

  print "\ncurrent item: ", name

  name_holder = name

  used_items.append(name)

  path.append(name_holder)
  print "current path: ", path

  next_nodes_available = next_nodes_dict[name_holder]
  print "next nodes available: ", next_nodes_available

  if next_nodes_dict[name_holder] > []:

    for next_node in next_nodes_available:

      if next_node not in used_items:

        print "next_node: ", next_node
        Generate_All_Paths_From_Name(next_node, names_list)

  else:
    return path
    del path[::]
    pass

  return path




'''
  name_holder = name

  available_names_list = extract_name_from_list(name, names_list)
  print "\navailable list: ", available_names_list
  path.append(name_holder)
  print 'current path: ', path

  # find the list of words for name
  next_nodes_for_name = next_nodes_dict[name_holder]

  if len(next_nodes_for_name) != 0  :

    for next_node in next_nodes_for_name:
      print 'next_node: ', next_node

      while len(next_nodes_dict[next_node]) > 0 and next_node in available_names_list:
      #if len(next_nodes_dict[next_node]) > 0 and next_node in available_names_list:
        #path.append(next_node)
        #print 'current path: ', path
        Generate_All_Paths_From_Name(next_node, available_names_list)

      else:
        path.append(next_node)
        print 'current path: ', path

      if next_node in available_names_list:
        path.append(name_holder)

      """else:
                          path.append(next_node)
                          del path[::]
                          available_names_list = names_list"""

  else:
    path.append(name_holder)

'''


print 'all paths: ', Find_All_Paths(pokemons_l)

print len(max(Find_All_Paths(pokemons_l)))




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
#   20min     #
###############
