import Reducer as ReducerModule

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
            matrix.append(input().split(" "))
            if(len(matrix[i]) == columns):
                break
            else:
                print("Each row requires " + str(columns) + " arguments. Try again!")
    
    return matrix

if __name__ == '__main__':
    matrix = takeInput()
    
    print('Given matrix: ')
    for row in matrix:
        print(row)
    
    rd = ReducerModule.Reducer(matrix)

    print('Reduced echelon form: ')
    rd.EchelonForm()