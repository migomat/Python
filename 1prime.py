
num_test=1
stop_key=1
print('test print')
flag=1

while num_test<1000000:
    flag = 1
    num_test=num_test+2
    
    for i in range(2,(num_test//2)+1):
        if(num_test%i == 0):
            #print('%d =i' %i)
            #print('%d is not a prime number' %num_test)
            flag = 0
            break
        
    if(flag==1):
        print('%d is a prime number' %num_test)
            
    #input("Press Enter to continue...")            

