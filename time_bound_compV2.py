import matplotlib.pyplot as plt
import numpy as np
import time
from numba import jit


@jit(nopython=True)
def jit_matrix_mult(n, a, b):
    c = [[0 for col in range(n)] for row in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = 0
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]



class matrix_calc():
    def __init__(self):
        self.timenor = []
        self.input_size = []
        self.timenum = []
        self.timejit = []

    def rand_matrix_gen(self,n):
        array1 = np.random.rand(n, n)
        array2 = np.random.rand(n, n)
        return array1,array2

    def matrix_mult (self,n,a,b):
        c = [[0 for col in range(n)] for row in range(n)]
        for i in range(n):
            for j in range(n):
                c[i][j] = 0
                for k in range(n):
                    c[i][j] += a[i][k] * b[k][j]

    def main (self):
        for i in range (1,20):
            j = i*10
            a,b = self.rand_matrix_gen(j)

            start = time.process_time()
            self.matrix_mult(j,a,b)
            stop = time.process_time()
            self.timenor.append(stop-start)

            start = time.process_time()
            jit_matrix_mult(j, a, b)
            stop = time.process_time()
            self.timejit.append(stop - start)

            start = time.process_time()
            np.matmul(a,b)
            stop = time.process_time()
            self.timenum.append(stop - start)

            self.input_size.append(j)
            print("Done", i*10)

        plt.plot(self.input_size, self.timenum,label='With numpy')
        plt.plot(self.input_size, self.timenor,label='With python')
        plt.plot(self.input_size, self.timejit,label='With python and numba.jit')
        plt.xlabel('Input size')
        plt.ylabel('Time')

        plt.title('Time Bound Computations For Matrix Multiplication')
        plt.legend()
        plt.show()


instance = matrix_calc()
instance.main()
