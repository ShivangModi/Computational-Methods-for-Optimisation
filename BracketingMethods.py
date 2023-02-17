class BracketingMethods:
    @staticmethod
    def __fun(x):
        return x ** 2 + 54 / x

    def ExhaustiveSearchMethod(self, a, b, n):
        step = (b - a) / n
        if a == 0:
            x1, fx1 = step, self.__fun(step)
        else:
            x1, fx1 = a, self.__fun(a)

        x2, fx2 = x1 + step, self.__fun(x1 + step)
        if fx2 > fx1:
            x1, x2 = x2, x1
            fx1, fx2 = fx2, fx1
            step = -step

        flag = True
        while True:
            x3, fx3 = x2 + step, self.__fun(x2 + step)
            if x3 > b:
                break
            if fx2 < fx3:
                print(f'f({x2})= {fx2}')
                print(f'Interval: [{x1}, {x3}]')
                print(f'Range: {2 * (b - a) / n}')
                flag = False
                break
            x1, fx1, x2, fx2 = x2, fx2, x3, fx3

        if flag:
            print(f'No minimum exist in [{a}, {b}] or boundary point ({a} or {b}) is minimum point.')

    def BoundingPhaseMethod(self, x0, step):
        # if abs(step) >= x0:
        #     x0 = abs(step) + 0.1
        k = 0
        a = x0 - step
        b = x0 + step
        fx0 = self.__fun(x0)
        fa = self.__fun(a)
        fb = self.__fun(b)

        if fa >= fx0 >= fb:
            print("Delta is positive(+ve).")
        elif fa <= fx0 <= fb:
            print("Delta is negative(-ve).")
        elif fa <= fx0 and fx0 >= fb:
            print("function is not uni-modal.")
            return
        elif fa >= fx0 and fx0 <= fb:
            print(f"Interval: [{a}, {b}]")
            print(f'f({x0})= {fx0}')
            return

        while True:
            k = k + 1
            a, x0 = x0, b
            b = x0 + pow(2, k) * step
            if self.__fun(b) >= self.__fun(x0):
                break

        print(f"Interval: [{a}, {b}]")
        print(f'f({a})= {fa}')
        print(f'f({x0})= {fx0}')
        print(f'f({b})= {fb}')

    def IntervalHalvingMethod(self, a, b):
        l0 = abs(b - a)
        xm = (a + b) / 2
        x1 = a + (l0 / 4)
        x2 = b - (l0 / 4)

        if self.__fun(x1) < self.__fun(xm):
            b, xm = xm, x1
        elif self.__fun(x2) < self.__fun(xm):
            a, xm = xm, x2
        else:
            a, b = x1, x2

        if abs(b - a) < 10 ** (-3):
            print(f"Interval: [{a}, {b}]")
            print(f'f({a})= {self.__fun(a)}')
            print(f'f({xm})= {self.__fun(xm)}')
            print(f'f({b})= {self.__fun(b)}')
        else:
            self.IntervalHalvingMethod(a, b)

    def __firstOrder(self, x):
        diff = (0.01 * abs(x)) if abs(x) > 0.01 else 0.0001
        return (self.__fun(x + diff) - self.__fun(x - diff)) / (2 * diff)

    def __secondOrder(self, x):
        diff = (0.01 * abs(x)) if abs(x) > 0.01 else 0.0001
        return (self.__fun(x + diff) - (2 * self.__fun(x)) + self.__fun(x - diff)) / (diff ** 2)

    def BisectionMethod(self, a, b):
        if self.__firstOrder(a) >= 0 >= self.__firstOrder(b):
            print("Change interval")
            return
        x1, x2 = a, b
        while True:
            z = (x1 + x2)/2
            fz = self.__firstOrder(z)
            print(f'x1={x1}, z={z}, f\'(z)={fz}, x2={x2}')
            if abs(fz) <= 10 ** (-3):
                print(f"Interval: [{x1}, {x2}]")
                print(f'f({x1})= {self.__fun(x1)}')
                print(f'f({z})= {self.__fun(z)}')
                print(f'f({x2})= {self.__fun(x2)}')
                return
            elif fz < 0:
                x1 = z
            elif fz > 0:
                x2 = z


if __name__ == "__main__":
    bm = BracketingMethods()
    # bm.ExhaustiveSearchMethod(0, 5, 10)
    # bm.BoundingPhaseMethod(0.6, 0.5)
    # bm.IntervalHalvingMethod(0, 5)
    bm.BisectionMethod(2, 5)
