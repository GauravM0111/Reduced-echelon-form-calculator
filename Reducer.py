#File to reduce to a given matrix(as a nested list) to echelon or reduced echelon form
import RowOperations

class Reducer:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    # convert matrix to echelon form
    def EchelonForm(self):
        #making matrix rows ordered by number of leading zeroes
        self.matrix = RowOperations.orderByLeadingZeroes(self.matrix)

        #identifying pivots and making elements below them zero
        for row in range(0,self.rows):
            for col in range(0,self.cols):
                if(self.matrix[row][col] != 0.0):
                    for row_below in range(row+1, self.rows):
                        if(self.matrix[row_below][col] != 0.0):
                            row1_multiple = -1.0 * (self.matrix[row_below][col] / self.matrix[row][col])
                            self.matrix = RowOperations.addOperation(self.matrix, row, row_below, row1_multiple, 1)
                    break
        self.matrix = RowOperations.orderByLeadingZeroes(self.matrix)
        
        return self.matrix

    #convert a matrix to reduced echelon form
    def ReducedEchelonForm(self):
        #convert a matrix to echelon form first
        #making matrix rows ordered by number of leading zeroes
        self.matrix = RowOperations.orderByLeadingZeroes(self.matrix)

        #identifying pivots and making elements below them zero
        for row in range(0,self.rows):
            for col in range(0,self.cols):
                if(self.matrix[row][col] != 0.0):
                    for row_below in range(row+1, self.rows):
                        if(self.matrix[row_below][col] != 0.0):
                            row1_multiple = -1.0 * (self.matrix[row_below][col] / self.matrix[row][col])
                            self.matrix = RowOperations.addOperation(self.matrix, row, row_below, row1_multiple, 1)
                    break
        self.matrix = RowOperations.orderByLeadingZeroes(self.matrix)


        #making each pivot = 1 and all values above pivot = 0
        for row in range(0,self.rows):
            for col in range(0, self.cols):
                if(self.matrix[row][col] != 0.0): #pivot found
                    #making pivot = 1
                    self.matrix = RowOperations.scalarMultiply(self.matrix, row, (1.0/self.matrix[row][col]))

                    #making all values above pivot = 0
                    for row_above in range(row-1, -1, -1):
                        if(self.matrix[row_above][col] != 0.0):
                            row1_multiple = -1.0 * (self.matrix[row_above][col] / self.matrix[row][col])
                            self.matrix = RowOperations.addOperation(self.matrix, row, row_above, row1_multiple, 1)

                    break

        return self.matrix