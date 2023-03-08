
# import pydevd_pycharm
# pydevd_pycharm.settrace('localhost', port=59277, stdoutToServer=True, stderrToServer=True)

def factorial(n):
    product = 1
    while n > 1:
        product = product * n
        n = n - 1
    return product


print factorial(5)