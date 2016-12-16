# Copy your SymbolArray function (along with all required subroutines) below this line.
# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol)
def SymbolArray(Genome, symbol):
    array = {}
    # type your code here
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array

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

# We will be reading the E. coli genome, and we will store it as a variable called e_coli.
import sys                            # needed to read the genome

e_coli = "AAAAGGGG"
# Print the result of calling SymbolArray, passing in e_coli for Genome and "C" for symbol
print(SymbolArray(e_coli,"A"))