# -*- coding: utf-8 -*-
"""assignment6 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16Z-GvCZDfaiEHyFspB4RXY9fAMwKDcFB
"""

#11
def wabbits(n,k):
  if n == 0:
    return 0
  if n == 1:
    return 1
  else:
    return wabbits(n-1, k) + k*wabbits(n-2, k)
print(wabbits(31,5))

#12
max_gc = 0.0
DNA = '''>Rosalind_1480
GGCACAATCGCAGTCGTGGGAGTTAGAAACGGACCTCCCGTCAAAATCGTACAACCTTTTTCAGCGTGGCAACTCTTCAACACTAAAGCAATAGTGATCTGTACAATGATCAAACGAGTTCGCCCCACTGCTGGCGCGCTCCTCGGCCATTAATCTGCTCGATATTATTATTACCGGCGTTAGCGTCAGGCATCAAAGTCGGGGACCGACGGGGTTAACAGAAGCTGAGAGGGACTAGAATGCTGACTCCAAGATCCCAGGCAATTGGAAGTCTGCTACGACCCGTTGAATTCGTTCACGAAGCATGGCGCTTGCCATTAGACCCAACCCTGCCCCCGGCCGGACTCGCGTGCCAGTCAGCGATCAACCAAGTGTGCCCTACCTCATTGTATCCAAGTTCGATTGCAATGCAAAGTGAGGAAATAGTACAAGCGTACCTGGGGTAAGCCCTCCCCTCCCTCCCATGTATTCAGCGCGCAGGCATTGCCTAGGATGGTGTAACAGTATCCTCAGGTGTCTCTGGAGACCGGCCCGATAACGCGCCACGGTCAGGACAGGGATAGGTAGGAAAAAACTCGTTTTCCGCACATTGATTCCGCTGACTCGCATTCTGGCAGAGAGTCCGTCGTGTTCCAGACGACTTCAATCCCGTTGTATCTG
GCTCACCATCCTAGCTAAATGGCGGTAGTACATAACCTACAAGCCCCGTGAAAACTTGGA
ACTACAGGTAATTGTTACACTATCCCCGCTCTAGCTATCCTTGGGCCTTGGAGTTCTCCA
TCCTTTCTTTGCTGCTTGCCGGATCAAATACGGCCACGTGACATAAGCAGGGTCTAATCG
TCGATAAGAGTCTCAC
>Rosalind_7813
ACGGACGCCTGAAGCAGGGCAACACGTCGCGGGGAGTTAGCGCAGATAAAAGATTTCCCG
CTCCCTGCCGGTTCATTGATGCTCTCCGAGGCATAGGTCAGCCCTACCCGGCTGGCAGGA
TAAATGCGGTCGATTCGAGTATCGTGGCTCCTACGAATGTTGGATTAGATGTTATGTCTT
GATTGTCTGAACCCATATGCCCGTAGTGAGTTCTACTAACACTAGATCCATCTAGCACGG
TACTTACTACGTGATAGGGTCCCGAGTCAATAGTGGTATATAAGGTGGATTGGGATACCC
CCGAGTAAGTATATCCATACTCATCATAGCGGGATATTAGGCCTCTACGTTCTATGTGAT
ACCACCGAGCCCGGATAGCTGGCTACCATCAATTACCCAAGGTCACACACCATCTGCTCA
TCAAACCGTTCATGTATCCATCTGGGAACACAGGCGAACAAGCTCGTGCAGGGGACGAGT
CGAACAAATCGGTGTGACAACGCCGTGTACCCCTATTTTGAATAAAGTGTACAGGAATCA
GTCACTAGCCAAACAAGGAGAGTGTTCTCCTCAGAGAAGAAAGCCGGGTATCCGCTAAAT
CGTGCGTTGGGCCCACGGGTTACACCGTTGGGCGAGCAGGATGTGTTGCAGACCGGGCAT
TATAACAATTAGATATAGTTGGAAAAGTCTGTGTGGTTTCATTGACCGTCAATAAGCGTC
ATCTCTGGCGTCCACCCTAAACGCGCGGTCTCTGGAACTCAGAACATTCTAATTTACCGT
CGTGGACCTGCTTTACGGAAACCGCTGTAAAGTAGATGCTGCGAGACTTTAATGTCAAGC
GGAGCAATGCTTAACGAATACAGCAGTGCACCGTTGTCCGGCTGAATTCGCGGTCTGGAG
AGATGTAAATCAAATCGGAATACTCGCGTCGCTGGG
>Rosalind_7455
TTGATCGGCACTAGTAGCAAATTCTTACAGAACACTGCCAAGTAAAACTGCGATCCCGGC
ATTCGAACTGGGGGCCCTAGAGGACCTCGCCACGCGCCCTAGTCATATAACAATGGATGT
AGATATCGGTGTCTTTGCTACGGCTCGCCGCACTGGTTCATGCCAACTGCACGCGAATAC
GTATGAGACTACTCGGCGTTATTACGCAAACGGAAACGCGGTCCGTTACGAAATGCGCCT
CCTATCGAAGCGCCGATAGCAAGGATCGACAATTTCGGGTCATCGACATCTGCACGGGTG
TATCCGGTAGCATTACCCGTTATGTGCGTTGTTTGTGATCAACACTCGCGCGGACTCCAG
GAGTTTGTTTTGTTGATAACAACAGATTATAACGCCGAATACCGTCAGGTTGGCTTCATT
GCGGCTAACCGACGCCCTCACGGCCAATCGAACCTGGTAGCTCGGAGCTTGGTGCCATCG
CGAGATATCTCAGCGTAATGTACCAATTCCTGCTTTGACGAATCGAGTCTTGTGTCTCTA
AACACATAGCACTACTGGATCACTTAGGGTCTTTTCACATGGTACGAAGCAAACATTGTT
TTCATTCTCCGTTGCCTAGGGAAAACGCGAGCTGTTCGTGTGGACATACAGCATAAAAAT
ATCCGTCTCTCTCACGATGCAAAAACGATCCCGAATATCGCGGGGACTTGTGGTTCTTAG
CTATGTAGACGCCATAAGCCCACAACGTCAAATAGGGGTGCTGCACGCTTTATAGGAGGT
CTAGGAAGTGGATCTCGGTGAAAGGTTACTGGGGCCGCACTCGAATCGTTGTCAAGGCGC
ACGCATGCTCGAAGACGTGTTAGGAACCCGAGCCGTTTTCAGTAAGCAAGCGGAAACCGC
ATAGCCTCCCAGAGAATTTTGCTTCGGAAGTTGTGTCACCGGGATTGTATGCCTAAACGT
TGCTACGGACCGTTTAAGTGACGGC
>Rosalind_2671
TAAGACGTGGGCACAGGCCTGGTGTTCAACCACGGTTTCTCATGAACGAATGCTGTACTT
TCCCCCTACACGCGTGTAATTAAGGAGATGCTTAGGCAGTAAAAGTACCTAGGTGCCTTC
ATCGTATCCGGCTAACGGACGTCGGGCGTGGATGATCTTAGGGGCAGTCAGAGTGTTTCT
GCCTGGGTGGTCCAAACCGCGTCGCCTGCGATGTCCTCAAAAGTGTATTGTAAGGAACTG
AATGTGTGACCGAAAGACGAAAGCACGAAGTCAGACTATCCAAGAAATTAGCATGAATGA
CGTGACGCTGGCAATGGTCGGCGTACAAATGCGTTGGGTAACGCGAGCGTTGCGTAAGAT
AGACGGACATTAGTTCATCCGTCTCCGCTATCCCGTGCCTTATAAGGTGCTCGAGAGGTA
GGCCATAATACGATCCGTGCAAGCCGCGAGGAGGTGAGTATGGCAACAACCCTTACGAGA
AATGCTGATCCGTTCAGATGACTCCGTGGATTGGATTTCTGTGGCTCGGGGTGCACCCGA
TTTTGAACCGCCCCTGAAAGCCCCCGAGCCTTATGTACCAGGTCTTGGAGTGGATAATTT
AGTACTCTAATGGCCATCAAGTCCAACTTTGTACATTGTATGTTGCCTGGGTCTAAGCAC
ATCCTTTTAAGGAACCGCCACTGTCCTAGTGGATCTGGCATCGGTAATGAATGGAAGAGT
CTGCGAATCAAAACGTTGACTAGTTTAACCAATGTCTAGATAGCTTATAGGGTTAACACG
GCCAAAGAACTCTCCCTTAGCATCGCAAGTATGCCTACCACGAGCTTCGTAGACTGCGAT
GATGGCCAGGCTCATTAAGTGTTGGGTAATATTAGACGCTAATATTTAGCGCCCCCGACA
TTCAGCATTATGAACCAACGCCGGAAAGTAAGCGGGACTGAAGACCCCCTGGTCAATAAT
TA
>Rosalind_0956
TCGAACTTTATAGTCGTGATATCTCGGCCTTTAACCATATGCCTCGATTATATCCTCTGA
ACGCATCGGGTAAGTGCTATGCTTAACTATCTTGTCGTTCTGTTGATACCATGTTGTAAG
TCGAGGGTAAGGGGTGTCAGGTGTACCACAATTTGGACTGCTTTTATGGTCGGCAGACAT
CTTTGCGGCGAATCCGTATCGTTCGTAGAAGACGGGAATGGAACGTTGGCTAAGAATGGC
CTAGTCCGGAAGAGGCCAGCGGATCTCATTCGTCGGGAAGCCGAGCGTCTTGACTGGTGG
GTGCGAGTGACTTTTCCGTTATCGCTGTCTCATACTACAAACTAATAGACTCTTGAATAC
TACTGATCGTGACTTCATTGTACAGGTATATTCTGCTCACCATTTTTACGGCCTCTCGGA
GCTCCTCCGTGACTTGTAGATACGTACTGACGCCACGGCGCCATGAATGCAATACGTCGG
CAGTAGTTAACTACGACACCAATCCTTGTTCGCGATCGCCGGAACACGAGTGCCGCGGAC
TTAAGTCAGAACAATATATCGGCCCTTAATATCTCACCCTGACATATCGAGGTTTCAAAA
CATACATTGCGCAGATGCCTAACGACGACCGCCCATGCTTGCGAAATTAAACTGGTTTAG
ACCTTTTATAGGTCTTCAGCACGCGATCTTCGACGGACAAACAAGCCCGACCGAGCAAAC
ACTAGGGCTCTTGAACTGATGCGCGCCCGCATAGGGAAGTTTGACATGGTGCCAAGAAGA
GCAGCCCCAGGCTCACACCCCCTAAACGCGCGTAAGTAAAAGCGAATGTACACGGCCATA
GCGTCCAGTCAACCCGGGGCACTCGGCATGCTGGACATTGTCGTGTCTACACTCCGTG
>Rosalind_6127
GACTTTATATCGCGATGACCATCAGGATTTCTAGCACCTGCCCTCGACGTGTTATTAGAG
TCTGTTGTATATTACGATATCGTTGACCGATTATCAGGGAGTGTTGGCCGTGGGCACAAA
TCTTTCATATCTAGAGACATTAGCCGGTTAGAGCATGCATATACCGTGTTTTAGTCGCCG
TAGGAGAAAGTTGCGCTGGCCGCGTACTATTGAATGGGGGATACCAAAATCTAAGGATTG
GATCCCCGGCTTCAGTTGGTGAATAACCGCGCTAGAGGGGGTTTTTAGGGGGGGCAGTGG
TTCCCTAGACCCTGCCTTAAGTCACTCACTTATAGAAACTCCCCCTAAGTGTTTACTGCT
TAAAAGCACTTCACGTAAGGGACACGGACTATCGTAAATGCGATCGCCGAGCGCCGATTA
CCCGCTCTCCGAGAGATTTAGAGATGTTGAGTCCTCGTTGGCCAGAAAATTGTAGGATCA
GATTAGATAAGTTTTAGCGGAACCCACTTGCTCATCGCTATGATGCACGGCGGGGTCTAT
TGTGTACGCCACAGATATTATGGGGCTGACAGTATGAGAGTCAAACGGCCTACGCAGGTA
AGTTTTGACTGACGTCTTTCTGCCACGGTAAGGGGCCCCCTTTGTGGCGCATACGATTGG
TTATCTTCGGCCGATAATTGATTCCTATAATCTGTGGGAACAGGCGCGCCCCTAAGCATC
AACTTACCGCTCTTGTCTTGGCGGATTGGGGCAACTGTATGTGACCAAGTCGGGGATATA
TAGAACTCTATGCTTAAAGTGTTATGTAGTACAACCTATGCCACTCGACGAGCGCGAATA
ATGACGTGAAATCGGAAAGGTAGGGATATTATGCGTGAGTACAGTGTGCTGATTAGAGCG
GTGGCTGTAACAACCCGGAA
>Rosalind_4517
ACTATTAGCCGGAGGTCGTAGAAATACGATAAATAGGCATGTAATTGGTGGTACTCAGGT
ATTCGGGAGCGCGATTAAACAATGTGAGCAAGGTCTTACTCGTTTGCGGTATCCTACCCA
TCTGTAGCTCCCCGTTCCCGCACCTAGTAAAAGTAGCCTCAGGAACAGCCATGGGCGCGA
ATCGAGTCGGGTCGCCTTGACGTCATAGTCACATTAATCACCCATTGACTGCCGAGCTGC
CCTTCCAGCATGCGGTTGCGGGTAAAAACCACAAGCTGCAGGGATGATAGCTACCCTGGC
GATTGTCTATCATACAATCATAAGACCTTCTCGGTGCGCAGCAAAACTACAGCCAGAAGT
GAGAGTGATACAATCGGCACCGCCCGACCCATTAGTTCCCCCGGGTTCTCAGTTCAGCAT
GGTCAATGCAATGAGCGGCGGGAATAGTCTAACATATTGTTGCTGACCAGCTGTCGGTTT
CGGCGGCTGCTTGCGGACGGTGAATCGATGTCAGGGCGCATGAGCTTCGAGGGGCGGCAT
CTGTATTTGCTAGCGCGTTCAGTATCAGACCAAGTGAGTAGCTCGGGTTCTGATGCGTCC
CTTTGTCGCCTGCTTGGCGAATCTCGTAGCGCTTCCTAACACTTCGTCAGGTTGGCCGCT
CCCTCCCTAAGCAGACCCACACGGCTTTTGGGCCTGAGTGTGGTTGAGCTTATAATCTGG
TCGACCTTCATCCCCTACCAACCATAAGGCTGATTCGCAGGCGCCAAATAACAGGCCGTT
GTCGAAAAGCGTTGCAACATCGAATTCGGATACCATAATACTGCGAAGAAGAGATGCAAG
CGTATTTCGGTACGCACGAGTGATCCCAGGGACGAGAACCGAACCTATACTCCAGAAGTC
GCTGGACA
>Rosalind_2426
TCGCCGTGGCAGGAGTCATGTAACCAACGCATTCCCAGGAGGATGAAGAGTAACCGGGAG
TGGGAACGGCATGACTAGACGTTCCTCACTTAAGGATCGGAAGTCATGACAAGCTGTCTT
GTTACGCTACACGCTCTAGGCTACAGCTTCGGTCCGCCTGAAGACCTAACGCGTTTAGAA
AAAATCTTTGAGTGGCATATGCCTGTTGAGATTGTCGTCATCCCTTAATGTTAATATGAA
CGCGTTTCCGGTGCTATTGGTATATGGATAGCTCAGGTAACGTCTACAGGAATTTATAGT
CCGCAAGGTGGCATCAGCTTGCGTAATCGCCAGTGCCGCGATCACACTCTTCCGCGAGAA
TAAGCCATGCCCCTAATCTAGCAACCGTCGTGCCCACTATGCCTACTTCTGCTAGGATCA
ACCAATCGCTGCCCAGCGATTGAGTTATTCGGTCACAAGGGCTATCCGAAACGGGCAATA
ACTGTAGAACAAACAAAAGTCGGATTACGAGGAACCCCATGACCAGTACAGAGTCAACAA
TGGCGCCGTAAATCTCATTTTCTCCAACCATAAGGAATAGACGCGAATACGGCTGTGAGT
CGGGAGCTCAAATTCGAGAACCCATCGCCGCTAGTTTGACCCATCATGAGATTGTTTTAA
GTCAGAGATTGCTCGGCTACCGGTACTCTCGGAGCGAGAAACCAGTGCCATGAGCGCAAG
ATCAAATAAACGCGATGCTAACGCGAGGGTCCTGTACACTACAAAGGTGGCGTACCGAGC
GTTATCCTGGGTGGGTGAGTTCATACCTTATGTATATCCCTAACTCATTACTGTATCATT
ACGTGCCACATTATGACATTGCAACACTCGTGACTACTGCCGAGTCACCTGGCGGAGCTA
ACTCGCGTTTAGAGTAAAGTATTTTCTTAACATTGTCGAATTAGGCTGCATGTAGCATCG
GCGACCGCGCAAATAGCGGTGCCCCTAGCCCTACC
>Rosalind_7588
CGGAGAGCTTCTCCTGGCACTTCCCTGTATATTCTTAGTCATTCAGCTAGTGCTATGGTG
GCTTGACAATTCGTCGTGACGCTCATCTAAGCAGGATAGATTGTCAATTAGGGACAGATT
CGATATGTCCCCTTGGCTACCAACATCTGGTCTACTTGGCCCCTTCACCATAACACTAGC
CAACGGATGCCGTGCTGGTCTAACTTCCAGCAACTCGATATGGGGTGAGTGCTCCTCGTA
AACAGCAAGCGTAGTGCGCGTTTAAAAAAGCTCTCCCAGCTTTCTTCCCCAATCTTTGTT
GCAGCACTATCTGCGTATACCATCCGTTAGCTCAAGGTAACTTCGGCGAAGTGGAGGATA
AGCCGTGACTGGGTGTATACAGTGGGGCTTTGCAAAAGCTTACGCAAGTCCATGATTTTA
ATGTCTGAAATAGTCAAAACTTACAATGTTTCATAGGTTTCTCAATACAGGCATGCGCCA
TCCGCACAGGAATTACTCGGTATAACTGAACTTATGAACGAGTTGACTGAGTGACGTTAT
ATAAGCAGAACATTAACCATACATAACTAGGCCCTGGGTGTACGCTACCGCCCCGCTAAC
ACCACACCCTCAATCAGAATTACAATAGACTGTACGGTCGCCGACATTAGCTAAGGAGTG
TCTGAAAAGCCAGGCTCGATGATTGTTGACGGTTCATACTGTTTAATGTCTCCCTCTGAT
CGTCTGTTGGCCTTAGGTATACACGGTCGCTGGGAATACTAACATTATTCTTGAGTCTAC
AAATGGAGCCCAAAACTTTCTCCATGACGAGTCTCTAGAAGTTTCATTTCATCGAGCTAA
TCGTCGCTG '''


f = DNA.split('\n')
print(f)
for line in f:
  if line.startswitch('>'):
    ID = line[1:]
  else:

        gc = 100 * (line.count('G') + line.count('C')) / len(line)
        if gc > max_gc:
          max_gc = gc
          max_ID = ID
print(max_ID)
print(max_gc)

#13
def iprb(k, m, n):
  i = m*m+4*n*n+4*m*n-4*n-m
  j = 4 * (k + m + n) * (k + m + n -1)
  rst = 1 - float(i)/j
  return rst

if __name__ == "__main__" :
  with open("/content/rosalind_iprb (3).txt", 'r') as f:
    k, m, n = map(int, f.readline().strip().split(" "))
    print(iprb(k, m, n))

#14
s = "ACTCCAGTTACAACGTTACAACGTTACAAGTTACAAGTTACAAGTTACAATGTTACAATAGGTTACAACATCTGTTACAAAATTTATAGATGTTACAACACTGGTTACAATCGAACGTTTGAGTGTGTTACAAGCGTTACAAGTTACAAGTTACAACCTTTTGTTACAATCGGTTACAAGCGTTACAAACTAGTTACAAGTTACAATCCGTTACAAGATCGCGGTTACAATGCCGTTACAATCTTATGAGGTTACAAGCCTAGTTACAATCGCAGTTACAACTATGGCATGTTACAAGTTACAAACTACCTTAGTTACAAGGGTTACAAGCATCACGTTACAACGTTACAAAATGTTACAAGTTACAACGGCGCCAGTTACAAGCATTCGTTACAAGCCGTTGGTTACAAGTTACAAGTTACAATTGTTACAACCGTTACAAGAGTTACAATGTTACAAGTTACAATGTTACAAGATGTTACAAAAGTTACAACGCAGTTACAAGTTATGTTACAAGTTACAATCCGTTACAAGTTACAAGTTACAAGACGTTACAACCGGGCGTTACAAGTTACAAGTTCCATCCGCGTTACAACGGTTACAAAAGTTACAATTGGTTACAATAGTTACAAAGTTACAACAGAGTTACAAGTTACAAGTTACAAATTCGTTACAACAGCCATTGCGCGGTTACAAGTTACAATCTCTACGTTACAACTGTTACAACAGTTACAAGTTACAACAGGTTACAATGTTACAAAAGGTTACAATGTTACAAGTTACAAGTTACAACGTTACAATCGTTACAAGTTACAAAAACGTTACAAGGCCTACGGCTGTTACAATTTAT"
t = "GTTACAAGT"

for position in range(len(s)):
  if s[position:].startswith(t):
    print(position+1)

#15
def rev_comp(fa):
  '''
  Give transript and reversed complementary transcript
  '''
  fa_transcript = ''
  for i in range(len(fa)):
    index = -(i+1)
    if fa[index] == 'A':
      fa_transcript = fa_transcript + 'U'
    elif fa[index] == 'T':
      fa_transcript = fa_transcript + 'A'
    elif fa[index] == 'C':
      fa_transcript = fa_transcript 'G'
    else:
      fa_transcript = fa_transcript + 'C'
  fa_rc = ''
  for i in range(len(fa_transcript)):
    index = -(i+1)
    if fa_transcript[index] == 'A':
      fa_rc = fa_rc + 'U'
    elif fa_transcript[index] == 'U':
      fa_rc = fa_rc + 'A'
    elif fa_transcript[index] == 'C':
      fa_rc = fa_rc + 'G'
    else:
      fa_rc = fa_rc + 'C'
  return fa_transcript, fa_rc
def find_all(s, substring):
  '''
  this function is for find all subtrings in one string.
  It returns the index(es) of the start of all substring(s).
  '''
  index_list = []
  index = s.find(substring)
  while index != -1:
    index_list.append(index)
    index = s.find(substring, index+1)
  if len(index_list) > 0:
    return index_list
  else:
    return -1

def orf(mrna):
  start_codon = 'AUG'
  stop_codon =['UAA', 'UAG', 'UGA']
  i, j = 0.0
  out = []
  while i <= len(mrna)-2:
    if mrna[i:i+3] == start_codon:
      j=i
      sequence=''
      while i <= len(mrna) -2:
        if mrna[i:i:3] in stop_codon:
          out.append(sequence)
          break
        sequence = sequence + mrna[i:i+3]
        i = i+3
    i = j+1
    j = j+1
  return out

def translate(rnaseq):
  codon_table =
  length = len(rnaseq)
  proseq = []
  for i in range(0, length, 3):
    triplet = rnaseq[i:i:+3]
    if codon_table[str(triplet)] != 'Stop':
      proseq.append(codon_table[str(triplet)])
    else:
      break
  proseq = '', join(proseq)
  return proseq
dna = "ACACAAGGCCCGAATACTATCCCTTCGTCTTGTCTATCTGGAGTATGATCGGGTGAATACCTTCGGGAGACTGTCGAGCATTGCCCGGTGACCTTCAACGTGAGACGCGAGCCTCTATCAGCCTCTTATACTGTGACCGTCCAACTCTCACAGGTGCTGACTACGTCAACCAGTGCACTGTATCTACTGCGTCCCAGGCCCAACGATCCCTGGCTCCCCTCTTATTCAGGAGTCGTTGATAGATTGGATCGGCATGGCGGGCATCGCGGAATTACAGGTGTTTAGGCGGCTGAGGGCAATACACAGGGCCCTTGACCTTCGTAATGGTTGCGTACTCGCAGTCCTACCATTAACAATTATTAATGAGGTGATTCATACTGTGCCTAAGCTGTAAATACGCTCACTACTAATCATTCAGACACCGTTGCATCGGCTTAGGTACTGCTTAATACATCTTATGACACCATTAGGTATGAATGTGTACTGAAGTTAGCTAACTTCAGTACACATTCATACCTAATGGTGTCATCCTACATCAATTATGAGATCGGACTTCTGCGCCCGCCCGCATCGTAGAAGTTGCCGTGCCCATTACCACACCATTCGAATCTCGCAAGAACGAGCCTACTGACTTGTTGTTGCCTGCGCGGACCTGCCCGGCTTACGCTACTGTTTCTATACGAACTGCTGATCTACCATGAGTTGTCACCTTTTTCGGATCTACTTTGAATGAGTCACCCAAGATCCTCACAGTAAACCTCTTCCCAACCCTCTTAGATTCGTCCCAATCGCGTACTAGACTCGATTCCCCTAGACTTATTATTTTCTCCGGCACGGTTAGTTGCACTACCCTCGGTACCATTAGAGTTCCCGTTCAATCTGATGTGAGACCTGTGACACCTCGTGCTTAGCCAGATTCAGTCGGCTTGACCCGTTCATAAGTCAGGCCACCCGACCCATTGGGACACTGTGGCGGAACAATTATA"
mrna1, mrna2 = rev_comp(dna)
orf_list1=orf(mrna1)
orf_list2=orf(mrna2)
orf_list = orf_list1
for i in orf_list2:
  if i not in orf_list:
    orf_list.append(i)
for i in orf_list:
  print(translate(i))