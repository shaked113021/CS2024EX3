
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

