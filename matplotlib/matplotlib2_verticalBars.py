import numpy as np
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# ---------------------- PROBLEM - bars stacked on one another ----------------------------

# dev_y = [38496, 42000, 46752, 49320, 53200,
#          56000, 62316, 64928, 67317, 68748, 73752]
# plt.bar(ages_x, dev_y, color="#444444", label="All Devs")
#
# py_dev_y = [45372, 48876, 53850, 57287, 63016,
#             65998, 70003, 70000, 71496, 75370, 83640]
# plt.bar(ages_x, py_dev_y, color="#008fd5", label="Python")
#
# js_dev_y = [37810, 43515, 46823, 49293, 53437,
#             56373, 62375, 66674, 68745, 68746, 74583]
# plt.bar(ages_x, js_dev_y, color="#e5ae38", label="JavaScript")



# -------------- SOLUTION to display bars side by side - offset x values each time we plot some data (using numpy) --------------

# create a range from x values using numpy (it is a numpy array of values (values are numbered version of our x values - like a list)):
x_indexes = np.arange(len(ages_x))
width = 0.25  # width of bars

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
# use x_indexes instead of ages_x, and now we can shift a location of these by adding or subtracting (first bar to the left and last to the right)
# we need to shift them by exact width of a bar, so we need to specify a width of bars
# also we need to specify that the width of our bars are width we declared (width=width)
plt.bar(x_indexes - width, dev_y, width=width, color="#444444", label="All Devs")

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_indexes, py_dev_y, width=width, color="#008fd5", label="Python")

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_indexes + width, js_dev_y, width=width, color="#e5ae38", label="JavaScript")

# but now we have our x axis values of indexes, so we need to fix that with xticks

plt.legend()

plt.xticks(ticks=x_indexes, labels=ages_x)  # we use x_indexes as a ticks, but for labels we use ages_x

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

plt.tight_layout()

plt.show()