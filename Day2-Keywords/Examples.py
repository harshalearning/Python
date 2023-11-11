x=100 #global variable

def my_function():
    y =20 #local variable
    print(x) #100
    print(y) #20

def sec_fun():
    print(x) #100
    print(y) #error brcause y is local variable and cannot be used inside another function
    