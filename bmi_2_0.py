#!/usr/bin/env python3
#user wight input height formula weight/height*height then if else  if data is <= 18.5 under weight else if a 

weight=float(input("What's your weight?\n"))
height=float(input("What's your height?\n")) 
#print(type(height))
total_bmi=round(weight/height**2)
#print(total_bmi)

if total_bmi<18.5:
	print(f"Your bmi is {total_bmi}.You are underwieght")
elif total_bmi<25:
	print(f"Your bmi is {total_bmi}.volia you have normal bmi")
elif total_bmi<30:
	print(f"Your bmi is {total_bmi}.You are slightly overwieght")
elif total_bmi<35:
	print(f"Your bmi is {total_bmi}.You are obese")
else:
	print("You are clinically obese.")