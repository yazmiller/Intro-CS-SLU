# -*- coding: utf-8 -*-
"""Lab 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_KT6Vm2EdTW9Snxyq7_o9n1oKENrOwkD
"""

#1
table = [[1, 1, 1],
         [2, 2, 2],
         [3, 3, 3]]
print(table)

#2
for i in range(0, len(table)):
  print("row", i, ":",table[i])

#3
for i in range(0,len(table[0])):
  table[0][i] = -1

print('Update Table')
for i in range(0,len(table)):
  print("Row", i, ":", table[i])

#4
for i in range(0,len(table[0])):
  table[i][0] = -1

print('Update Table')
for i in range(0,len(table)):
  print("Row", i, ":", table[i])

def alignment_table(sequence1, sequence2):
  print('sequence 1: ', sequence1, "with length of", len(sequence1))
  print('sequence 2:', sequence2, "with length of", len(sequence2))
  print('the intitial table with dimension 10 and 8 for the sequence alignment is:')
  alignment_table = [[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0]]
  for i in range(0, len(alignment_table)):
    print('row', i, ":", alignment_table[i])

#5
alignment_table('AATTATATT', 'ACGTTAT')

#6
def alignment_table_update(sequence1, sequence2):
  print('sequence 1: ', sequence1, "with length of", len(sequence1))
  print('sequence 2: ', sequence2, "with length of", len(sequence2))
  print('the update table with dimension 10 and 8 for the sequence alignment is: ')
  alignment_table_update = [[0,-1,-2,-3,-4,-5,-6,-7],[-1,0,0,0,0,0,0,0],[-2,0,0,0,0,0,0,0],[-3,0,0,0,0,0,0,0],[-4,0,0,0,0,0,0,0],[-5,0,0,0,0,0,0,0],[-6,0,0,0,0,0,0,0],[-7,0,0,0,0,0,0,0],[-8,0,0,0,0,0,0,0],[-9,0,0,0,0,0,0,0]]
  for i in range(0, len(alignment_table_update[1])):
    alignment_table_update[i][0]
  for i in range(0, len(alignment_table_update)):
    print('row', i, ":", alignment_table_update[i])

alignment_table('AATTATATT', 'ACGTTAT')