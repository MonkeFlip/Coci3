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

###################################################
# def fwht(a) -> None:
#     """In-place Fast Walsh–Hadamard Transform of array a."""
#     h = 1
#     while h < len(a):
#         for i in range(0, len(a), h * 2):
#             for j in range(i, i + h):
#                 x = a[j]
#                 y = a[j + h]
#                 a[j] = x + y
#                 a[j + h] = x - y
#         h *= 2
#     return a

def wht_python(x):
    # Function computes (slow) Discrete Walsh-Hadamard Transform
    # for any 1D real-valued signal
    # (c) 2015 QuantAtRisk.com, by Pawel Lachowicz
    x = np.array(x)
    if (len(x.shape) < 2):  # make sure x is 1D array
        if (len(x) > 3):  # accept x of min length of 4 elements (M=2)
            # check length of signal, adjust to 2**m
            n = len(x)
            M = math.trunc(math.log(n, 2))
            x = x[0:2 ** M]
            h2 = np.array([[1, 1], [1, -1]])
            for i in range(M - 1):
                if (i == 0):
                    H = np.kron(h2, h2)
                else:
                    H = np.kron(H, h2)

            return (np.dot(H, x) / 2. ** M, x, M)
        else:
            print("HWT(x): Array too short!")
            raise SystemExit
    else:
        print("HWT(x): 1D array expected!")
        raise SystemExit

#радемахер
def R(k, g ):
    t = g / N
    if math.sin((2**k)*math.pi*t) > 0:
        return 1
    return -1

def WAL(n,t):
    result = 1
    r = 0
    if n <= 16:
        r = 4
    if n <= 8:
        r = 3
    if n <= 4:
        r = 2
    if n <= 2:
        r = 1
    k = 1
    while k <= r:
        degree = (n>>(k - 1) & 1) ^ (n>>(k) & 1)
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
    while k< len(array):
        array[k] /= len(array)
        k+=1
    return array

##################
#ДПУ
y_result = DWT(discrete_y_points)
plt.grid(True)
plt.title("График амплитуды ДПУ")
plt.plot(x_result, y_result)
plt.show()

#ДПУ
y_result = DWT(y_result)
plt.grid(True)
plt.title("График обратного ДПУ")
plt.plot(x_result, y_result)
plt.show()

#ДПУ_by python
y_result = wht_python(discrete_y_points)[0]
plt.grid(True)
plt.title("График амплитуды ДПУ by python")
plt.plot(x_result, y_result)
plt.show()

#ДПУ_by python
y_result = wht_python(y_result)[0]
plt.grid(True)
plt.title("Reverse DWT by python")
plt.plot(x_result, y_result)
plt.show()

####################
y_result = WFT(discrete_y_points)
# i = 0
# while i < len(y_result):
#     y_result[i] /= N
#     i += 1
######График амплитуд

plt.grid(True)
plt.title("График амплитуды БПУ")
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
