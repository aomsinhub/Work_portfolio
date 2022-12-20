score = round(float(input("ใส่คะแนน : ")))
if score < 50 and score >= 0 :
    print ("ไม่ผ่าน")
elif score >= 50 and score < 55 :
    print ("1.0")
elif score >= 55 and score < 60 :
    print ("1.5")
elif score >= 60 and score < 65 :
    print ("2.0")
elif score >= 65 and score < 70 :
    print ("2.5")
elif score >= 70 and score < 75 :
    print ("3.0")
elif score >= 75 and score < 80 :
    print ("3.5")
else :
    print ("4.0")