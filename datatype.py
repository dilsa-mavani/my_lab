Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x="hello world"
print(x)
hello world
x=20
print(x)
20
x=20.5 #float
print(x)
20.5
x=1j #complex
print(x)
1j
x=["apple","banana","cherry"] #list
print(x)
['apple', 'banana', 'cherry']
x=["apple","banana","cherry"]
print(x)
['apple', 'banana', 'cherry']
x=range(6) #range
print(x)
range(0, 6)
x={"name": "john" ,"age":36}

3
x={"name" : "john","age":"36"} #dict
print(x)
{'name': 'john', 'age': '36'}
x={"aple","banana","cheery"} #set
print(x)
{'banana', 'aple', 'cheery'}
x=frozenset({"apple","banana","cheery"}) #frozenset
print(x)
frozenset({'banana', 'apple', 'cheery'})
x=true #bool
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    x=true #bool
NameError: name 'true' is not defined. Did you mean: 'True'?

x='true' #bool
print(x)
true
x=b"hello"  #bytypes
print(x)
b'hello'
x=byterray(8)  #byterray
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    x=byterray(8)  #byterray
NameError: name 'byterray' is not defined. Did you mean: 'bytearray'?
x=True
print(x)
True
x=Memoryview(bytes(5))
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    x=Memoryview(bytes(5))
NameError: name 'Memoryview' is not defined. Did you mean: 'memoryview'?
x=memoryview(bytes(5))
print(x)
<memory at 0x000001BD08B33D00>
x=none  #nonetype
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    x=none  #nonetype
NameError: name 'none' is not defined. Did you mean: 'None'?
x=None
print(x)
None
