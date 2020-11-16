#File to reduce to a given matrix(as a nested list) to echelon or reduced echelon form
import RowOperations

class Reducer:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    # convert matrix to echelon form
    def EchelonForm(self):
        #storing number of leading zeros in each row
        zero_count = {}
        for rowno in range(0,self.rows):
            count = 0
            for colno in range(0,self.cols):
                if(self.matrix[rowno][colno] != '0'):
                    zero_count[rowno] = count
                    break
                count += 1
            if(colno == (self.cols-1)):
                zero_count[rowno] = count

        #sorting matrix based on number of leading zeroes
        zero_ordered_matrix = []
        while(zero_count):
            key_list = list(zero_count.keys())
            val_list = list(zero_count.values())
            min_index = key_list[val_list.index(min(val_list))]
            zero_ordered_matrix.append(self.matrix[min_index])
            zero_count.pop(min_index)

        return zero_ordered_matrix