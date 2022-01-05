class Atm(object):
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    
    def CashWithdawal(self):
        print('Cash Withdrawn')
    
    def BalanceEnquiry(self):
        print('You have 5000 rupees balance')
    
    def Savings(self):
        print('You have saved 10000 rupees')

card1 = Atm('123456789', '1234')
print(card1.cardNumber)
print(card1.CashWithdawal())
print(card1.BalanceEnquiry())
print(card1.Savings())