#READ Binary
f=open("text.txt",'rb')
print(f.read())
f.close() 


#Write Binary
f=open("text.txt",'wb')
f.write("binary")
f.close() 


#Read
try:
        f=open("text.txt",'r',encoding="utf-8")
        for line in f:
            print(line,end='')
except:
        print("Operation Failed!!!!")

finally:
        f.close() 



#Read As Obj
try:
        f=open("text.txt",'r',encoding="utf-8")
        for line in f:
            print(line,end='')
except:
        print("Operation Failed!!!!")

finally:
        f.close() 




#Read with
with open("text.txt",'r',encoding='utf-8') as f:
     print(f.read())
     f.close() 



#Write as Obj
try:
    f=open("text.txt",'w',encoding="utf-8")

    f.write("With Object method ")
except:
    print("operation failed!!!")
finally:
     f=open("text.txt",'w',encoding="utf-8")
     f.close()



#text
Hey 
 How are you
 This is sample text


#Write
with open("text.txt",'w',encoding="utf-8")as f:
    f.write("Hey \n How are you")
    f.write("\n This is sample text")