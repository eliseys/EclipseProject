import numpy as np




step = -1.0

def bracket(n_0, n):
    for i in np.arange(n, n_0-1, step):
        if i < 0:
            print(i, "\t", "1/"+str(2**(-i)), "\t\t", 1.0/2**(-i))
        if i >= 0:
            print(i, "\t", str(2**i), "\t\t", 2**i)

        
def sum_bracket(n_0, n):
    s = 0
    for i in np.arange(n, n_0-1, step):
        s = s + 2**i
    return s




n = 2


n_0 = n - 6

bracket(n_0, n)

print("Corrected summa", (sum_bracket(n_0, n)+7*0.1)*1.25)
print("Exposure time", sum_bracket(n_0, n))
