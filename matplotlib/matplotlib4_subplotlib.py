import pandas as pd
from matplotlib import pyplot as plt

# ------------ WITHOUT SUBPLOTS (single figure and single axes (plot) object) --------------

# plt.style.use('seaborn')
#
# data = pd.read_csv('data1.csv')
# ages = data['Age']
# dev_salaries = data['All_Devs']
# py_salaries = data['Python']
# js_salaries = data['JavaScript']
#
# print(ages)  # index and value
#
# plt.plot(ages, py_salaries, label='Python')
# plt.plot(ages, js_salaries, label='JavaScript')
#
# plt.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')
#
# plt.legend()
#
# plt.title('Median Salary (USD) by Age')
# plt.xlabel('Ages')
# plt.ylabel('Median Salary (USD)')
#
# plt.tight_layout()
#
# plt.show()


# ------------ WITH SUBPLOTS method (if we want additional plots or work with plots in more object-oriented manner) --------------

plt.style.use('seaborn')

data = pd.read_csv('data1.csv')  # load .csv file using pandas method read_csv
ages = data['Age']  # Age column values are saved in ages var
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# subplots create a figure and specifies a certain number of rows and columns of axes
# fig, ax = plt.subplots() # a single axe at the moment (or a single plot), default one by one - one row and one column = 1 axes
#
# # plt.plot(ages, py_salaries, label='Python')
# # plt.plot(ages, js_salaries, label='JavaScript')
# #
# # plt.plot(ages, dev_salaries, color='#444444',
# #          linestyle='--', label='All Devs')
#
# # switch plt. object to ax.:
# ax.plot(ages, py_salaries, label='Python')
# ax.plot(ages, js_salaries, label='JavaScript')
#
# ax.plot(ages, dev_salaries, color='#444444',vlinestyle='--', label='All Devs')
#
# # plt.legend()
# ax.legend()
#
# # plt.title('Median Salary (USD) by Age')
# ax.set_title('Median Salary (USD) by Age')
# # plt.xlabel('Ages')
# ax.set_xlabel('Ages')
# # plt.ylabel('Median Salary (USD)')
# ax.set_ylabel('Median Salary (USD)')
#
# plt.tight_layout()
#
# plt.show()

# NOW WE WANT FOR E.G. PYTHON AND JS IN ONE PLOT (AXES), AND ALL DEVS ON ANOTHER:

# fig, ax = plt.subplots(nrows=2, ncols=1)  # two axes in one figure (2 rows, 1 column)
# print(ax)  # we are returning a list of two values here (2 axes)
# so we can unpack these axes:
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)  # two axes in one figure (2 rows, 1 column), sharex will label xticks only for bottom axe
# print these axes individually:
# print(ax1)
# print(ax2)

# if we want different figures:
# fig1, ax1 = plt.subplots()
# fig2, ax2 = plt.subplots()

ax1.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
# ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')

ax2.legend()
# ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()

# fig1.savefig('fig1.png')
# fig2.savefig('fig2.png')