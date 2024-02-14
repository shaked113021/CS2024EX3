
def pascal_triangle(n):
    PRINTED_CELL_SIZE = 5
    last_line = []
    for line_index in range(n):
        # calculating padding for line using non-flooring division to handle even lines half a cell padding
        padding = (n - line_index - 1) / 2
        # create list for current line cells
        current_line = []
        # print padding
        print(' ' * (round(PRINTED_CELL_SIZE * padding)), end='')
        # calculate and print cells for current line
        for cell_index in range(line_index+1):
            # if first or last cell then value is one
            if cell_index == 0 or cell_index == line_index:
                value = 1
            else:
                # otherwise value is sum of last_line[i-1] + last_line[i]
                value = last_line[cell_index-1] + last_line[cell_index]
            current_line.append(value)
            print(value, end=' ' * (PRINTED_CELL_SIZE - len(str(value))))
        print()
        last_line = current_line


num_lines = input('please enter number of lines(must be positive integer): ')
while (not num_lines.isnumeric()) or (int(num_lines) == 0):
    num_lines = input("Invalid input! please enter a positive integer: ")

num_lines = int(num_lines)
pascal_triangle(num_lines)
