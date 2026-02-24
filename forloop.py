Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
for i in range(1,6):
    print(i)

    
1
2
3
4
5
for i in range(4):
    print("atmiya")

    
atmiya
atmiya
atmiya
atmiya
for i in range(1,12):
    print(i)

    
1
2
3
4
5
6
7
8
9
10
11
for i in range(1,21):
    if i%2==0:
        print(i)

        
2
4
6
8
10
12
14
16
18
20
for i in range(1,21):
    if i%2!=0:
        print(i)

        
1
3
5
7
9
11
13
15
17
19
for i in range(1,11):
    print("5 x",i,"=",5*i)

    
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
>>> name="atmiya"
>>> for letter in name:
...     print(letter)
... 
...     
a
t
m
i
y
a
>>> for i in range(1,6):
...     total=total+i
...     print("sum is:",total)
... 
...     
Traceback (most recent call last):
  File "<pyshell#28>", line 2, in <module>
    total=total+i
NameError: name 'total' is not defined
>>> numbers=[10,20,30,40]
>>> for n in numbers:
...     print(n)
... 
...     
10
20
30
40
>>> for i in range(1,6):
...     total=total+i
...     print("sum is:",i)
... 
...     
Traceback (most recent call last):
  File "<pyshell#36>", line 2, in <module>
    total=total+i
NameError: name 'total' is not defined
