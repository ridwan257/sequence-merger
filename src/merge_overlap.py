from dataclasses import dataclass, field
from generate_alignment import build_alignment
from traceback_paths import path_to_alignment
from utils import clear, to_iupac
from random import randint
from math import inf

@dataclass
class Consensus:
    name : str = field( default_factory=lambda : "Seq" + str(randint(100, 99_999)) )
    seq : str = ""
    left_seq_len : int = 0
    right_seq_len : int = 0
    length : int = 0
    score : int = inf
    overlap_length : int = 0
    quality : list = field(default_factory=list)
    gap_ratio : float = 0.0
    error_rate : float = 0.0
    precision : float = 0.0

    def summary(self, retrive=False, mode='compact'):
        summary_string = '@ ' + self.name + '\n'

        if self.length > 30:
            summary_string += self.seq[:15] + ' ... ' + self.seq[-15:] + '\n'
            first = [str(n) for n in self.quality[:15]]
            last = [str(n) for n in self.quality[-15:]]
            summary_string += " ".join(first) + '...' + " ".join(last) + '\n'

        else:
            summary_string += self.seq + '\n'
            qual = [str(n) for n in self.quality]
            summary_string += " ".join(qual) + '\n'

        summary_string += 'Left seq length : ' + str(self.left_seq_len) + '\n'
        summary_string += 'Right seq length : ' + str(self.right_seq_len) + '\n'
        summary_string += 'Length : ' + str(self.length) + '\n'
        summary_string += 'Alignment Score : ' + str(self.score) + '\n'
        summary_string += 'Overlap length : ' + str(self.overlap_length) + '\n'
        summary_string += 'Overlap Precision : ' + str(self.precision) + '\n'
        summary_string += 'Gap Ratio : ' + str(self.gap_ratio) + '\n'
        summary_string += 'Error Rate : ' + str(self.error_rate) + '\n'

        print(summary_string)

        if retrive:
            return summary_string


def build_consensus_from_alignment( left_align, right_align, 
        left_qual=None, right_qual=None, 
        mode='left', name = '',
        aln_score=None, verbose=False
    ):

    if left_qual is None:
        left_qual = [1 for ch in left_align if ch!='-']
    if right_qual is None:
        right_qual = [1 for ch in right_align if ch!='-']

   
    ## Variable Declaretion 
    consensus = ""
    consensus_quality = []
    left_length = len(left_qual)
    right_length = len(right_qual)
    mismatch_count = 0
    left_gap_count = 0
    right_gap_count = 0
    fragment_length = 0
    

    ## -----------------------------
    flank_r_len = len(right_align) - len(left_align)
    flank_l_len = 0
    for ch in right_align:
        if ch != '-':
            break
        flank_l_len += 1

    fragment_length = len(left_align) - flank_l_len
    # print(left_align)
    # print(right_align)
    # print(flank_r_len)
    # print(flank_l_len)

    consensus += left_align[:flank_l_len]
    consensus_quality.extend(left_qual[:flank_l_len])

    l_index = flank_l_len
    r_index = 0

    for i in range(flank_l_len, len(left_align)):
        # print(f'{l[i]}[{l_index}] -> {left_qual[l_index]}')
        # print(f'{r[i]}[{r_index}] -> {right_qual[r_index]}')
        # print()

        # if both nucleotides are same
        if  left_align[i] == right_align[i] : 
            consensus += left_align[i]
 
            qscore = 0
            if left_qual[l_index] >= right_qual[r_index]:
                qscore = left_qual[l_index]
            else :
                qscore = right_qual[r_index]
            consensus_quality.append(qscore)

            l_index += 1
            r_index += 1

        # if there is gap in left sequence
        elif left_align[i] == '-' : 
            consensus += right_align[i]
            consensus_quality.append(right_qual[r_index])
            left_gap_count += 1
            r_index += 1

        # if there is gap in right sequence
        elif right_align[i] == '-' : 
            consensus += left_align[i]
            consensus_quality.append(left_qual[l_index])
            right_gap_count += 1
            l_index += 1

        # if both nucleotides are different
        else:
            # if left nucleotide quality high
            if   left_qual[l_index] > right_qual[r_index] :  
                consensus += left_align[i]
                consensus_quality.append(left_qual[l_index])

            # if right nucleotide quality high
            elif left_qual[l_index] < right_qual[r_index] :  
                consensus += right_align[i]
                consensus_quality.append(right_qual[r_index])

            # if both nucleotides quality same  
            else:
                if mode == 'left' : consensus += left_align[i]
                elif mode == 'right' : consensus += right_align[i]
                elif mode == 'iupac' : consensus += to_iupac(left_align[i], right_align[i])

                consensus_quality.append(left_qual[l_index])

            mismatch_count += 1
            l_index += 1
            r_index += 1

    consensus += right_align[len(left_align):]
    consensus_quality.extend(right_qual[r_index:])

    consensus_obj = Consensus(
        seq = consensus,
        quality = consensus_quality,
        length = len(consensus),
        left_seq_len = len(left_qual),
        right_seq_len = len(right_qual),
        overlap_length = fragment_length
    )

    if name: consensus_obj.name = name
    if aln_score is not None : consensus_obj.score = aln_score

    total_gap = left_gap_count + right_gap_count
    consensus_obj.error_rate = (left_gap_count + right_gap_count + mismatch_count) / fragment_length
    consensus_obj.gap_ratio = total_gap / ( 2*fragment_length - total_gap )
    consensus_obj.precision = 1 - max(left_gap_count, right_gap_count) / fragment_length

    if verbose:
        print(consensus)
        print('Overlap length :', fragment_length)
        print('Overlap Precision :', consensus_obj.precision)
        print('Gap Ratio :', consensus_obj.gap_ratio)
        print('Error Rate :', consensus_obj.error_rate)

    return consensus_obj

    

def merge_overlap(left, right, left_qual=None, right_qual=None, name='', mode='left', match = 1, mismatch=-1, gap=-1, verbose=False):
    # mode -> 'left', 'right', 'iupac'

    l, r, s = build_alignment(left, right, match=match, mismatch=mismatch, gap=gap, verbose=verbose)

    print(s)
    consensus = build_consensus_from_alignment(
            l, r, 
            left_qual = left_qual, 
            right_qual = right_qual, 
            mode = mode, 
            name = name,
            aln_score = s,
            verbose=verbose
        )

    return consensus


if __name__ == "__main__":
    left = "AGCTAG"
    right = "AATACCTA"

    left_qual = [5, 5, 6, 7, 8, 9, 1]
    right_qual = [2, 3, 9, 5, 6, 5]

    origin = merge_overlap(left, right, mode='iupac')

    print()
    origin.summary()
