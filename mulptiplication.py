n=int(input("enter the range"))
for i in range(n):
    print("multiplication table of :",i)
    for j in range(1,11):
        print(str(j)+ " x "+str(i)+ " = " + str(j*i))


