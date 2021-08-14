name_a=input("What's your name?\n")
name_b=input("What's your name?\n")
combined_names=name_a+name_b
lower_names=combined_names.lower()


#print(name_a.lower())
t=lower_names.count('t')
r=lower_names.count('r')
u=lower_names.count('u')
e=lower_names.count('e')

first_digit=t+r+u+e

l=lower_names.count('l')
o=lower_names.count('o')
v=lower_names.count('v')
e=lower_names.count('e')
second_digit=l+o+v+e

score=int(str(first_digit)+str(second_digit))
print(score)

if score<10 or score>90:
	print(f"Your score is {score}, you go together like coke and mentos.")
elif score >=40 and score<=50:
	print(f"Your score is {score}, you are alright together")
else:
	print("I guess you dont have hahah shame on you are alone your freind has but you dont have ohhh what kind of person you are !!!!!!!!!!!!!!!!!!!!!!!!!!!!!,Wait a minute may be you both are not compatible together but i guess you should stay together do not  belive on this silly calc which compares with your name .So dont take the result seriously ,Have great day")
#l_int=int(l)
#o_int=int(o)
#v_int=int(v)
#e_int=int(e)
#true_str=t_int+r_int+u_int+e_int
#love_str=l_int+o_int+v_int+e_int
