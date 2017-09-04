#آله حاسبة بسيطة
#تعريف الدوال 
def idn1(idn2, idn3):
	return idn2 + idn3 

def idn4(idn2 , idn3 ):
	return idn2 - idn3 

def idn5(idn2 , idn3 ):
	return idn2 * idn3 

def idn6(idn2 , idn3 ):
	return idn2 / idn3 

# اختيار العملية من قبل المستخدم
print  ("اختر العملية")
print  ("١ لعملية الجمع")
print  ("٢ لعملية الطرح")
print  ("٣ لعملية الضرب")
print  ("٤ لعملية القسمة")

idn7 = int(input("ادخل العملية المطلوبة (١/٢/٣/٤):  "))
if idn7  in range(1,5):
	idn8 = int(input(" ادخل العدد الاول: "))
	idn9 = int(input(" ادخل العدد الثاني: "))

	if idn7  == 1 :	        
		print (idn8 , "+", idn9 , "=" , idn1 (idn8 , idn9 ))
	elif idn7  == 2 :	        
		print (idn8 , "-", idn9 , "=" , idn4 (idn8 , idn9 ))
	elif idn7  == 3 :	        
		print (idn8 , "*", idn9 , "=" , idn5 (idn8 , idn9 ))
	elif idn7  == 4 :	        
		print (idn8 , "/", idn9 , "=" , idn6 (idn8 , idn9 ))
else :
	print("الاختيار المدخل غير صحيح")