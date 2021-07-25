

try:
    f = open('curruptfile.txt')
except IOError as e:
    print('Primeiro')
except Exception as e:
    print('Segudno')
else:
    print(f.read())
    f.close()
finally:
    print("Execurando")

print('Fim')