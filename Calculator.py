from termcolor import colored
print ("Hello I am encod i am a calculator:-")
a=float(input("input no.1 (a): "))
b=float(input("input no.2 (b): "))
c=0
d = 0
e = 1
error = "errR;\n\t","'", c, "'", "is not an option!"
colorederror = colored (error, 'red')
while e == 1:
        e = 0
        c=int(input("options (c):\n1 for adding 2 for subtracting\n3 for multiplying 4 for dividing: "))
        if c == 1:       
                print ("the answer is... ")
                d = a+b
        elif c == 2:
                print ("the answer is... ")
                d = a-b   
        elif c == 3:
                print ("the answer is... ")
                d = a*b
        elif c == 4:
                print ("the answer is... ")
                d = a/b
        elif c > 4 or c < 1:
                print (colorederror) 
                e = 1      
if d > 0:
        print("Ans(d)= ", d)
print("a = ", a)
print("b = ", b)
print("c = ", c)
leave = input ("Press enter to exit")