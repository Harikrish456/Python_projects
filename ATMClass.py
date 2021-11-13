class ATM(object):
     def __init__(self, cardNumber, pinNumber):
         self.cardNumber = cardNumber
         self.pinNumber = pinNumber
     
     def CashWithdrawl(self):
        print('Card number:', self.cardNumber, 'is being validated')
        print('Pin number:', self.pinNumber, 'is being verified')
        print('Process initiated..')
        print('Withdrawal successful')
     
     def BalanceEnquiry(self):
       print('Your card number:', self.cardNumber, 'is being sent to our servers and your pin number:', self.pinNumber, 'is verified')
       print('This is your balance: - ')

     def Help(self):
         print('These are the commands you can perform in this atm: ')
         print('CashWithdrawl, BalanceEnquiry, MoneyTransfer')
    
     def MoneyTransfer(self, receiver, amount):
         print(amount, 'is being transfered to the', receiver)
         print('Money transfered successfully!')

atm = ATM(54567, 1234)
print('The following numbers are matched with a function, please enter the number you would like:')
print('1 is CashWithdrawal, 2 is Balance Enquiry, 3 is MoneyTransfer and 4 is Help')

inputValue = int(input('Enter your number to start a bank process: '))
print('You have chosen', inputValue)

if inputValue == 1:
    atm.CashWithdrawl()

if inputValue == 2:
    atm.BalanceEnquiry()

if inputValue == 3:
    atm.MoneyTransfer('Dad', 20000)

if inputValue == 4:
    atm.Help()