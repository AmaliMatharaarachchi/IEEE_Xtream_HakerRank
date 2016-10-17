num1=raw_input()
while(num1 != "END"):
    count=0
    while(num1!= "break"):
        count=count+1
        temp= len(num1)
        
        num2= str(temp)
        
        if (num2==num1):
            num1="break"
        else:
            num1=num2
    print (count)
    num1=raw_input()

