import random
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
# Input:  A dictionary Probabilities whose keys are k-mers and whose values are the probabilities of these kmers
# Output: A randomly chosen k-mer with respect to the values in Probabilities
def WeightedDie(Probabilities):
    kmer = '' # output variable
    # your code here
    Probabilities = Normalize(Probabilities)
    Rnum = random.uniform(0,1)
    for i in Probabilities.keys():
        Rnum = Rnum - Probabilities[i]
        if Rnum < 0:
            kmer = i
            return kmer
print(WeightedDie({'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}))