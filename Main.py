import Reducer as ReducerModule
from fractions import Fraction

rows = 0
columns = 0

def takeInput():
    while(True):
        print("Enter number of rows and columns in the matrix seperated by whitespace:")
        dimensions = input().split(" ")
        if(len(dimensions) == 2):
            rows = int(dimensions[0])
            columns = int(dimensions[1])
            break
        else:
            print("Two arguments required. Try again!")
    
    matrix = []
    for i in range(0, rows):
        print("Enter elements in row " + str((i+1)) + " seperated by whitespace:")
        while(True):
            inputRow = list(map(float, input().split(" ")))
            if(len(inputRow) == columns):
                matrix.append(inputRow)
                break
            else:
                print("Each row requires " + str(columns) + " arguments. Try again!")
    
    return matrix

if __name__ == '__main__':
    matrix = takeInput()

    print()
    
    print('Given matrix:')
    for row in matrix:
        print(row)

    print()
    
    rd = ReducerModule.Reducer(matrix)
    print('Echelon form:')
    matrix = rd.EchelonForm()
    for row in matrix:
        print(["{0:0.3f}".format(element) for element in row], end='')
        print('\t', end='')
        print([str(Fraction(element).limit_denominator()) for element in row])

    print()

    print('Reduced Echelon form:')
    matrix = rd.ReducedEchelonForm()
    for row in matrix:
        print(["{0:0.3f}".format(element) for element in row], end='')
        print('\t', end='')
        print([str(Fraction(element).limit_denominator()) for element in row])

    print()