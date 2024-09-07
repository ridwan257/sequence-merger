from Bio.Seq import Seq

def render(mattix):
    for row in mattix :
        for num in row:
            print(f"{num:3}", end=" ")
        print()

def clear():
    print("\033c", end='')


IUPAC_TO_NT = {
    'A': {'A'}, 
    'T': {'T'}, 
    'C': {'C'}, 
    'G': {'G'},
    'R': {'A', 'G'}, 
    'Y': {'C', 'T'}, 
    'S': {'G', 'C'}, 
    'W': {'A', 'T'},
    'K': {'G', 'T'}, 
    'M': {'A', 'C'}, 
    'B': {'C', 'G', 'T'}, 
    'D': {'A', 'G', 'T'},
    'H': {'A', 'C', 'T'}, 
    'V': {'A', 'C', 'G'}, 
    'N': {'A', 'C', 'G', 'T'}
}

NT_TO_IUPAC = { frozenset(v): k for k, v in IUPAC_TO_NT.items() }

def to_iupac(nt1, nt2):
    bases1 = IUPAC_TO_NT.get(nt1, set())
    bases2 = IUPAC_TO_NT.get(nt2, set())
    
    combined_bases = bases1.union(bases2)
    
    return NT_TO_IUPAC.get(frozenset(combined_bases), None)




def reverse_complement(sequence):
    seq = Seq(sequence)    
    reverse_comp = seq.reverse_complement()
    
    return str(reverse_comp)



if __name__ == '__main__':
    print(to_iupac('B', 'D'))
    print(to_iupac('A', 'C'))
    print(to_iupac('W', 'W'))











