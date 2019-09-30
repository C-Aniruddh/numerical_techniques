import numpy as np

def determinant(lst):
    array = np.array(lst)
    return np.linalg.det(array)

a_values = input('Enter values for A : ')
b_values = input('Enter values for B : ')
c_values = input('Enter values for C : ')
d_values = input('Enter values for D : ')

a_vals = list(map(int, a_values.split(' ')))
b_vals = list(map(int, b_values.split(' ')))
c_vals = list(map(int, c_values.split(' ')))
d_vals = list(map(int, d_values.split(' ')))

lst =[a_vals, b_vals, c_vals]
det = determinant(lst)

if (det != 0):
    lst_x = [d_vals, b_vals, c_vals]
    detX = determinant(lst_x)

    lst_y = [a_vals, d_vals, c_vals]
    detY = determinant(lst_y)

    lst_z = [a_vals, b_vals, d_vals]
    detZ = determinant(lst_z)

    X = detX / det
    Y = detY / det
    Z = detZ / det

    print("X = {}, Y = {}, Z = {}".format(X, Y, Z))
else:
    print("Invalid inputs, determinant value = 0")
