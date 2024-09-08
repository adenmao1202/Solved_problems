"""
Matrix HW 6  ( skipped ) 

Function to Calculate Row and Column Sums: 
This function will return two lists, one for the sum of each row and one for the sum of each column.

Function to Check Testability: This function checks if all the sums in the given lists (from the first function) are even.

Function to Identify the Change: If the matrix is not testable, this function will identify if changing a single bit can make it testable.

Main Function: This will handle input, call the other functions, and display the result.
"""
def row_sums(matrix):
    return [sum(row) for row in matrix]

def col_sums(matrix):
    return [sum(matrix[row][col] for row in range(len(matrix))) for col in range(len(matrix[0]))]

def is_testable(row_sums, col_sums):
    return all(s % 2 == 0 for s in row_sums) and all(s % 2 == 0 for s in col_sums)

def find_change(matrix, row_sums, col_sums):
    odd_rows = [index for index, value in enumerate(row_sums) if value % 2 != 0]
    odd_cols = [index for index, value in enumerate(col_sums) if value % 2 != 0]

    if len(odd_rows) == 1 and len(odd_cols) == 1:
        return odd_rows[0], odd_cols[0]
    return None