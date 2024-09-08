# Figure 8.9


def findPayment(loan, r, m):
    """Assumes:
     loan and r are floats, m an int
    Returns: the monthly payment for a mortgage of size
    loan(total): r --> rate
                 m --> months"""
    return loan * (
        (r * (1 + r) ** m) / ((1 + r) ** m - 1)
    )  # just an equation for monthly payment


class Mortgage(object):
    """Abstract class for building different kinds of mortgages"""

    def __init__(self, loan, annRate, months):
        """Assumes: 
        loan and annRate are floats
        months an int
        Creates a new mortgage of size loan, duration months, and
        annual rate annRate"""
        
        self.loan = loan  # 貸款的總金額（本金）
        self.rate = annRate / 12  # 將年利率轉換為月利率
        self.months = months  # 貸款的總月數
        self.paid = [0.0]  # 已支付金額的列表，初始為0.0
        self.outstanding = [loan]  # 尚未償還的貸款金額列表，初始為貸款總金額
        self.payment = findPayment(loan, self.rate, months)  # 計算每月還款額（呼叫上方定義的findPayment方法）
        self.legend = None  # 貸款的描述

    def makePayment(self):
        """Make a payment"""
        
        self.paid.append(self.payment)  # 將當前月的付款添加到已支付金額列表中
        reduction = self.payment - self.outstanding[-1] * self.rate  # 計算本金還款部分
        self.outstanding.append(self.outstanding[-1] - reduction)  # 更新尚未償還的貸款金額

    def getTotalPaid(self):
        """Return the total amount paid so far"""
        return sum(self.paid)  # 返回迄今為止的總付款額

    def __str__(self):
        return self.legend  # 返回貸款的描述

