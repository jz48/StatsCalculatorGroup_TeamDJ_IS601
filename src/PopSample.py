from .Calc import Calculator


class PopulationSample(Calculator):
    def __init__(self):
        super().__init__()

def cochran(z, p, q, e):
    try:
        z = float(z)
        p = float(p)
        q = float(q)
        e = float(e)

        num1 = z * z
        num2 = p * q
        num3 = e * e
        num4 = num1 * num2
        result = round(num4 / num3)
        return result

    except ZeroDivisionError:
        print('Error!  Cannot divide by 0')
    except ValueError:
        print('Error! Invalid data inputs')

# Z,p,q,e,Sample
# 1.96,0.5,0.5,0.05,384

# num1 = 3.8416
# num2 = 0.25
# num3 = 0.0025
# num4 = 0.9604
# return = 384.16


def find_sample_size(p, q, za2, e):
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