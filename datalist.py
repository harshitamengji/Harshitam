#declare list type which carry 10 elements
A= [a,b,c,d,e,f,g,h,i,j]
print("List A :",A[:])


#extract index number 2 to 5
print("List A :2 to 5",A[2:6])


#print list element reverse
print("List A in reverse:",A[::-1])


#using append, insert add elemenent in list

#Append
A.append('Alphabets')
print(" List A after Appending  :",A[:])

#insert
A.insert(3,'k')
print(" List A after inserting  :",A[:])

#Pop element
A.pop(1)
print(" List A after poping :",A[:])

#Remove
A.remove('e')
print(" List A after removing  :",A[:])

#delete
del A[0]
print(" List A after deleting  :",A[:])

#Clear List
A.clear()
print(" List A after clearing  :",A[:])


