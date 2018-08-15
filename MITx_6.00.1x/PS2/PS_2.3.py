# Test Case 1:
balance = 320000
annualInterestRate = 0.2

# Test Case 2:
# balance = 999999
# annualInterestRate = 0.18

initialBalance = balance
monthlyInterestRate = annualInterestRate / 12.0
lowerBound = balance / 12.0
upperBound = (balance * ((1.0 + monthlyInterestRate)**12))/12.0
epsilon = 0.01
minimumPayment = (upperBound + lowerBound)/2.0
month = 0

def claculator(month,balance,minimumPayment,monthlyInterestRate):
    while month < 12:
        unpaidBalance = balance - minimumPayment
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        month += 1
    return balance

while abs(balance) >= epsilon:
    balance = initialBalance
    month = 0
    balance = claculator(month,balance,minimumPayment,monthlyInterestRate)
    if balance > 0:
        lowerBound = minimumPayment
    else:
        upperBound = minimumPayment
    minimumPayment = (upperBound + lowerBound) / 2.0

minimumPayment = round(minimumPayment,2)
print(f'Lowest Payment: {minimumPayment}')