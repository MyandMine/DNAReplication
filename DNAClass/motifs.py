# Input: A dictionary Probabilities, where keys are k-mers and values are the probabilities of these k-mers (which do not necessarily sum up to 1)
# Output: A normalized dictionary where the probability of each k-mer was divided by the sum of all k-mers' probabilities
def Normalize(Probabilities):
    # your code here
    count = 0
    for i in Probabilities.keys():
        count = count + Probabilities[i]
    for i in Probabilities.keys():
        Probabilities[i] = Probabilities[i]/count
    return Probabilities
# Input:  Positive integers k and t, followed by a list of strings Dna
# Output: RandomizedMotifSearch(Dna, k, t)
def RandomizedMotifSearch(Dna, k, t):
    # insert your code here
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs 
# Input:  A list of strings Dna, and integers k and t
# Output: RandomMotifs(Dna, k, t)
# HINT:   You might not actually need to use t since t = len(Dna), but you may find it convenient
def RandomMotifs(Dna, k, t):
    # place your code here.
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
        DnaLen = len(Dna[0])
    motifs = []
    RandomStart = random.randint(0,DnaLen-k)
    motifs.append(Dna[random.randint(0,t-1)][RandomStart:RandomStart+k])
    for j in range(t):
        Profile = ProfileWithPseudocounts(motifs[0:j+1])
        motifs.append(ProfileMostProbablePattern(Dna[j], k, Profile))
    motifs.remove(motifs[0])
    if Score(motifs) < Score(BestMotifs):
        BestMotifs = motifs
    return BestMotifs

def Score2(Profile):
    score = 0;
    for i in range(len(Profile)):
            score = score + Profile[i] * math.log2(Profile[i])
    return score
# Input:  A profile matrix Profile and a list of strings Dna
# Output: Motifs(Profile, Dna)
def Motifs(Profile, Dna):
    # insert your code here
    motifs = [];
    for i in range(len(Dna)):
        motifs.append(ProfileMostProbablePattern(Dna[i], len(Profile["A"]), Profile))
    return motifs

# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = [] # output variable
    # your code here
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
        n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

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

# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearch(Dna, k, t):
    # type your GreedyMotifSearch code here.
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
        n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

# Input:  String Text, an integer k, and profile matrix Profile
# Output: ProfileMostProbablePattern(Text, k, Profile)
def ProfileMostProbablePattern(Text, k, Profile):
    # insert your code here. Make sure to use Pr(Text, Profile) as a subroutine!
    score = -1;
    profileMost = ""
    a = len(Text)
    for i in range(a-k+1):
        if score < Pr(Text[i:i+k],Profile):
            score = Pr(Text[i:i+k],Profile)
            profileMost = Text[i:i+k]
    return profileMost
# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    # insert your code here
    pr = 1
    for i in range(len(Text)):
        pr = pr * Profile[Text[i]][i]
    return pr

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
# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    # insert your code here
    profile = Count(Motifs)
    for i in range(k):
        for j in "ACGT":
            profile[j][i] = profile[j][i] / t
    return profile

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

import math
import random

Text = ["TTACCTTAAC","GATGTCTGTC","ACGGCGTTAG","CCCTAACGAG","CGTCAGAGGT"]
A = [0.8, 0.0, 0.0, 0.2]
C = [0.0, 0.6, 0.2, 0.0]
G = [0.2, 0.2, 0.8, 0.0]
T = [0.0, 0.2, 0.0, 0.8]
#Profile = {'A':A, 'C':C, 'G':G, 'T':T}
Dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
    "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
    "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
    "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
    "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
print(RandomizedMotifSearch(Dna,8,5))