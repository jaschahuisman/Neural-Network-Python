import math
import random

class Matrix:
    # Initialize
    def __init__(self, rows:int, cols:int):
        self.rows = rows
        self.cols = cols
        self.matrix = []
        
        for i in range(self.rows):
            self.matrix.append([])
            for j in range(self.cols):
                self.matrix[i].append(0)

    # Print the matrix array
    def print(self):
        print("")
        print(f"Matrix ({self.rows} rows x {self.cols} columns)")
        print("———————————————————————————")
        for i in range(self.rows):
            row = "r | "
            for j in range(self.cols):
                row = (f" {row} {self.matrix[i][j]} ")
            print(row)
        print("———————————————————————————")
        print("")

    # Randomize
    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                # self.matrix[i][j] = 1 * random.randint(0,100)/100
                self.matrix[i][j] = 1 * random.randint(0,10)

    # Scalar Add
    def add(self, n):
        for i in range(self.rows):
            for j in range(self.cols):
                if (isinstance(n, Matrix)):
                    self.matrix[i][j] += n.matrix[i][j]
                else:
                    self.matrix[i][j] += n 
    
    # Scalar Substract
    def substract(self, n):
        for i in range(self.rows):
            for j in range(self.cols):
                if (isinstance(n, Matrix)):
                    self.matrix[i][j] -= n.matrix[i][j]
                else:
                    self.matrix[i][j] -= n 
    
    # Multiply
    def multiply(self, n):

        if (isinstance(n, Matrix)):
            # Matrix Product
            if (not self.cols == n.rows):
                try:
                    raise Warning(f"The columns of the matrix ({self.cols}) don't match with the rows of the other matrix ({n.rows}).")
                except:
                    raise
            else:
                a = self
                b = n
                result = Matrix(a.rows, b.cols)

                for i in range(result.rows):
                    for j in range(result.cols):
                        sum = 0
                        for k in range(a.cols):
                            sum += a.matrix[i][k] * b.matrix[k][j]
                            # print(f"{a.matrix[i][k]} =")
                        result.matrix[i][j] = sum
                return result
        else:
            # Scalar Product
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] *= n 

    # Transpose
    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[j][i] = self.matrix[i][j]
        return result

    
        
   

# m1 = Matrix(3, 1)
# m1.randomize()

# m2 = m1.transpose()


# m1.print()
# m2.print()













