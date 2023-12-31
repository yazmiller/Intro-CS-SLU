# -*- coding: utf-8 -*-
"""lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_u-ip5Q0o5pdKb_PN1rWETL-aCcg4whH

(5 points) Assume that we have 5 DNA motifs that have the following strings:

TTCAT
AATCATGA
CCCG
GGCATT
CACGT

which are comprised of four nucleotides (e.g. A, T, C, G). We would like to define a variable called 'DNA_motifs', and store these sequences in this variable using the data type list. Then we need to print the variable by print("DNA_motifs: ", DNA_motifs)
Please write your python codes for this activity.
"""

DNA_motifs = ['TTCAT', 'AATCATGA', 'CCCG', 'GGCATT', 'CACGT']
print("DNA_motifs:", DNA_motifs)

"""(10 points) Based on the defined list 'DNA_motifs', please write your python codes for the following activities:

What is the first element of the list 'DNA_motifs'?
What is the last element of the list 'DNA_motifs'?
What is the 3rd element of the list 'DNA_motifs'?
What are the first 3 elements of the list 'DNA_motifs'?
What are the last 2 elements of the list 'DNA_motifs'?
Given the list 'DNA_motifs', how to concatenate the first 2 elements and the last element together into a string?
"""

DNA_motifs = ['TTCAT', 'AATCATGA', 'CCCG', 'GGCATT', 'CACGT']
print(DNA_motifs[0])
print(DNA_motifs[-1])
print(DNA_motifs[2])
print(DNA_motifs[0:3])
print(DNA_motifs[-2:])
print(DNA_motifs[0] + DNA_motifs[1] + DNA_motifs[-1])

"""(5 points) Based on the defined list 'DNA_motifs', we need to calculate the length of each motif in this list. We need to use the 'for' loop to access each motif in the list and calculate/print the length. The expected outputs should be similar as follows:

Length of TTCAT is 5
Length of AATCATGA is 8
Length of CCCG is 4
Length of GGCATT is 6
Length of CACGT is 5

"""

for motif in DNA_motifs:
  print("Length of %s is %i" % (motif, len(motif)))

"""(10 points) Based on the defined list 'DNA_motifs', we need to use the 'for' loop to access each motif in the list and find the longest motif in this list. The expected output is 'The longest motif is AATCATGA with length 8'
Please write your python codes for this activity.
"""

DNA_motifs = ['TTCAT', 'AATCATGA', 'CCCG', 'GGCATT', 'CACGT']
longest_motif=''
for motif in DNA_motifs:
  if ((len(motif)) > (len(longest_motif))):
    longest_motif = motif
  print("The longest motif is %s with length %i" %(longest_motif, len(longest_motif)))

"""(5 points) Now let's practice more advanced programming using a list and dictionary. Based on the list 'DNA_motifs', let's define a dictionary 'DNA_motifs_length', where the key is each motif in the list 'DNA_motifs', and the value is its length. You need to use 'for' statement to loop through the list 'DNA_motifs' to store key:value into the dictionary.
Please write your python codes for this activity.
"""

DNA_motifs = ['TTCAT', 'AATCATGA', 'CCCG', 'GGCATT', 'CACGT']
DNA_motifs_length = {}
for motif in DNA_motifs:
  DNA_motifs_length[motif] = len(motif)

print(DNA_motifs_length)
for key, val in DNA_motifs_length.items():
  print(key, val)

"""(10 points) Given the defined dictionary 'DNA_motifs_length', please write your python codes for the following activities.

Add a new motif 'AAT' as a key into the dictionary, and assign its length as a value
Print out all the keys in the dictionary
Print out all the values in the dictionary
Print out all the items in the dictionary
Check whether the key 'CCT' already exists in a dictionary
"""

DNA_motifs_length['???'] = len('???')
print('Keys:', DNA_motifs_length.keys())
print('Values:',
DNA_motifs_length.items())
if '???' in DNA_motifs_length:
  print("??? already exists!")
else:
  print("??? does not exist!")

"""(5 points) Based on the defined list 'DNA_motifs', we are interested in the motifs that contain substring 'CAT', please write your python codes to print out these motifs. (hint: combine while/for loop with if conditions)."""

DNA_motifs = ['TTCAT', 'AATCATGA', 'CCCG', 'GGCATT', 'CACGT']
for motif in DNA_motifs:
  if 'CAT' in motif:
    print('CAT exists!')
  else:
    print('CAT does not exist!')

"""(5 points) Based on the defined list 'DNA_motifs', we are also interested in the motifs that have a length larger than 5, please write your python codes to print out these motifs. (hint: use while/for loop and if conditions)."""

DNA_motifs = ['TTCAT', 'AATCATGA', 'CCCG', 'GGCATT', 'CACGT']
for motif in DNA_motifs:
  if len(motif) > 5:
    print(motif, 'is longer than 5.')
  else:
    print(motif, 'is not longer than 5.')

"""(5 points) Based on the defined list 'DNA_motifs', we would like to replace the letter 'T' with 'U' for every motif and append them to a new list called 'RNA_motifs'.
Please write your python codes for this activity (hint: use for loop, string.replace() and list.append() function).
"""

DNA_motifs = ['TTCAT', 'AATCATGA', 'CCCG', 'GGCATT', 'CACGT']
RNA_motifs = []
for motifs in DNA_motifs:
  x = motif.replace('T', 'U')
  RNA_motifs.append(x)
print(RNA_motifs)

"""(5 points) Based on the defined list 'DNA_motifs', we are also interested in the motifs that have a length larger than 5. After we find the motifs, we need to concatenate them as a new string and add it as a new key into the dictionary 'DNA_motifs_length', where the value is the new sequence's length. Please write your python codes for this activity. (hint: use while/for loop and if conditions)."""

DNA_motifs = ['TTCAT', 'AATCATGA', 'CCCG', 'GGCATT', 'CACGT']
really_long_motif= []
for motif in DNA_motifs:
  if len(motif) > 5:
    really_long_motif.append(motif)

print(really_long_motif[0] + really_long_motif[1])

really_long_motif_final = (really_long_motif[0] + really_long_motif[1])
DNA_motifs_length[really_long_motif_final] = len(really_long_motif_final)
print(DNA_motifs_length)

""" Given the sequence, ATCCGAATACGGTTCGGGTA, and the following two motifs found in this sequence: motif 'CGAA' (motif1) and its reverse complement 'TTCG' (motif2),  write your python codes to get the mutated DNA that results from removing the two motifs, and then zero or more characters that might be found between them."""

sequence = 'ATCCGAATACGGTTCGGGTA'
motif1 = 'CGAA'
motif2 = 'TTCG'
new_sequence = sequence.replace('CGAA', '')
new_sequence2 = new_sequence.replace('TTCG', '')
new_sequence3 = new_sequence2.replace('TACGG', '')
print(new_sequence3)