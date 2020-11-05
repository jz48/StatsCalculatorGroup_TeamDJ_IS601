from Calc import Calculator
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
            num2 = p * q
            num3 = e * e
            num4 = num1 * num2
            self.result = round(num4 / num3)
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

            num1 = p * q
            num2 = za2 / e
            num3 = num2 * num2
            result = int(num1 * num3)
            return result

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

            n = len(data)
            stand_dev = self.standard_deviation([a, b, c, d, e])
            sqr_n = round(self.root(n), 2)
            value1 = stand_dev / sqr_n
            z = int(1.96)
            result = round((value1 * z), 1)
            return result

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

            n = len(data)
            z = int(1.96)
            x = self.mean([a, b, c, d, e])
            s = self.standard_deviation([a, b, c, d, e])

            num1 = self.root(n)
            num2 = s / num1
            num3 = z * num2
            result = round((x - num3), 2)
            return result

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



