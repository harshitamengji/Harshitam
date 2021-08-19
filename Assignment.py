#1
def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('Python Skills'))



#2
print("2nd Answer")
x="16-03-2003"

print("Printing only year from string",x[6:])


#3
print("3rd Answer")
e1=1100
e2=500
e3=0
avg=1000
totalsalaryof3emp=1000*3
e3=totalsalaryof3emp-e1-e2
print("Salary of third employee is ",e3)


#4
print("4th Answer")
from fractions import Fraction
percent=30
print ("Conversion of 30 percent into fraction is",Fraction(30,100))




#5
print("5th Answer")
trainlen = 340
tunnellen = 160
total = trainlen + tunnellen
speed = 45
mps = 5/18
time = total / (45 * mps)
print ("Total time taken by train to cross the tunnel is: ",time) 




    
