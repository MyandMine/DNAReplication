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
### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
Text = ["TTACCTTAAC","GATGTCTGTC","ACGGCGTTAG","CCCTAACGAG","CGTCAGAGGT"]
A = [0.8, 0.0, 0.0, 0.2]
C = [0.0, 0.6, 0.2, 0.0]
G = [0.2, 0.2, 0.8, 0.0]
T = [0.0, 0.2, 0.0, 0.8]
Profile = {'A':A, 'C':C, 'G':G, 'T':T}
print(Motifs(Profile,Text))