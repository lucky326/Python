Name=[]
Roll_no=[]
Marks1=[]
Marks2=[]

    
def Accept():
    N=input("\nEnter Students Details\n\tName: ")
    S=int(input("\tRoll_Number: "))
    M1=int(input("\tMarks1: "))
    M2=int(input("\tMarks2: "))

    Name.append(N)
    Roll_no.append(S)
    Marks1.append(M1)
    Marks2.append(M2)
    return

def Display():
    for i in range(len(Name)):
        print(Name[i],' ',Roll_no[i],' ',Marks1[i],' ',Marks2[i],'\n')
        return
    
def Search():
    S=int(input("\nEnter the Roll_Number to search: "))
    for i in range(len(Name)):
        if S==Roll_no[i]:
            print(Name[i],' ',Roll_no[i],' ',Marks1[i],' ',Marks2[i],'\n')
    return

def Delete():
    S=int(input("\nEnter the Roll_Number to Delete: "))
    for i in range(len(Name)):
        if S==Roll_no[i]:
            Name.pop(i)
            Roll_no.pop(i)
            Marks1.pop(i)
            Marks2.pop(i)
            print("\nThis student details are deleted")
    return

while True:
    ch=int(input("\nplease enter your choice\n1:Accept\n2:Display\n3:Search\n4:delete\n5:Exit\n"))
    if ch==1: Accept()
    elif ch==2: Display()
    elif ch==3: Search()
    elif ch==4: Delete()
    else:
        print('\nExiting...')
        break