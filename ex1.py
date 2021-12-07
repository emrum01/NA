import math


class compPrec:

    def getNegativeMachinePrecision(self):
        d = 1
        n = -1
        d = 1-pow(2, n)
        while d != 1:
            n -= 1
            d = 1-pow(2, n)
        return pow(2, n)

    def getLargestNumber(self):

        r = 2
        eps = self.getNegativeMachinePrecision()
        d: float = 1 - r*eps

        # 値取得用のリスト
        list1 = []
        i = 0
        while not math.isinf(d):
            d = r*d
            list1.append(d)
            i += 1
        d = list1[i-2]
        return d


a = compPrec()
print("Floating-point machine parameters")
print("---------------------------------")
print("Negative machine precision = {}".format(a.getNegativeMachinePrecision()))
print('Largest number = {:.16g}'.format(a.getLargestNumber()))
