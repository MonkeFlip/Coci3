import matplotlib.pyplot as plt
import math
import numpy as np

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
#####################
x_result = range(0, N)
discrete_x_points = [0] * N
discrete_y_points = [0] * N
i = 0
while i < len(discrete_x_points):
    discrete_x_points[i] = x_points[i * 4]
    discrete_y_points[i] = y_points[i * 4]
    i += 1
plt.grid(True)
plt.title("График исходной функции")
plt.plot(discrete_x_points, discrete_y_points)
plt.show()


#радемахер
def R(k, t):
    t = t / N
    if math.sin((2**k)*math.pi*t) > 0:
        return 1
    return -1

def WAL(n,t):
    if n == 0:
        return 1
    result = 1
    r = 1
    if n >= 2:
        r = 2
    if n >= 4:
        r = 3
    if n >= 8:
        r = 4
    if n >= 16:
        r = 5
    k = 1
    while k <= r:
        bit1 = n>>(k - 1) & 1
        if (r - k + 1) == 0:
            bit1 = 0
        bit2 = n>>(k) & 1
        if (r - k) == 0:
            bit2 = 0
        degree = bit1 ^ bit2
        result *= (R(k, t) ** degree)
        k+=1
    return result






def DWT(array):
    result = [0] * N
    s = 0
    while s < N:
        k = 0
        while k < N:
            result[s] += array[k]*WAL(s, k)
            k+=1
        s+=1
    return result





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

def reverse_WFT(array):
    array = WFT(array)
    k = 0
    # while k< len(array):
    #     array[k] /= len(array)
    #     k+=1
    return array

##################
#ДПУ
y_result = DWT(discrete_y_points)
i = 0
while i < len(y_result):
    y_result[i] /= N
    i += 1
plt.grid(True)
plt.title("График ДПУ")
plt.plot(x_result, y_result)
plt.show()

#ДПУ
y_result = DWT(y_result)
plt.grid(True)
plt.title("График обратного ДПУ")
plt.plot(x_result, y_result)
plt.show()


####################
y_result = WFT(discrete_y_points)
i = 0
while i < len(y_result):
    y_result[i] /= N
    i += 1
######График амплитуд

plt.grid(True)
plt.title("График БПУ")
plt.plot(x_result, y_result)
plt.show()

##################
y_result = reverse_WFT(y_result)
######График обратного БПУ


plt.grid(True)
plt.title("График обратного БПУ")
plt.plot(x_result, y_result)
plt.show()

# #################
# x_result = range(0, N)
# y_result = fwht(discrete_y_points)
# ######График амплитуд by python
# plt.grid(True)
# plt.title("График амплитуды БПУ by python")
# plt.plot(x_result, y_result)
# plt.show()
