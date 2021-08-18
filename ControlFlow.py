#if
print("if statement")
h=60
n=int(input("Enter number: "))
if h>m:
    print(h,"is greater than",m)

#if else
print("if else statement ")
h=90
if h>m:
    print(h,"is greater than",m)
else:
    print(h,"is smaller than",m)

#elif
print("elif statement ")
m=int(input("Enter number: "))
if m>0 :
    print(m,"is a positive number")
elif m==0:
        print("Number is zero")
else:
    print(m,"is a negative number")

#for loop
print("For Loop ")
list=[1,2,3,4,5,6,7,8,9]
sum=0
for num in list:
    sum=sum+num
    print("sum:",sum)

#while loop
print("While loop")
i = 1
while i < 6:
  print(i)
  i += 1

#Pass
print("Pass statement ")
if 10>5:
    pass

#Break
print("Break statement ")
for h in "industrial training":
    if h=='m':
        break
    print(h)

#Continue
print("Continue statement ")
for h in "Types of Loops":
    if h=='m':
        continue
    print(a) 