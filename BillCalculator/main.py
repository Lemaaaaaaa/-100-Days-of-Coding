print('Welcome to the tip calculator')
bill=float(input('What was the total bill'))
customer=float(input('How many people to split the bill'))
tip=float(input('What percentage would you like to give? 10,12 or 15?'))
bill_shared= (bill/customer)*(tip+100)/100
print(f"Each person should pay: {bill_shared}")
