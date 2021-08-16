#Find ASCII Value of a character 'X' and 'x'
c = 'x'
print("The ASCII value of '" + c + "' is", ord(c))


#Python program to find the quotient and remainder  
h=7
m=2
q=h/m
print("quotient :", int(q))
r=h%m
print("remainder :",r)


#Python program to swap two variables
x = 5
y = 10
temp=x
x=y
y=temp
print("\n value of x :",x)
print("\n value of y :",y)


#Python program to check if the input number is odd or even
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % l)
elif l == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % l) 
    

#Write programm to calculate monthly simple intrest and compound intrest(5%/Month) on amount - 161258/-

    p=161258
    t=30
    r=5
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
      
    si = (p * t * r)/100
      
    print('The Simple Interest is', si)


#Program to calculate GST i.e. 18% on base price 34900/-

    baseprice = 34900
    GST =0.18 * baseprice
    print("GST =",GST)


#Program to generate equated monthly instalments (EMI)(intrest 5%/Month) of 3 year and 5 year of amount 161258/-

    a=161258
    #instalments for 3 years
    e3=a/36
    #instalments for 5 years
    e5=a/60
    #instalments for 3 years with 5% intrest
    emi=e3+(0.05*e3)
    #instalments for 5 years with 5% intrest
    emi=e5+(0.05*e5)
     print("EMI for 3 years with 5% intrest",emi)
     
     print("EMI for 5 years with 5% intrest",emi)

     







