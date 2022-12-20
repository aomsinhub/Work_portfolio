money = int(input())
bill = 0

while money >= 100 :
    money = money-100
    bill = bill+1

print(bill)