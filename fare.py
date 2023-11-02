distance=int(input("Enter the distance:"))
if 1<=distance<=50:
    charge1=distance*8
    print(charge1, "is the fare")
elif 51<=distance<=100:
    charge2=distance*10
    print(charge2,"is the fare")
else:
    charge3=distance*12
    print(charge3,"is the fare")
    
