# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    revComp = '' # output variable
    # your code here
    for i in Pattern:
        revComp = complement(i) + revComp
    return revComp
# HINT:   Filling in the following function is optional, but it may come in handy when solving ReverseComplement
# Input:  A character Nucleotide
# Output: The complement of Nucleotide
def complement(Nucleotide):
    comp = '' # output variable
    # your code here
    dic = {"A":"T","T":"A","G":"C","C":"G"}
    comp = dic[Nucleotide]
    return comp
# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    # your code here
    count = len(ApproximatePatternMatching(Pattern,Text,d))
    return count

# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] # initializing list of positions
    # your code here
    for i in range(len(Text) - len(Pattern) +1 ):
        if HammingDistance(Text[i:i+len(Pattern)],Pattern) <= d:
            positions.append(i)
    return positions

# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
def HammingDistance(p, q):
    # your code here
    count = 0
    for i in range(len(p)):
        if p[i]!=q[i]:
            count = count + 1
    return count
# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable
    # your code here
    skew = Skew(Genome)
    count = min(skew.values())
    for i in range(len(skew)):
        if count == skew[i]:
            positions.append(i)
    return positions

# Input:  A String Genome
# Output: Skew(Genome)
def Skew(Genome):
    skew = {} #initializing the dictionary
    # your code here
    skew[0] = 0
    for i in range(len(Genome)):
        skew[i+1] = skew[i]
        if Genome[i] == 'G':
            skew[i+1] = skew[i]+1
        if Genome[i] == 'C':
            skew[i+1] = skew[i]-1
    return skew

# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    FrequentPatterns = [] # output variable
    # your code here
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
        FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates

# Input: A List Items
# Output: A List not have any repetition
def remove_duplicates(Items):
    ItemsNoDuplicates = [] # output variable
    # your code here
    for i in Items:
        if ItemsNoDuplicates.count(i) < 1:
            ItemsNoDuplicates.append(i)
    return ItemsNoDuplicates

# Input:  A string Text and an integer k
# Output: CountDict(Text, k)
# HINT:   This code should be identical to when you last implemented CountDict
def CountDict(Text, k):
    Count = {} # output variable
    # your code here
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

# Input:  Strings Pattern and Text
# Output: The number of times Pattern appears in Text
# HINT:   This code should be identical to when you last implemented PatternCount
def PatternCount(Pattern, Text):
    count = 0 # output variable
    # your code here
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

# Input:  Two strings, Pattern and Genome
# Output: A list containing all starting positions where Pattern appears as a substring of Genome
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    # your code here
    for i in range(len(Genome)-len(Pattern)+1):
        if Pattern == Genome[i:i+len(Pattern)]:
            positions.append(i)
    return positions


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
#lines = sys.stdin.read().splitlines()
print(Score(["AACGTA","CCCGTT","CACCTT","GGATTA","TTCCGG"]))