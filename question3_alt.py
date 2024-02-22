from math import comb as nCr
from time import perf_counter_ns
from matplotlib import pyplot as plt
from typing import Callable
import sys
from io import StringIO


def pascal_triangle(n):
    last_line = []
    for line_index in range(n):
        # create list for current line cells
        current_line = []
        # calculate and print cells for current line
        for cell_index in range(line_index+1):
            # if first or last cell then value is one
            if cell_index == 0 or cell_index == line_index:
                value = 1
            else:
                # otherwise value is sum of last_line[i-1] + last_line[i]
                value = last_line[cell_index-1] + last_line[cell_index]
            current_line.append(value)
            print(value, end='\t')
        print()
        last_line = current_line


def pascal_triangle_ncr(n):
    for row in range(n):
        for col in range(row + 1):
            print(nCr(row, col), end='\t')
        print()


plt.style.use('_mpl-gallery')


figure, axes = plt.subplots()
x = list(range(1, 200))


def calc_performance(func: Callable[[int], None]):
    fake_out = StringIO()
    tmp_stdout = sys.stdout
    sys.stdout = fake_out
    time_iterations = list()
    for i in range(1, 200):
        time_start = perf_counter_ns()
        func(i)
        time_end = perf_counter_ns()
        time_iterations.append((time_end - time_start))
    sys.stdout = tmp_stdout
    return time_iterations


y_pascal_triangle = calc_performance(pascal_triangle)
y_pascal_triangle_ncr = calc_performance(pascal_triangle_ncr)

axes.plot(x, y_pascal_triangle, label='pascal_triangle', color='red')
axes.plot(x, y_pascal_triangle_ncr, label='pascal_triangle_ncr', color='blue')

plt.show()




