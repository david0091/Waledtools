class calcu:
    def add():
        x = int(input ("Enter a Number :: "))
        y = int(input("Enter a Number ;: "))
        c = x + y
        print("is " ,c)

    def suptra():
        x = input ("Enter a Number :: ")
        y = input("Enter a Number ;: ")
        c = x - y
        print("is " ,c)
        
    def multi():
        x = int(input ("Enter a Number :: "))
        y = int(input("Enter a Number ;: "))
        c = x  * y
        print("is " ,c)

    def divi():
        x = int(input ("Enter a Number :: "))
        y = int(input("Enter a Number ;: "))
        c = x / y
        print("is " ,c)

   
def cal():
    x = str(input("Enter a option "))
    if x == '+':
        calcu.add()
    elif x == '-':
        calcu.suptra()
    elif x =='*':
        calcu.multi()
    elif x =='/':
        calcu.divi()
    else:
        print("Fuck of Idon't give a sheet D)")

cal()

