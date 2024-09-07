import utils as utl
import build_matrix as bld
import traceback_paths as trc

def build_alignment(left, right, match=1, mismatch=-1, gap=-1, verbose=False):
    if not isinstance(left, str) : left = str(left)
    if not isinstance(right, str) : right = str(right)

    score_mat, trace_mat = bld.build_alignment_matrix(left, right, match, mismatch, gap)

    score, li, ri = bld.get_maximum_score_index(score_mat, verbose=verbose)

    path_list = []
    trc.trace_all_paths(trace_mat, li, ri, "", path_list, 1)

    la, ra = trc.path_to_alignment(left, right, li, ri, path_list[0])

    if verbose:
        print(la)
        print(ra)

    return la, ra, score


if __name__ == "__main__":
    print("\033c", end='')

    left = "AGCTTCG"
    right = "CTCGAT"

    l, r = build_alignment(left, right)
    print(l)
    print(r)
    






















