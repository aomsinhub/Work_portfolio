with open("stdthk.txt",'w') as x:
    for r in range (1,4) :
        name = input("ใส่ชื่อ : ")
        c = input("ใส่ชั้น : ")
        n = input("ใส่เลขที่ : ")
        p = input("ใส่เบอร์มือถือ : ")
        print("*"*30)
        x.write(name+'/'+c+'/'+n+'/'+p+"\n")