nums = [1,2,3,4,5,6,7,8,9,10]

for num in nums:
    print(num)

print('\n')

for num in nums:
    if num == 4:
        print('Achou!')
        break
    print(num)

print('\n')

for num in nums:
    if num == 5:
        print('Achou!')
        continue
    print(num)

print('\n')

for num in nums:
    for letra in 'abcd':
        print(num, letra)

print('\n')

for i in range(10):
    print(i)

print('\n')

for ii in range(1, 11):
    print(ii)

print('\n')

x = 0

while x < 12:
    
    if x > 10:
        break

    print(x)
    x += 1

print('\n')

