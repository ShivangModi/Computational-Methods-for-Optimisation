import numpy as np
from matplotlib import pyplot as plt


class DirectSearchMethods:
    @staticmethod
    def __fun(x):
        return (x[0]**2 + x[1] - 11) ** 2 + (x[0] + x[1]**2 - 7)**2

    def __centroid(self, xl, xg, xh):
        fxl, fxg, fxh = self.__fun(xl), self.__fun(xg), self.__fun(xh)
        if fxl > fxg:
            xl, xg = xg, xl
            fxl, fxg = fxg, fxl
        if fxl > fxh:
            xl, xh = xh, xl
            fxl, fxh = fxh, fxl
        if fxg > fxh:
            xg, xh = xh, xg
            fxg, fxh = fxh, fxg

        # centroid
        return xl, xg, xh, (xl + xg)/2

    def __quantity(self, xl, xg, xh, xc):
        fxc = self.__fun(xc)
        res = ((self.__fun(xl) - fxc)**2 + (self.__fun(xg) - fxc)**2 + (self.__fun(xh) - fxc)**2)/3
        return res**0.5

    def SimplexSearchMethod(self, gama=1.5, beta=0.5):
        # xl best point, xg second-worst point, xh worst point
        xl, xg, xh = np.array([0, 0]), np.array([2, 0]), np.array([1, 1])

        i = 1
        data = dict()
        while True:
            # centroid
            xl, xg, xh, xc = self.__centroid(xl, xg, xh)
            # reflected point
            xr = 2 * xc - xh

            x_new = xr
            if self.__fun(xr) < self.__fun(xl):
                x_new = (1+gama)*xc - gama*xh   # expansion
            elif self.__fun(xr) >= self.__fun(xh):
                x_new = (1-beta)*xc + beta*xh   # contraction
            elif self.__fun(xg) < self.__fun(xr) < self.__fun(xh):
                x_new = (1+beta)*xc - beta*xh   # contraction
            xh = x_new

            data[i] = self.__quantity(xl, xg, xh, xc)
            if self.__quantity(xl, xg, xh, xc) < 10**(-3):
                x, y = zip(*data.items())
                plt.plot(x, y)
                plt.title('Simplex Search Method')
                plt.xlabel('iteration')
                plt.ylabel('converge')
                plt.show()
                break
            i += 1

    def __line_search(self, x, s):
        # set the initial step size, step size reduction factor and the tolerance for step size
        alpha, beta, tol = 1.0, 0.5, 1e-4
        fx = self.__fun(x)
        while True:
            x_new = x + alpha*s
            f_new = self.__fun(x_new)
            if f_new < fx:
                return x_new, f_new
            alpha *= beta
            if alpha < tol:
                return x, fx

    def PowellConjugateMethod(self, maxiter=1000, tol=1e-6):
        x = np.array([0, 4])
        n = x.shape[0]
        d = np.eye(n)
        for _ in range(maxiter):
            fx = self.__fun(x)
            # loop for the direction
            for j in range(n):
                s = d[:, j]
                # find the minimum along the direction s
                x_new, f_new = self.__line_search(x, s)
                if abs(f_new - fx) < tol:
                    return x_new
                x = x_new
                # update the conjugate direction
                if j < n-1:
                    d[:, j] = x_new - x
                    d[:, j+1] = s - d[:, j]
                else:
                    d[:, n-1] = s
        return x


if __name__ == "__main__":
    dsm = DirectSearchMethods()
    dsm.SimplexSearchMethod()
    # print(dsm.PowellConjugateMethod())
