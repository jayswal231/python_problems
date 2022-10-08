"""
#1. TO CHECK PELINDROM NUMBER
number=int(input("enter thr number: "))
copy=number
reverse=0
while number !=0:
    remainder=number%10
    reverse= reverse*10 + remainder
    number= number//10

if copy == reverse:
    print("This number is pelindrom")
else:
    print("This number is not pelindrom")
   

#2. TO CHECK PRIME NUMBER
number=int(input("enter the number: "))
if number>1:
    for i in range(2,number//2):
        if number % i ==0:
            print(number,"not prime")
            break
    else:
        print(number,"prime")
else:
    print("not prime")


#3. PRINT STRING 
str= input("enter the string: ")
for row in range(len(str)):
    for col in range(row+1):
        print(str[col], end=" ")
    print()


#4. TO CHECK REAPTED NUMBER IN LIST
lists=[1,2,2,3,2]
result=[]
for i in lists:
    if i not in result:
        result.append(i)
    else:
        print("the reapted num is:",i)
print("the final result is :",result)


#5. TO FIND FACTORIAL OF ANY NUMBER
num=int(input("enter the number: "))
fact=1
for i in range(1, num+1):
    fact=fact*i
print(fact)

#6. To find reverse number
num=int(input("enter the number: "))
reverse=0
while num!=0:
    remainder=num%10            
    reverse=reverse*10+remainder
    num=num//10
print(reverse)


#7. To find HCF and LCM of two number
def find_hcf(a,b):
    hcf=1
    for i in range(1, a+1):
        if a%i==0 and b%i==0:
            hcf=i
    return hcf
first_num=int(input("enter the first number: "))
second_num=int(input("enter the second number: "))
print("The HCF of: ",first_num,"and", second_num,"is :" ,find_hcf(first_num,second_num))

lcm=first_num*second_num / find_hcf(first_num,second_num)
print('The lcm of  %d and %d is %d' %(first_num,second_num,lcm))

#8. To count number
digit=1234123
count=0
while digit !=0:
    digit=digit//10
    count +=1
print(count)


#9. To check armstrong number
def count_num(n):
    count=0
    while n !=0:
        n=n//10
        count +=1
    print(count)
    return count
#count_num()

def check_arm(n):
    num=n
    sum=0
    p=count_num(n)
    while n !=0:
        rem=n%10
        sum=sum+rem**p
        n=n//10
    print(sum)
    if sum==num:         
        print("armstrong")
    else:
        print("not armstrong")
    return
number=int(input("enter the number: "))
check_arm(number)


#10. To check strong number
def fact(n):
    factorial=1
    for i in range(1,n+1):
        factorial *=i
#    print(factorial)
    return factorial
#fact(3)

def check_strong(n):
    sum=0
    num=n
    while n !=0:
        rem=n%10
        sum =sum+ fact(rem)
        n=n//10
 #   print(sum)
    if sum==num:
        print("strong number")
    else:
        print("not strong number")
    return
number=int(input("enter the number: "))
check_strong(number)


#11. To fibonancci series
def fib(n):
    a,b=0,1
    while a<n:
        print(a, end=', ')
        next_num=a+b
        a,b=b,next_num
max_num=int(input("enter the maxm number: "))
fib(max_num)


#12. To check perfect number
def perfect(num):
   
    n=num
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    if sum==n:
        print("perfect number")
    else:
        print("not perfect number")
    return
number=int(input("enter the number: "))
perfect(number)
"""
#13. To check triangular number
def triangular_num(a):
    num=a
    sum=0
    n=[]
    for i in range(1,num):
        n.append(i)
        sum=sum+i
        if num==sum:
            print(n)
            break
    if sum==num:
        print("triangular number")
    else:
        print("not triangular number")
number=int(input("enter the number: "))
triangular_num(number)
