import re

x = input("Paste the DNA coding template here(capital letters, free of any '-' or numbers): ")
# for example TACATGAAATACGGGATT
r = re.split(r'\W*', x)

codons = []
def flip_it(r):
    for i in r:
        if i == 'A':
            codons.append('U')
        if i == 'T':
            codons.append('A')
        if i == 'G':
            codons.append('C')
        if i == 'C':
            codons.append('G')
flip_it(r)

# the flip_it 

for i in codons:
    i = codons[0:3]
    if i == ['A', 'U', 'G']:
        print("Met")
    if i == ['U', 'U', 'U']:
        print("Phe")
    if i == ['U', 'U', 'C']:
        print("Phe")
    if i == ['U', 'U', 'A']:
        print("Leu")
    if i == ['U', 'U', 'G']:
        print("Leu")
    if i == ['C', 'U', 'U']:
        print("Leu")
    if i == ['C', 'U', 'C']:
        print("Leu")
    if i == ['C', 'U', 'A']:
        print("Leu")
    if i == ['C', 'U', 'G']:
        print("Leu")
    if i == ['A', 'U', 'U']:
        print("Ilu")
    if i == ['A', 'U', 'C']:
        print("Ilu")
    if i == ['A', 'U', 'A']:
        print("Ilu")
    if i == ['G', 'U', 'U']:
        print("Val")
    if i == ['G', 'U', 'C']:
        print("Val")
    if i == ['G', 'U', 'A']:
        print("Val")
    if i == ['G', 'U', 'G']:
        print("Val")
    if i == ['U', 'C', 'U']:
        print("Ser")
    if i == ['U', 'C', 'C']:
        print("Ser")
    if i == ['U', 'C', 'A']:
        print("Ser")
    if i == ['U', 'C', 'G']:
        print("Ser")
    if i == ['C', 'C', 'U']:
        print("Pro")
    if i == ['C', 'C', 'C']:
        print("Pro")
    if i == ['C', 'C', 'A']:
        print("Pro")
    if i == ['C', 'C', 'G']:
        print("Pro")
    if i == ['A', 'C', 'U']:
        print("Thr")
    if i == ['A', 'C', 'C']:
        print("Thr")
    if i == ['A', 'C', 'A']:
        print("Thr")
    if i == ['A', 'C', 'G']:
        print("Thr")
    if i == ['G', 'C', 'U']:
        print("Ala")
    if i == ['G', 'C', 'C']:
        print("Ala")
    if i == ['G', 'C', 'A']:
        print("Ala")
    if i == ['G', 'C', 'G']:
        print("Ala")
    if i == ['U', 'A', 'U']:
        print("Tyr")
    if i == ['U', 'A', 'C']:
        print("Tyr")
    if i == ['U', 'A', 'A']:
        print("Stop")
    if i == ['U', 'A', 'G']:
        print("Stop")
    if i == ['C', 'A', 'U']:
        print("His")
    if i == ['C', 'A', 'C']:
        print("His")
    if i == ['C', 'A', 'A']:
        print("Gln")
    if i == ['C', 'A', 'G']:
        print("Gln")
    if i == ['A', 'A', 'U']:
        print("Asn")
    if i == ['A', 'A', 'C']:
        print("Asn")
    if i == ['A', 'A', 'A']:
        print("Lys")
    if i == ['A', 'A', 'G']:
        print("Lys")
    if i == ['G', 'A', 'U']:
        print("Asp")
    if i == ['G', 'A', 'C']:
        print("Asp")
    if i == ['G', 'A', 'A']:
        print("Glu")
    if i == ['G', 'A', 'G']:
        print("Glu")
    if i == ['U', 'G', 'U']:
        print("Cys")
    if i == ['U', 'G', 'C']:
        print("Cys")
    if i == ['U', 'G', 'A']:
        print("Stop")
    if i == ['U', 'G', 'G']:
        print("Trp")
    if i == ['C', 'G', 'U']:
        print("Arg")
    if i == ['C', 'G', 'C']:
        print("Arg")
    if i == ['C', 'G', 'A']:
        print("Arg")
    if i == ['C', 'G', 'G']:
        print("Arg")
    if i == ['A', 'G', 'U']:
        print("Ser")
    if i == ['A', 'G', 'C']:
        print("Ser")
    if i == ['A', 'G', 'A']:
        print("Arg")
    if i == ['A', 'G', 'G']:
        print("Arg")
    if i == ['G', 'G', 'U']:
        print("Gly")
    if i == ['G', 'G', 'C']:
        print("Gly")
    if i == ['G', 'G', 'A']:
        print("Gly")
    if i == ['G', 'G', 'G']:
        print("Gly")
    codons.pop(0)
    codons.pop(0)
    codons.pop(0)
# the 3 codons.pop() lines progress the reading frame by 3 nucleotide increments
