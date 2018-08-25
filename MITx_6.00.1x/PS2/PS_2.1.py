# Test Case 1 
# balance = 42
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

# Test Case 2
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


month = 0
totalPayment = 0
monthlyInterestRate = annualInterestRate / 12.0

while month < 12:
    minimumMonthlyPayment = monthlyPaymentRate * balance
    unpaidBalance = balance - minimumMonthlyPayment
    totalPayment += minimumMonthlyPayment
    balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
    month += 1

print('Remaining balance: '+str(round(balance,2)))