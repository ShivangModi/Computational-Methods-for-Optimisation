class GradientMethod:
    @staticmethod
    def __fun(x):
        return x ** 2 + 54 / x

    def __firstOrder(self, x):
        diff = (0.01 * abs(x)) if abs(x) > 0.01 else 0.0001
        return (self.__fun(x + diff) - self.__fun(x - diff)) / (2 * diff)

    def __secondOrder(self, x):
        diff = (0.01 * abs(x)) if abs(x) > 0.01 else 0.0001
        return (self.__fun(x + diff) - (2 * self.__fun(x)) + self.__fun(x - diff)) / (diff ** 2)

    def NewtonRaphsonMethod(self, x=1):
        fo = self.__firstOrder(x)
        so = self.__secondOrder(x)
        new_x = x - fo/so
        # print(f'x={x}, f(x)={self.__fun(x)}, fo={fo}, so={so}')
        if abs(self.__firstOrder(new_x)) >= 10 ** (-3):
            self.NewtonRaphsonMethod(new_x)
        else:
            print(f'x={new_x}, f(x)={self.__fun(new_x)}, fo={self.__firstOrder(new_x)}, so={self.__secondOrder(new_x)}')

    def SecantMethod(self, a, b):
        if self.__firstOrder(a) >= 0 >= self.__firstOrder(b):
            print("Change interval")
            return
        while True:
            fx1 = self.__firstOrder(a)
            fx2 = self.__firstOrder(b)
            z = b - (fx2 * (b - a)) / (fx2 - fx1)
            fz = self.__firstOrder(z)
            # print(f'a={a}, z={z}, f\'(z)={fz}, b={b}')
            if abs(fz) < 10 ** (-3):
                print(f'x={z}, f(x)={self.__fun(z)}, fo={self.__firstOrder(z)}, so={self.__secondOrder(z)}')
                return
            elif fz < 0:
                a = z
            elif fz > 0:
                b = z


if __name__ == "__main__":
    gm = GradientMethod()
    gm.NewtonRaphsonMethod()
    gm.SecantMethod(2, 5)
