
with open('teste.txt','r') as f:
    f_contents = f.read()

print(f.contents)

size_to_read = 100
f_contents = f.read(size_to_read)
print(f_contents, end='')

while len(f_contents) > 0:
    print(f_contents,end='*')

