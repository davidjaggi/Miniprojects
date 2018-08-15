# Test Case 1:
# balance = 3329
# annualInterestRate = 0.2


# Test Case 2:
# balance = 4773
# annualInterestRate = 0.2

# Test Case 3:
# balance = 3926
# annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
initialBalance = balance
month = 0
minimumPayment = 0

def calculator(month,balance,minimumPayment,monthlyInterestRate):
    while month < 12:
        unpaidBalance = balance - minimumPayment
        balance = unpaidBalance + (monthlyInterestRate*unpaidBalance)
        month += 1
    return balance

while calculator(month,balance,minimumPayment,monthlyInterestRate) > 0:
    balance = initialBalance
    minimumPayment += 10
    month = 0
    calculator(month,balance,minimumPayment,monthlyInterestRate)

print(f'Lowest Payment: {minimumPayment}')
