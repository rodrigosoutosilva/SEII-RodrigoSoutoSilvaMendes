a = 12
b = 2
c = 98
d = 21
e = 10
f = 0
g = 7

x = e

if x == (a - b):
    print(x)

elif x == d:
    print(a+g)

elif x == f:
    print('zero')

else:
    print('ok')


if x%2 == 0 and x != 0:
    print('PAR')

else:
    print('NAO PAR')

if x >= 10 or x == 0:
    print('Dez ou Zero')

flag = False

if flag == False:
    print('N A O')

aa = [1,2,3]
bb = [1,2,3]

print(aa == bb)
print(aa is bb)

print(id(aa))
print(id(bb))

aa = bb

print(id(aa))
print(id(bb)) 

k = a < b

if k:
    print('V')
else:
    print('F')
