
def merge_overlap(left, right, left_qual, right_qual, mode='left', match = 1, mismatch=-1, gap=-1):
    # mode -> 'left', 'right', 'iupac'

    consensus = ""

    l, r = build_alignment(left, right, match, mismatch, gap)
    
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