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

Text = "AGCAGCTTTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATCTGAACTGGTTACCTGCCGTGAGTAAAT"
A = [0.7, 0.2, 0.1, 0.5, 0.4, 0.3, 0.2, 0.1]
C = [0.2, 0.2, 0.5, 0.4, 0.2, 0.3, 0.1, 0.6]
G = [0.1, 0.3, 0.2, 0.1, 0.2, 0.1, 0.4, 0.2]
T = [0.0, 0.3, 0.2, 0.0, 0.2, 0.3, 0.3, 0.1]
Profile = {'A':A, 'C':C, 'G':G, 'T':T}
print(ProfileMostProbablePattern(Text, 8, Profile))