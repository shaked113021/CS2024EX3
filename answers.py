# EX3 Q1

NUMS_TO_ENTER = 4
SIZE_OF_INPUT = 3


def validate_input(input_str: str) -> bool:
    """Check positive integer and 3 digits. returns True if all both conditions are met"""
    return input_str.isnumeric() and len(input_str) == SIZE_OF_INPUT


inputs_sum = 0

for i in range(NUMS_TO_ENTER):
    num_input = input(f"Please enter a three digit integer for num{i+1}: ")

    while not validate_input(num_input):
        num_input = input(f"Invalid Input! Please enter a three digit integer: ")

    inputs_sum += int(num_input[1])

print("sum of middle digits is:", inputs_sum)
# EX3 Q2

VALID_PEGS = ["A", "B", "C"]


def hanoi(n: int, from_: str, to: str, via: str) -> None:
    # Check parameters
    # is n a positive int
    if not isinstance(n, int):
        raise TypeError("Expected n to be of type 'int'")
    if not n >= 0:
        raise ValueError("Expected n to be 0 or more")
    if not isinstance(from_, str):
        raise TypeError("Expected from_ to be of type 'str'")
    # are from_ via and to valid pegs
    if from_ not in VALID_PEGS:
        raise ValueError(f"Expected from_ to be from [{','.join(VALID_PEGS)}]")
    if not isinstance(to, str):
        raise TypeError("Expected to to be of type 'str'")
    if to not in VALID_PEGS:
        raise ValueError(f"Expected to to be from [{','.join(VALID_PEGS)}]")
    if not isinstance(via, str):
        raise TypeError("Expected via to be of type 'str'")
    if via not in VALID_PEGS:
        raise ValueError(f"Expected via to be from [{','.join(VALID_PEGS)}]")

    # If n is 0 then there are no pegs to move anymore, otherwise there are pegs to move
    if n > 0:
        # move n-1 pegs to via peg, then move disk n to 'to' and move the disks from via to 'to'
        hanoi(n-1, from_, via, to)
        print(f"move disk {n} from {from_} to {to}")
        hanoi(n-1, via, to, from_)
# EX3 Q3
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