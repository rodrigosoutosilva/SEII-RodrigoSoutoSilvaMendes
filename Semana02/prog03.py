cores = ['azul','amarelo','vermelho','rosa']

print(len(cores))
print(cores)
print(cores[0])
print(cores[-1])
print(cores[0:2])
print(cores[:2])
print(cores[1:])

cores.append('preto')
print(cores)

cores.insert(0, 'branco')

cores2 = ['roxo','lilas','verde']

cores.extend(cores2)

print(cores)

cores.remove('rosa')
x = cores.pop()

print(cores)

print(x)

print(cores.reverse)

cores.sort()

print(cores)

nums = [7, 8 , 9 , 12 , 15 , 851 , 2 , 0 , 6 , 150, 1]
print(nums)

snums = sorted(nums)

print(snums)
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
print(sum(nums))

print(cores.index('azul'))
print('Cinza' in cores)

for cor in cores:
    print(cor)


print('\n\n')

for cor in enumerate(cores):
    print(cor)

print('\n\n')

for cor in enumerate(cores,start=3):
    print(cor)    

lista_cores = ','.join(cores)
print(lista_cores)
nlistac = lista_cores.split(',')
print(nlistac)

rgb = ('vermelho','verde','azul')
print(rgb)
nrgb = rgb
print(rgb)
print(nrgb)

orgb = ['v','vd','a']
srgb = {'verm','verd','az','az'}
xrgb = {'red','az','green'}

print(orgb)
print(srgb)

print(srgb.intersection(xrgb))
print(srgb.difference(xrgb))

