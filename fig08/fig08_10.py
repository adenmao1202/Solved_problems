# Figure 8.10

from fig08_09 import findPayment
from fig08_09 import Mortgage


class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = "Fixed, " + str(round(r * 100, 2)) + "%"


class FixedWithPts(Mortgage):  # 頭金：先扣的錢
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan * (pts / 100)]
        self.legend = "Fixed, " + str(round(r * 100, 2)) + "%, " + str(pts) + " points"


class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r / 12
        self.legend = (
            str(teaserRate * 100)
            + "% for "
            + str(self.teaserMonths)
            + " months, then "
            + str(round(r * 100, 2))
            + "%"
        )

    def makePayment(self):  # overwrite 父類別(mortgage)中 makePayment的方法
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(
                self.outstanding[-1], self.rate, self.months - self.teaserMonths
            )
        Mortgage.makePayment(self)
