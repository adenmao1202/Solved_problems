def calculate_sums(matrix, n):
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(matrix[row][col] for row in range(n)) for col in range(n)]
    return row_sums, col_sums


def is_testable(row_sums, col_sums):
    return all(s % 2 == 0 for s in row_sums) and all(s % 2 == 0 for s in col_sums)


def find_change(matrix, row_sums, col_sums, n):
    odd_rows = [index for index, value in enumerate(row_sums) if value % 2 != 0]
    odd_cols = [index for index, value in enumerate(col_sums) if value % 2 != 0]

    if len(odd_rows) == 1 and len(odd_cols) == 1:
        return odd_rows[0], odd_cols[0]
    return None




def main():
    while True:
        num = int(input())
        if num == 0:
            break

        matrix = []
        for _ in range(num):
            row = [int(x) for x in input().split()]
            matrix.append(row)

        row_sums, col_sums = calculate_sums(matrix, num)
        if is_testable(row_sums, col_sums):
            print("OK")
        else:
            change = find_change(matrix, row_sums, col_sums, num)
            if change:
                print(f"Change bit ({change[0]+1},{change[1]+1})", flush=True)
            else:
                print("Corrupt")


if __name__ == "__main__":
    main()
