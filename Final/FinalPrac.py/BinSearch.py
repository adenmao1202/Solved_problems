"""
Requirements:
The function should use a nested loop to iterate through the rows and columns of the matrix.
If the target is found, return its position as a tuple (row, col).
If the target is not found after scanning the entire matrix, return (-1, -1).
---------------------------------------------------------------------------------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
target = 5

matrix_search(matrix, target) -> (1, 1)
-----------------------------------------------------------
"""
def matrix_search(matrix, target):  #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in range(len(matrix)):  
        for j in range(len(matrix[0])):
            if matrix[i][j] == int(target):
                return (i, j)
            
    return (-1, -1) # tuple

# def main(): # 假設輸入的都是3x3的矩陣
#     matrix_input = input().split()  # --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     target = int(input())
    
#     matrix = []
#     for i in range(0, len(matrix_input), 3): # 0, 3, 6
#         matrix.append([matrix_input[i], matrix_input[i+1], matrix_input[i+2]])
    
#     print(matrix)
#     print(matrix_search(matrix, target))

def main():
    # Input matrix as space-separated rows, with rows separated by newlines
    rows = int(input("Enter number of rows: ")) # supposed to be a square matrix 
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().split())))
    
    target = int(input("Enter target value: "))
    result = matrix_search(matrix, target)
    print(result)

if __name__ == "__main__":
    main()