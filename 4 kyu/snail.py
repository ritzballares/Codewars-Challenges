'''
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
'''


def snail(snail_map):
    snail_sort = []

    if not snail_map:
        return snail_sort

    row_start = 0
    row_end = len(snail_map) - 1
    col_start = 0
    col_end = len(snail_map[0]) - 1

    while row_start <= row_end and col_start <= col_end:
        for i in range(col_start, col_end+1):  # Going right
            snail_sort.append(snail_map[row_start][i])
        row_start += 1

        for i in range(row_start, row_end+1):  # Going down
            snail_sort.append(snail_map[i][col_end])
        col_end -= 1

        if row_start <= row_end:
            for i in range(col_end, col_start-1, -1):  # Going left
                snail_sort.append(snail_map[row_end][i])
            row_end -= 1

        if col_start <= col_end:
            for i in range(row_end, row_start-1, -1):
                snail_sort.append(snail_map[i][col_start])
            col_start += 1

    return snail_sort
