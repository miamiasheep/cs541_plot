# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import sys
import numpy as np

file_name = sys.argv[1]
data = []
for line in open(file_name):
    data.append(float(line.strip()))
print(sum(data))
print(np.std(data))
print(np.average(data))
plt.xlabel('batches')
plt.ylabel('number of splits')
plt.plot(data)
plt.show()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
