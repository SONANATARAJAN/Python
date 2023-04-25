
#if statement
'''
n=int(input("Enter the number: "))
if n%2==0:
    print("this is even number")

'''


print("---------------------------------------------------")

#if else statement
'''
#vote eligible test

name= input("Enter your name :")
age = int(input("Enter your age: "))
if age>=18:
    print(name,"Your eligible for vote" )
else:
    print("not eligible for vote")

'''

print("---------------------------------------------------")


#elif statement

'''
membership seclection
days      fine
 0         No fine
 1-5        0.5
 5-17        1
 18-30       5
 >30        membership cancel
'''


days = int(input("enter the days :"))

if days==0:
    print("Good!, No fine")
elif days>=1 and days<=5 :
    print("Fine amount :", days*0.5)
elif days>=6 and days<=17 :
    print("Fine amount :" ,days*1)
elif days>=18 and days<=30:
    print("Fine amount :", days*5)
else:
    print("Your membership cancle ")
    



