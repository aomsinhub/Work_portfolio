print ("ข้อ 1")
number = 1
r = 1
while r <= 10 :
    if number % 5 == 0 :
        print (number)
        r += 1
    number += 1 
#------------------------------------
print ("ข้อ 2")
number2 = int(input("ใส่แม่สูตรคูณ : "))
print ("สูตรคูณแม่",number2)
for r2 in range (1,13) :
    print (number2,"X",r2,"=",number2*r2)