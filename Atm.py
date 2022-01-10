class atm(object):
    def __init__(self,card_number,pin_number):
        self.card_number=card_number
        self.pin_numebr=pin_number
    def CashWithDrawl(self):
        print("withdrawl")
    def Balanceinquiry(self):
        print("balance")
atm1 = atm("1234","3214")
atm1.Balanceinquiry()
atm1.CashWithDrawl()
