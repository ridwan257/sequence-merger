

def last_column(matrix):
    last_index = len(matrix[0]) - 1
    last_col = [0]*(len(matrix))

    for i in range(len(matrix)):
        last_col[i] = matrix[i][last_index]

    return last_col



def build_alignment_matrix(left, right):
    mat = [ [-i] + [0]*(len(left)) for i in range(len(right)+1) ]
    trace = [ ['---']+['h--']*len(left) 
            if i == 0 else ['--v']+['---']*len(left) 
            for i in range(len(right)+1) ]

    mismatch = -1
    match = 1
    gap = -1

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

    return mat, trace


def get_maximum_score_index(score):
    S_index = len(score[0]) - 1
    T_index = len(score) - 1
    maxNum = max([score[i][S_index] for i in range(T_index+1)])
    print([score[i][S_index] for i in range(T_index+1)])
    print("left | right -", S_index, T_index)
    
    for i in range(T_index, -1, -1):
        if score[i][S_index] == maxNum:
            T_index = i
            break

    print(f"% score - {(maxNum/T_index)*100:.4f}%")
    print("Socre of overlap region -", maxNum)

    return (maxNum, S_index, T_index)


if __name__ == "__main__":
    build_alignment_matrix("AGCT", "ASC")