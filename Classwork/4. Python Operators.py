#4. PythonOperators.py

#1.Arithmetic Operators
a=10
b=20
print("Addition(+):",a+b) #Addition(+): 30
print("Subtraction(-):",a-b) #Subtraction(-): -10
print("Multiplication(*):",a*b) #Multiplication(*): 200
print("Division(/):",a/b) #Division(/): 0.5
print("Floor Division(//):",a//b) #Floor Division(//): 0
print("Modulus(%):",a%b) #Modulus(%): 10
print("Modulus(%):",b%a) #Modulus(%): 0
print("Exponentiation(**):",a**b) #Exponentiation(**): 100000000000000000000

#2.Comparison Operators
print("Equal to(==):",a==b) #Equal to(==): False
print("Not equal to(!=):",a!=b) #Not equal to(!=): True
print("Greater than(>):",a>b) #Greater than(>): False
print("Less than(<):",a<b) #Less than(<): True
print("Greater than or equal to(>=):",a>=b) #Greater than or equal to(>=): False
print("Less than or equal to(<=):",a<=b) #Less than or equal to(<=): True

#3.Assignment Operators
a=10
print(a) #a=10
a+=20
print(a) #a=a+20->30
a-=10
print(a) #a=a-10->20
a*=3
print(a) #a=a*3->60
a/=2
print(a) #a=a/2->30.0
a//=2
print(a) #a=a//2->15.0
a**2
print(a) #a=a**2->15.0
a%=2
print(a) #a=a%2=->1.0

#4.Logical Operators
a=10
b=20
print(a>5 and b<25) #True(Both conditions are True)
print(a>20 and b<30) #False
print(a>5 or b<15) #True(Atleast one condition is True)
print(a>20 or b<10) #False
print(not(a>5)) #False(Reverses the True condition)
print(not(a<5)) #True(Reverses the False condition)

#5.Membership Operators
food=['pizza', 'burger', 'momos', 'chat']
print('burger' in food) #True
print('pasta' in food) #False

#6.Identity Operators
a=[1,2,3,4,5]
b=[1,2,3,4,5]
print(a==b) #True
print(a is b) #False(Different objects with same content)
c=a
print(c) #[1, 2, 3, 4, 5]
print(c is a) #True(Both refer to the same object)
print(b is not c) #True(Both are not same)

#7.Bitwise Opeartors
a=7
b=9
print(a&b) #output:1 (Binary: 0001->AND operation)
print(a|b) #output:15(Binary: 1111->OR operation)
print(a^b) #output:14(Binary: 1110->XOR operation)
print(~a)  #output:-8(Binary: Inverts bits of 7)
print(a<<1) #output:14(Binary: 1110->Shifts left by 1)
print(a>>1) #output:3(Binary: 0011->Shifts right by 1)