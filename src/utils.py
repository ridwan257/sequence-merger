from Bio.Seq import Seq

def render(mattix):
    for row in mattix : print(row)

def clear():
    print("\033c", end='')

def to_iupac(*nts):
    iupac_codes = {
        frozenset(['A']): 'A',
        frozenset(['C']): 'C',
        frozenset(['G']): 'G',
        frozenset(['T']): 'T',
        frozenset(['A', 'G']): 'R',
        frozenset(['C', 'T']): 'Y',
        frozenset(['C', 'G']): 'S',
        frozenset(['A', 'T']): 'W',
        frozenset(['G', 'T']): 'K',
        frozenset(['A', 'C']): 'M',
        frozenset(['A', 'C', 'G']): 'V',
        frozenset(['A', 'C', 'T']): 'H',
        frozenset(['A', 'G', 'T']): 'D',
        frozenset(['C', 'G', 'T']): 'B',
        frozenset(['A', 'C', 'G', 'T']): 'N'
    }
    nts = frozenset(sorted(nts))

    return iupac_codes.get(nts)



def reverse_complement(sequence):
    seq = Seq(sequence)    
    reverse_comp = seq.reverse_complement()
    
    return str(reverse_comp)
