# Input:  A list of strings Dna, and integers k and t
# Output: RandomMotifs(Dna, k, t)
# HINT:   You might not actually need to use t since t = len(Dna), but you may find it convenient
def RandomMotifs(Dna, k, t):
    # place your code here.
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
        DnaLen = len(Dna[0])
    for i in range(DnaLen-k+1):
        motifs = []
        RandomStart = random.randint(0,DnaLen-k)
        motifs.append(Dna[random.randint(0,t-1)][RandomStart:RandomStart+k])
        for j in range(t):
            Profile = ProfileWithPseudocounts(motifs[0:j+1])
            if 3 != len(Profile["A"]):
                print("sfd")
            motifs.append(ProfileMostProbablePattern(Dna[j], k, Profile))
        motifs.remove(motifs[0])
        if Score(motifs) < Score(BestMotifs):
            BestMotifs = motifs
    return BestMotifs
# Input:  A profile matrix Profile and a list of strings Dna
# Output: Motifs(Profile, Dna)
def Motifs(Profile, Dna):
    # insert your code here
    motifs = [];
    for i in range(len(Dna)):
        motifs.append(ProfileMostProbablePattern(Dna[i], len(Profile["A"]), Profile))
    return motifs
# Insert your ProfileMostProbablePattern(Text, k, Profile) and Pr(Pattern, Profile) functions here.
# Input:  String Text, an integer k, and profile matrix Profile
# Output: ProfileMostProbablePattern(Text, k, Profile)
def ProfileMostProbablePattern(Text, k, Profile):
    # insert your code here. Make sure to use Pr(Text, Profile) as a subroutine!
    score = -1;
    profileMost = ""
    a = len(Text)
    for i in range(a-k+1):
        if len(Text[i:i+k]) != len(Profile["A"]):
            print("sfd")
        if score < Pr(Text[i:i+k],Profile):
            score = Pr(Text[i:i+k],Profile)
            profileMost = Text[i:i+k]
    return profileMost
# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    # insert your code here
    if len(Text) != len(Profile["A"]):
        print("sfd")
    pr = 1
    for i in range(len(Text)):
        pr = pr * Profile[Text[i]][i]
    return pr
# Input:  A set of kmers Motifs
# Output: ProfileWithPseudocounts(Motifs)
def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {} # output variable
    # your code here
    profile = CountWithPseudocounts(Motifs)
    for i in range(k):
        for j in "ACGT":
            profile[j][i] = profile[j][i] / (t + 4)
    return profile
# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    # insert your code here
    count = Count(Motifs)
    for i in "ACGT":
        for j in range(len(count["A"])):
            count[i][j] = count[i][j]+1
    return count
# Input:  A set of kmers Motifs
# Output: Count(Motifs)
def Count(Motifs):
    count = {} # initializing the count dictionary
    # your code here
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count
# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    # Insert code here
    k = len(Motifs[0])
    t = len(Motifs)
    consensus = Consensus(Motifs)
    score = 0
    for i in range(t):
        for j in range(k):
            if consensus[j] != Motifs[i][j]:
                score = score + 1
    return score
# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
    # insert your code here
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus
### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
import random

Text = ["TTACCTTAAC","GATGTCTGTC","ACGGCGTTAG","CCCTAACGAG","CGTCAGAGGT"]
A = [0.8, 0.0, 0.0, 0.2]
C = [0.0, 0.6, 0.2, 0.0]
G = [0.2, 0.2, 0.8, 0.0]
T = [0.0, 0.2, 0.0, 0.8]
Profile = {'A':A, 'C':C, 'G':G, 'T':T}
Dna = ["TTACCTTAAC",
    "GATGTCTGTC",
    "ACGGCGTTAG",
    "CCCTAACGAG",
    "CGTCAGAGGT"]
print(GreedyMotifSearch(Dna,3,5))