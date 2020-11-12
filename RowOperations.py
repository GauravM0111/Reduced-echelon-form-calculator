#Function to store all matrix row operations

# eg: R1 <-> R2
def swapRows(matrix, row1_number, row2_number):
    temp = matrix[row1_number]
    matrix[row1_number] = matrix[row2_number]
    matrix[row2_number] = temp

    return matrix


# eg: R2 = 2R1 + 4R2
def addOperation(matrix, row1_number, row2_number, row1_multiple, row2_multiple):
    row1 = matrix[row1_number].copy()
    row2 = matrix[row2_number].copy()

    for i in range(0, len(row1) - 1):
        row1[i] = int(row1[i]) * row1_multiple
        row2[i] = int(row2[i]) * row2_multiple
        matrix[row2_number][i] = str(row1[i] + row2[i])

    return matrix


# R1 = 3R1
def scalarMultiply(matrix, rowNumber, multiple):
    for i in range(0, len(matrix[rowNumber])):
        matrix[rowNumber][i] = str(int(matrix[rowNumber][i]) * multiple)
    
    return matrix
