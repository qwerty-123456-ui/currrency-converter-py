with open('currencyData.txt') as f:
    lines=f.readlines()

currencyDict={}

for line in lines:
    parsed=line.split('\t')
    currencyDict[parsed[0]]=parsed[1]

# print(currencyDict)

amount=float(input("Enter the amount \n"))

print("Enter the name of currency ? (Available options) :\n")
[print(item) for item in currencyDict.keys()]
currency = input("Please enter one of these values : \n ")
print(f"{amount}INR is equal to {amount*float(currencyDict[currency])} {currency}")