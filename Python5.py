def menu():
    print("*"*10)
    print("* หาปริมาตร *")
    print("*"*10)
    print("1.สี่เหลี่ยมมุมฉาก")
    print("2.ลูกบาศก์")
    print("3.ทรงกลม")
    print("4.ทรงกระบอก")
    print("5.ออกจากโปรแกรม")
    print("*"*10)
def clear():
    print("\n"*4)
def shape1(ก,ย,ส):
    return ก*ย*ส
def shape2(ก):
    return ก**3
def shape3(ร):
    return 4/3*3.14*ร**3
def shape4(ร,ส):
    return 3.14*ส*ร**2
#โปรแกรม
menu()
INPUT = int(input("เลือกหัวข้อ : "))
while INPUT!=5:
    if INPUT == 1:
        ก = float(input("ความกว้าง : "))
        ย = float(input("ความยาม : "))
        ส = float(input("ความสูง : "))
        print("ปริมาตรสี่เหลี่ยมมุมฉาก =",shape1(ก,ย,ส))
    elif INPUT == 2:
        ก = float(input("ความกว้าง : "))
        print("ปริมาตรลูกบาศก์ =",shape2(ก))
    elif INPUT == 3:
        ร = float(input("รัศมี : "))
        print("ปริมาตรทรงกลม =",shape3(ร))
    elif INPUT == 4:
        ร = float(input("รัศมี : "))
        ส = float(input("ความสูง :"))
        print("ปริมาตรทรงกระบอก =",shape4(ร,ส))
    else :
        print("ไม่มีตัวเลือกนี้")
    clear()
    menu()
    INPUT = int(input("เลือกหัวข้อ : "))
else :
    print("ออกจากโปรแกรม")