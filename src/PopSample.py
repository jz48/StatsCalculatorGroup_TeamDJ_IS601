from StatsCalc import StatsCalculator


class PopulationSample(StatsCalculator):
    result = 0

    def __init__(self):
        super().__init__()

    def cochran(self, z, p, q, e):
        try:
            z = float(z)
            p = float(p)
            q = float(q)
            e = float(e)

            num1 = self.square(z)
            num2 = self.multiplication(p, q)
            num3 = self.square(e)
            num4 = self. multiplication(num1, num2)
            self.result = round(self.division(num3, num4))
        except ZeroDivisionError:
            print('Error!  Cannot divide by 0')
        except ValueError:
            print('Error! Invalid data inputs')

        return self.result

    def find_sample_size(self, p, q, za2, e):
        try:
            p = float(p)
            q = float(q)
            za2 = float(za2)
            e = float(e)

            num1 = self.multiplication(p, q)
            num2 = self.division(e, za2)
            num3 = self.square(num2)
            self.result = int(self.multiplication(num1, num3))


        except ZeroDivisionError:
            print('Error! Cannot divide by 0')
        except ValueError:
            print('Error! Invalid data entry')

        return self.result

    def margin(self, a, b, c, d, e):
        try:
            a = int(a)
            b = int(b)
            c = int(c)
            d = int(d)
            e = int(e)
            data = [a, b, c, d, e]

            n = len([data])
            num2 = self.standard_deviation([a, b, c, d, e])
            num3 = round(self.root(n), 2)
            value1 = self.division(num3, num2)
            z = int(1.96)
            value2 = round(self.multiplication(value1, z), 1)
            self.result = self.division(float(0.8947), value2)


        except ZeroDivisionError:
            print("Error! Cannot Divide by 0")
        except ValueError:
            print("Error! Invalid data inputs")
        return self.result

    def conf_int(self, a, b, c, d, e):
        try:
            a = int(a)
            b = int(b)
            c = int(c)
            d = int(d)
            e = int(e)
            data = [a, b, c, d, e]

            n = int(len(data) -1)
            z = int(1.96)
            x = self.mean([a, b, c, d, e])
            s = self.standard_deviation([a, b, c, d, e])

            num1 = self.root(n)
            num2 = self.division(num1, s)
            num3 = self.multiplication(z, num2)
            self.result = round(self.subtract(num3, x), 2)


        except ZeroDivisionError:
            print("Error! Cannot Divide by 0")
        except ValueError:
            print("Error! Invalid data inputs")
        return self.result





# Z,p,q,e,Sample
# 1.96,0.5,0.5,0.05,384

# num1 = 3.8416
# num2 = 0.25
# num3 = 0.0025
# num4 = 0.9604
# return = 384.16


if __name__ == '__main__':
    ps = PopulationSample()
    print('cochran: ', ps.cochran(1.96, 0.5, 0.5, 0.05))
    print('find sample size : ', ps.find_sample_size(0.41, 0.59, 1.96, 0.03))
    print('margin : ', ps.margin(10, 20, 30, 40, 50))
    print('conf int : ', ps.conf_int(175, 180, 210, 140, 170))



