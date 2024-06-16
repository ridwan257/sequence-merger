from generate_alignment import build_alignment
from utils import clear, to_iupac


def merge_overlap(left, right, left_qual, right_qual, mode='left'):
    # mode -> 'left', 'right', 'iupac'

    consensus = ""

    l, r = build_alignment(left, right)
    
    flank_r_len = len(r) - len(l)
    flank_l_len = 0
    for ch in r:
        if ch != '-':
            break
        flank_l_len += 1

    print(l)
    print(r)
    # print(flank_r_len)
    # print(flank_l_len)

    consensus += l[:flank_l_len]

    l_index = flank_l_len
    r_index = 0

    for i in range(flank_l_len, len(l)):
        # print(f'{l[i]}[{l_index}] -> {left_qual[l_index]}')
        # print(f'{r[i]}[{r_index}] -> {right_qual[r_index]}')
        # print()

        if  l[i] == r[i] : 
            consensus += l[i]
            l_index += 1
            r_index += 1

        elif l[i] == '-' : consensus += r[i]; r_index += 1
        elif r[i] == '-' : consensus += l[i]; l_index += 1

        else:
            if   left_qual[l_index] > right_qual[r_index] :  consensus += l[i]
            elif left_qual[l_index] < right_qual[r_index] :  consensus += r[i]
            else:
                if mode == 'left' : consensus += l[i]
                elif mode == 'right' : consensus += r[i]
                elif mode == 'iupac' : consensus += to_iupac(l[i], r[i])

            l_index += 1
            r_index += 1

    consensus += r[len(l):]
    
    return consensus

def simple_merge(left, right, mode='left'):
    lqual = [ 1 for i in range(len(left)) ]
    rqual = [ 1 for i in range(len(right)) ]
    consensus = merge_overlap(left, right, lqual, rqual, mode)

    return consensus


if __name__ == "__main__":
    clear()

    left = "AGCTAG"
    right = "AATACCTA"

    left_qual = [5, 5, 6, 7, 8, 9, 1]
    right_qual = [2, 3, 9, 5, 6, 5]

    origin = simple_merge(left, right, 'iupac')

    print()
    print(origin)
