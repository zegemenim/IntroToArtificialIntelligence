import matplotlib.pyplot as plt
import numpy as np
#increasing age
age_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#random heights
height_list = np.random.randint(150, 200, 10)
plt.plot(age_list, height_list, 'y')
plt.show()

df = np.random.randint(1, 100, (5, 3))
np_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
new_fig = plt.figure(dpi=100)
new_axes = new_fig.add_axes([0.1, 0.1, 0.9, 0.9])
new_axes.plot(np_array, np_array**2, 'r', label='x squared')
new_axes.plot(np_array, np_array**3, 'b', label='x cubed')
new_axes.set_xlabel('X axis')
new_axes.set_ylabel('Y axis')
new_axes.set_title('X vs Y')
new_axes.legend()
plt.show()

data1 = np.linspace(0, 10, 20)
data2 = data1 ** 2
new_fig, new_axes = plt.subplots()
new_axes.plot(data1, data1+2, color='blue', linewidth=4, linestyle='--', label='Linear', marker='o', markersize=8, markerfacecolor='red')
plt.show()