import sys
sys.path.append('/Users/reuben204/Reuben/practice/sequence-merger/src/')

from Bio import SeqIO
import merge_overlap as merge
import traceback_paths as trace
import build_matrix as build
import utils as utl

s1 = 'CTAAGGGATTCCGGTAATTAGACAG'
s2 = 'ATAGACCATATGTCAGTGACTGTGTAA'

merge.merge_overlap(s1, s2, match=1, mismatch=-2, gap=-2, verbose=True)

##score_mat, trace_mat = build.build_alignment_matrix(s1, s2)
##
##utl.render(score_mat)
##
##build.semi_global_alignment_matrix(s1, s2)

##l = 'CTGACG--AC'
##r = '---A-GCTAGCTA'
####    C  T  G  A  C  G  C  T  A  C  C  T  A
##lq = [2, 3, 4, 1, 4, 3,       2, 5]
##rq = [         3,    1, 3, 1, 4, 5, 7, 8, 9]
##cns = merge.build_consensus_from_alignment(l, r, lq, rq, mode='iupac')
##
##cns.
