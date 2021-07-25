li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li)

print('Sorted Variable:\t', s_li)
print('Original Variable:\t', li)

s_li = sorted(li, reverse=True)

print('Sorted Variable:\t', s_li)
print('Original Variable:\t', li)

tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup)
print('Tubple\t', s_tup)

di = {'nome':'Rodrigo', 'idade':'26'}
s_di = sorted(di)
print('Dict\t',s_di)

li = [-6,-5,-4,1,2,3]
s_li = sorted(li,key=abs)
print('Abs\t', s_li)