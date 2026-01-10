question = input("What is your question? ")
print("You asked:", question)
print("Ooor who cares? ¯\\_(ツ)_/¯")
print('"Sokaklar sakin, geceler karabasan.\nEllerim titrer, kim bu ben, kim bu susan?"')
if question.strip().endswith('?'):
    print("That's a question!")
else:
    print("BTW, is it really a question? 🤔")

import numpy as np
np_array = np.random.random_integers(1, 10, (3, 3))
np_array2 = np.random.random_integers(1, 10, (3, 3))
print("Here is a random numpy array:\n", np_array)
print("Here is the array multiplied by 2:\n", np_array2)
print("Here is the sum of the two arrays:\n", np_array + np_array2)
np_list = np.arange(10)
print("Here is a numpy array created from a range:\n", np_list)


matrix_array = np.array([1, 2, 3])
print("Here is a 1x3 matrix:\n", matrix_array)
matrix_array2 = np.array([[1, 2], [3, 4], [5, 6]])
print("Here is a 3x2 matrix:\n", matrix_array2)
print("Here is the dot product of the two matrices:\n", matrix_array.dot(matrix_array2))

# 1x1 + 2x3 + 3x5 = 22 & 1x2 + 2x4 + 3x6 = 28

my_matrix_array = np.array([[1, 2], [4, 5], [7, 8]])
print("Here is a 3x2 matrix:\n", my_matrix_array)
my_matrix_array2 = np.array([[1, 0, 5, 5, 6, 8, 9], [0, 1, 2, 3, 4, 5, 6]])
print("Here is a 2x7 matrix:\n", my_matrix_array2)
print("Here is the dot product of the two matrices:\n", my_matrix_array.dot(my_matrix_array2))

import pandas as pd
data = np.random.randint(1, 100, (5, 3))
df = pd.DataFrame(data, columns=['A', 'B', 'C'], index=['row1', 'row2', 'row3', 'row4', 'row5'])
print("Here is a random pandas DataFrame:\n", df)