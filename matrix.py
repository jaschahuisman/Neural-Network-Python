import math
import random

class Matrix:
    '''
    Matrix:
    ---
    A matrix has rows and columns, wich contain values (default 0).
    Matrixes can be modified with matrix methods.



    Parameters:
    ---
        rows (int): Rows
        cols (int): Columns
        data (Array): Matrix data
            
    '''

    # Initialize
    def __init__(self, rows:int, cols:int):
        self.rows = rows
        self.cols = cols
        self.data = []
        
        for i in range(self.rows):
            self.data.append([])
            for _ in range(self.cols):
                self.data[i].append(0)

    @staticmethod
    def fromArray(arr: list):
        '''Create a single column matrix from an array.'''
        m = Matrix(len(arr), 1)
        for i in range(len(arr)):
            m.data[i][0] = arr[i]
        return m
   
    def toArray(self):
        '''Create an array of a matrix.'''
        arr = []
        for i in range(self.rows):
            for j in range(self.cols):
                arr.append(self.data[i][j])
        return arr


    # Print the matrix array
    def print(self):
        '''Print the matrix in a table form'''
    
        print("")
        print(f"Matrix ({self.rows} rows x {self.cols} columns)")
        print("———————————————————————————")
        for i in range(self.rows):
            row = "r | "
            for j in range(self.cols):
                row = (f" {row} {self.data[i][j]} ")
            print(row)
        print("———————————————————————————")
        print("")

    # Randomize
    def randomize(self):
        '''Randomize tha data in a matrix floating between -1 and 1'''
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = 1 * random.randint(0,100)/100


    # Scalar Add
    def add(self, n):
        '''
        Add:
        ---
            Adds each matrix container with the value n.
            Add multiple matrixes to each other.
        '''
        for i in range(self.rows):
            for j in range(self.cols):
                if (isinstance(n, Matrix)):
                    self.data[i][j] += n.data[i][j]
                else:
                    self.data[i][j] += n 
    
    # Scalar Substract
    # def substract(self, n):
    #     '''
    #     Substract:
    #     ---
    #         Substracts each matrix container with the value n.
    #         Substract multiple matrixes from each other.
    #     '''
    #     for i in range(self.rows):
    #         for j in range(self.cols):
    #             if (isinstance(n, Matrix)):
    #                 self.data[i][j] -= n.data[i][j]
    #             else:
    #                 self.data[i][j] -= n 

    @staticmethod
    def subtract(a, b):
        '''
        Subtract:
        ---
            Subtracts one matrix from another
        '''   
        if (isinstance(a, Matrix) and isinstance(b, Matrix)):
            # TODO: Check matrixes size
            result = Matrix(a.rows, a.cols)

            for i in range(result.rows):
                for j in range(result.cols):
                    result.data[i][j] = a.data[i][j] - b.data[i][j]
            return result
    
    # Multiply (Static Matrix)
    @staticmethod
    def multiply(a, b):
        '''
        Calculate the matrix product of two matrixes.

        Requirements:
        ---
            * Parameters are both matrixes
            * Rows of Matrix a have to be equal to columns of Matrix b

        Returns:
        ---
            Matrix(a.rows, b.cols)
        '''
        if (isinstance(a, Matrix) and isinstance(b, Matrix)):
            # Matrix Product
            # TODO: Rewrite code of checking matrix size
            if (not a.cols == b.rows):
                try:
                    raise Warning(f"The columns of the matrix ({a.cols}) don't match with the rows of the other matrix ({b.rows}).")
                except:
                    raise
            else:
                result = Matrix(a.rows, b.cols)

                for i in range(result.rows):
                    for j in range(result.cols):
                        sum = 0
                        for k in range(a.cols):
                            sum += a.data[i][k] * b.data[k][j]
                        result.data[i][j] = sum
                return result
    
    # Multiply (Non Static Scalar)
    def s_multiply(self, n):
        '''
        Scalar Multiply:
        ---
            Multiplies each matrix container with value n.
        '''
        # Scalar Product
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] *= n 

    # Transpose
    def transpose(self):
        '''
        Transposes a matrix from (rows,cols) to (cols, rows)
        '''
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result

    # Non Static Map function
    def map(self, fn):
        '''
        Executes function fn to all matrix container values individually and returns the values back in the matrix.
       
        Updated values:
        ---
            val = self.data[i][j]
            self.data[i][j] = fn(val)
        '''
        for i in range(self.rows):
            for j in range(self.cols):
                val = self.data[i][j]
                self.data[i][j] = fn(val)

    @staticmethod
    def s_map(matrix, fn):
        '''
        Executes function fn to all matrix container values individually and returns the values back in the matrix.
       
        Updated values:
        ---
            val = self.data[i][j]
            self.data[i][j] = fn(val)
        '''
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                val = matrix.data[i][j]
                matrix.data[i][j] = fn(val)
        
        return matrix

