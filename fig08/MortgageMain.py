# Figure 8.11

from fig08_10 import Fixed
from fig08_10 import FixedWithPts
from fig08_10 import TwoRate


def compareMortgages(
    amt, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths
):
    totMonths = years * 12  # total month
    fixed1 = Fixed(amt, fixedRate, totMonths)  # amount, rate, months
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)  # amount, rate, months, pts
    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)

    morts = [fixed1, fixed2, twoRate]

    for m in range(totMonths):  # 複利算法
        for mort in morts:
            mort.makePayment()

    for m in morts:  # 會算出三種貸款的總付款金額
        print(m)
        print(" Total payments = $" + str(int(m.getTotalPaid())))


if __name__ == "__main__":
    compareMortgages(  # 輸入目前所有外生＋內生條件
        amt=200000,
        years=30,
        fixedRate=0.07,
        pts=3.25,
        ptsRate=0.05,
        varRate1=0.045,
        varRate2=0.095,
        varMonths=48,
    )
""" Output:
Fixed, 7.0%
 Total payments = $479017
Fixed, 5.0%, 3.25 points
 Total payments = $393011
4.5% for 48 months, then 9.5%
 Total payments = $551444 """
