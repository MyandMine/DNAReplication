# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    revComp = '' # output variable
    # your code here
    for i in Pattern:
        revComp = complement(i) + revComp
    return revComp


# Copy your reverse function from the previous step here.


# HINT:   Filling in the following function is optional, but it may come in handy when solving ReverseComplement
# Input:  A character Nucleotide
# Output: The complement of Nucleotide
def complement(Nucleotide):
    comp = '' # output variable
    # your code here
    dic = {"A":"T","T":"A","G":"C","C":"G"}
    comp = dic[Nucleotide]
    return comp



### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
print(ReverseComplement("AAAACCCGGT"))