import matplotlib.pyplot as plt
import math

x_points = [0] * 64
y_points = [0] * 64
value = 0
i = 0
N = 16
while i < len(x_points):
    y_points[i] = math.sin(value) + math.cos(4 * value)
    x_points[i] = value
    i += 1
    value += 0.1

plt.plot(x_points, y_points)
plt.grid(True)
plt.show()
#####################
discrete_x_points = [0] * N
discrete_y_points = [0] * N
i = 0
while i < len(discrete_x_points):
    discrete_x_points[i] = x_points[i * 4]
    discrete_y_points[i] = y_points[i * 4]
    i += 1
plt.grid(True)
plt.title("График исходной функции")
plt.bar(discrete_x_points, discrete_y_points,
        width=0.1, color='blue', alpha=0.7,
        zorder=2)
plt.show()

###################################################
def DWT(array):
    if (len(array) == 1):
        return array
    left_subarray = [0] * (int)(len(array) / 2)
    right_subarray = [0] * (int)(len(array) / 2)
    i = 0
    while i < len(array) / 2:
        left_subarray[i] = array[i] + array[i + (int)(len(array) / 2)]
        right_subarray[i] = array[i] - array[i + (int)(len(array) / 2)]
        i += 1
    a = DWT(left_subarray)
    b = DWT(right_subarray)
    result = [0] * len(array)
    i = 0
    while i < len(array) / 2:
        result[i] = a[i]
        result[i + (int)(len(array) / 2)] = b[i]
        i += 1

##################
DWT(discrete_y_points)