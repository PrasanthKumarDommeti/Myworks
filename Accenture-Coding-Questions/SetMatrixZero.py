from math import *
from collections import *
from sys import *

from typing import List

#from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    """
    Sets the entire row and column to 0's if an element is 0 in the given matrix.

    Args:
    matrix (List[List[int]]): A 2D list of integers.

    Returns:
    None
    """
    # Get the number of rows and columns in the matrix
    rows, cols = len(matrix), len(matrix[0])
    
    # Initialize sets to store the rows and columns that need to be zeroed
    zero_rows, zero_cols = set(), set()
    
    # Iterate over the matrix to find the cells with 0's
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    
    # Iterate over the matrix again to set the rows and columns to 0's
    for i in range(rows):
        for j in range(cols):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0

