


def trace_all_paths(trace_matrix, j, i, path, path_list, limit=None):
    # i --> row index of matrix
    # j --> column index of matrix

    if limit and len(path_list) == limit:
        return
        
    entry = trace_matrix[i][j]
    if i == 0:
        path_list.append(path + 'h'*j)
        return


    if entry[0] == 'h' :
        path += "h"
        trace_all_paths(trace_matrix, j-1, i, path, path_list, limit)
        if path != "" : path = path[:-1]

    if entry[1] == 'd' :
        path += "d"
        trace_all_paths(trace_matrix, j-1, i-1, path, path_list, limit)
        if path != "" : path = path[:-1]
    
    if entry[2] == 'v' :
        path += "v"
        trace_all_paths(trace_matrix, j, i-1, path, path_list, limit)
        if path != "" : path = path[:-1]



def path_to_alignment(left, right, posL, posR, path):
    La, Ra = '', right[posR:][::-1]
    posR -= 1
    posL -= 1
    
    for direction in path:
        if direction == 'd':
            La += left[posL]
            Ra += right[posR]
            posL -= 1
            posR -= 1
        elif direction == 'h':
            La += left[posL]
            Ra += '-'
            posL -= 1
        elif direction == 'v':
            La += '-'
            Ra += right[posR]
            posR -= 1

    if posL != -1:
        offset = left[:posL+1][::-1]
        La += offset
        Ra += '-'*len(offset)

    return La[::-1], Ra[::-1]