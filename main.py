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
def fwht(a) -> None:
    """In-place Fast Walsh–Hadamard Transform of array a."""
    h = 1
    while h < len(a):
        for i in range(0, len(a), h * 2):
            for j in range(i, i + h):
                x = a[j]
                y = a[j + h]
                a[j] = x + y
                a[j + h] = x - y
        h *= 2
    return a

def WFT(array):
    if (len(array) == 1):
        return array
    left_subarray = [0] * (int)(len(array) / 2)
    right_subarray = [0] * (int)(len(array) / 2)
    i = 0
    while i < len(array) / 2:
        left_subarray[i] = array[i] + array[i + (int)(len(array) / 2)]
        right_subarray[i] = array[i] - array[i + (int)(len(array) / 2)]
        i += 1
    left_subarray = WFT(left_subarray)
    right_subarray = WFT(right_subarray)
    result = [0] * len(array)
    i = 0
    while i < len(array) / 2:
        result[i] = left_subarray[i]
        result[i + (int)(len(array) / 2)] = right_subarray[i]
        i += 1
    return result

##################
x_result = range(0, N)
y_result = WFT(discrete_y_points)
i = 0
while i < len(y_result):
    y_result[i] /= N
    i += 1
######График амплитуд
m = 0
amp_result = [0] * N
while m < len(y_result):
    amp_result[m] = abs(y_result[m])
    m += 1

plt.grid(True)
plt.title("График амплитуды БПУ")
plt.bar(x_result, amp_result,
        width=0.1, color='blue', alpha=0.7,
        zorder=2)
plt.show()

##################
x_result = range(0, N)
y_result = fwht(discrete_y_points)
######График амплитуд by python
m = 0
amp_result = [0] * N
while m < len(y_result):
    amp_result[m] = abs(y_result[m])
    m += 1

plt.grid(True)
plt.title("График амплитуды БПУ by python")
plt.bar(x_result, amp_result,
        width=0.1, color='blue', alpha=0.7,
        zorder=2)
plt.show()

####График фазы
# m = 0
# phase_result = [0] * N
# while m < len(y_result):
#     phase_result[m] = y_result[m].imag
#     m += 1
#
# plt.grid(True)
# plt.title("График фазы ДПФ")
# plt.bar(x_result, phase_result,
#         width=0.1, color='blue', alpha=0.7,
#         zorder=2)
# plt.show()
