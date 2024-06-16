import utils as utl
import build_matrix as bld
import traceback as trc

def build_alignment(left, right):
    score_mat, trace_mat = bld.build_alignment_matrix(left, right)

    # utl.render(score_mat)

    score, li, ri = bld.get_maximum_score_index(score_mat)

    print("index left | total match right :", li, ri)

    path_list = []
    trc.trace_all_paths(trace_mat, li, ri, "", path_list, 1)
    # print(path_list)

    la, ra = trc.path_to_alignment(left, right, li, ri, path_list[0])

    return la, ra


if __name__ == "__main__":
    print("\033c", end='')

    left = "AGCTTCG"
    right = "CTCGAT"

    l, r = build_alignment(left, right)
    print(l)
    print(r)






















