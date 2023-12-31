# -*- coding: utf-8 -*-
"""Assignment_5 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/114bNHQFfMNX6paaA0q14vJ95wwHD-SwE
"""

def buildTable(X, Y, match=1, mismatch=-1, gap=-1):
  print("Sequence 1:", X)
  print("Sequence 2:", Y)
  table = [[0]*(len(Y) + 1) for _ in range(0, len(X) + 1)]
  print("The initial alignment table is: ")
  row = 0
  for i in table:
    print(i)
    row += 1
  value = 0
  for i in range(0, len(table[0])):
    table[0][i] = value
    value += gap
  score1 = 0
  score2 = 0
  score3 = 0
  for i in range(len(X)):
    for j in range(len(Y)):
      if X[i] == Y[j]:
        score1 = table[i][j] + match
      else:
        score1 = table[i][j] + mismatch
      score2 = table[i][j+1] + gap
      score3 = table[i+1][j] + gap
      score_max = max(score1, score2, score3)
      table[i+1][j+1] = score_max
  print("The final alignement table is: ")
  row = 0
  for i in table:
    print(i)
    row += 1
  return table

def TraceBack(X,Y, match=1, mismatch=-1, gap=-1):
  j = len(X)
  k = len(Y)
  first = ''
  second = ''
  glue = ''
  while j>0 or k>0:
    if j>0 and k>0 and ((X[j-1] == Y[k-1] and table[j][k] == table[j-1][k-1] + match) or (X[j-1 != Y[k-1] and table[j][k] == table[j-1][k-1] + mismatch)):
      first += X[j-1]
      second += Y[k-1]
      j = j-1
      k = k-1
    elif j>0 and table[j][k] == table[j-1][k] + gap:
      first += X[j-1]
      second += '-'
      j = j-1
    elif k > 0 and table[j][k] == [j][k-1] + gap:
      first += '-'
      second += Y[k-1]
      k = k-1

TraceBack('TTGCT', 'CCTCCT', buildTable ('TTGCT', 'CTTCCT'))