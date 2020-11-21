#File to store all matrix row operations

# order matrix by leading zeroes
def orderByLeadingZeroes(matrix):
    #storing number of leading zeros in each row
    rows = len(matrix)
    cols = len(matrix[0])
    zero_count = {}

    for rowno in range(0,rows):
        count = 0
        for colno in range(0,cols):
            if(matrix[rowno][colno] != 0.0):
                zero_count[rowno] = count
                break
            count += 1
        if(colno == (cols-1)):
            zero_count[rowno] = count
            
    #sorting matrix based on number of leading zeroes
    zero_ordered_matrix = []
    while(zero_count):
        key_list = list(zero_count.keys())
        val_list = list(zero_count.values())
        min_index = key_list[val_list.index(min(val_list))]
        zero_ordered_matrix.append(matrix[min_index])
        zero_count.pop(min_index)
    del zero_count

    return zero_ordered_matrix

# eg: R2 = 2R1 + 4R2
def addOperation(matrix, row1_number, row2_number, row1_multiple, row2_multiple):
    row1 = matrix[row1_number].copy()
    row2 = matrix[row2_number].copy()

    for i in range(0, len(row1)):
        row1[i] = row1[i] * row1_multiple
        row2[i] = row2[i] * row2_multiple
        sum = row1[i] + row2[i]
        if(sum == -0.0):
            matrix[row2_number][i] = 0.0
        else:
            matrix[row2_number][i] = sum

    return matrix


# R1 = 3R1
def scalarMultiply(matrix, rowNumber, multiple):
    for i in range(0, len(matrix[rowNumber])):
        product = matrix[rowNumber][i] * multiple
        if(product == -0.0):
            matrix[rowNumber][i] = 0.0
        else:
            matrix[rowNumber][i] = product
    
    return matrix