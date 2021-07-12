'''yes value of a dictionary key can be updated. 
syntax:
dictionaryname[keyname]=new/updated value. I have provided the code below in the dictionary methods'''
#list methods
l=[23,2,67,5,8]
l.clear()
l.append(21)
l.append(22)
print("after appending 2 values: ",l)
l1=l.copy()
print("after copying: ", l1)
print("how many 21's are there in the list? ",l.count(21))
l.extend([24,68,9,8])
print("After adding another list to the previous list: ",l)
print("68 is located at: ",l.index(68))
l.insert(10,2)
l.pop(5)
l.remove(2)
l.sort()
l.reverse()
print("finally we got our list as: ",l)
print("NEXT WE SHALL SEE THE TUPLE METHODS!\n")


#tuple methods
t=(1,2,3,4,5,5,4)
print("5 is repeated {} times".format(t.count(5)))
print("3 is at the {} position".format(t.index(3)))
print("NEXT WE SHALL GO FOR METHODS OF DICTIONARIES\n")


#dictionary methods
d={"name":"paushi","course":"python","mark":100}
print("\nthe list of dict values are: ",d.values())
d1={"other courses":"c"}
d.update(d1)
print("after adding other courses: ",d)
print("dict values as tuples is: ",d.items())
print("value of a key can be updated as follows!")
d["name"]="Paushigaa S"
print(d)
print("\n")


#a simple calculator
n1=int(input("ENTER THE FIRST NUMBER: "))
n2=int(input("ENTER THE SECOND NUMBER: "))
choice=input("what arithmetical calculation do you need to perform? (+,-,*,/,//,**,%)  ")
if choice=="+":
    print("added: ",n1+n2)
elif choice=="-":
    print("subtracted: ",n1-n2)
elif choice=="*":
    print("multiplied: ",n1*n2)
elif choice=="/":
    print("exact division is: ",n1/n2)
elif choice=="//":
    print("rounded off as: ",n1//n2)
elif choice=="**":
    print("power value is",n1**n2)
elif choice=="%":
    print("reminder is: ",n1%n2)
else:
    print("enter the correct choice from the list given above")
