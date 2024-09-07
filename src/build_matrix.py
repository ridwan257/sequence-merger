import utils as utl



def last_column(matrix):
    last_index = len(matrix[0]) - 1
    last_col = [0]*(len(matrix))

    for i in range(len(matrix)):
        last_col[i] = matrix[i][last_index]

    return last_col


def build_alignment_matrix(left , right, match = 1, mismatch=-1, gap=-1):
    """
        Perform overlap alignment between 2 sequence. It alings in such fashion -
        # left  sequence : --------------
        # right sequence :        --------------
        It follows a Base Case => OPT(0,j) = 0 for 0 ≤ j ≤ m
        And trace back starts from => max OPT(i,m) for 0 ≤ i ≤ n

        Parameters:
        left : Leftward Sequence
        rigth : Rightward Sequence
        match : match score
        mismatch : mismatch score [should be -ve sign]
        gap : gap penalty [should be -ve sign]

        Returns:
        A tuppple of 2 matrices : Score matrix, Trace matrix
    """
    mat = [ [-i] + [0]*(len(left)) for i in range(len(right)+1) ]
    trace = [ ['---']+['h--']*len(left) 
            if i == 0 else ['--v']+['---']*len(left) 
            for i in range(len(right)+1) ]

    # mismatch = -1
    # match = 1
    # gap = -1

    for i in range(1, len(right)+1):
        for j in range(1, len(left)+1): 
            if right[i-1] == left[j-1] : diag = mat[i-1][j-1] + match
            else : diag = mat[i-1][j-1] + mismatch

            hor = mat[i][j-1] + gap
            ver = mat[i-1][j] + gap

            mat[i][j] = max(diag, hor, ver)

            if   hor > diag and hor > ver : trace[i][j] = 'h--'
            elif diag > hor and diag > ver  : trace[i][j] = '-d-'
            elif ver > diag and ver > hor : trace[i][j] = '--v'
            elif diag == hor and diag > ver : trace[i][j] = 'hd-'
            elif ver == hor and ver > diag : trace[i][j] = 'h-v'
            elif ver > hor and ver == diag : trace[i][j] = '-dv'
            else : trace[i][j] = 'hdv'
    
    # for row in mat : print(row)
    # for row in trace : print(row)

    return (mat, trace)


def get_maximum_score_index(score, verbose=False):
    left_index = len(score[0]) - 1
    right_index = len(score) - 1
    max_score = max([score[i][left_index] for i in range(right_index+1)])

    if(verbose):
        print([score[i][left_index] for i in range(right_index+1)])
        print("left seqecuence length -", left_index)
        print("right seqecuence length -", right_index)
    
    for i in range(right_index, -1, -1):
        if score[i][left_index] == max_score:
            right_index = i
            break

    if verbose:
        print(f"% score - {(max_score/right_index)*100:.4f}%")
        print("Socre of overlap region -", max_score)

    return (max_score, left_index, right_index)











if __name__ == "__main__":
    build_alignment_matrix("AGCT", "ASC")





