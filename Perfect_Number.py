number=int(input('Enter A Number : '))
sum=0
for fact in range(1,number):
    if number%fact==0:
        sum=sum+fact
if number==sum:
    print('Perfect Number')
else:
     print('Not A Perfect Number')
    
