aluno = {'nome': 'Jao', 'idade': 25, 'cursos': ['Mat','Por']}

print(aluno['cursos'])
print(aluno.get('nome'))
print(aluno.get('fone','Nao encontrado'))

aluno['fone'] = '34125544'
print(aluno.get('fone','Nao encontrado'))

aluno.update({'nome': 'Jane', 'idade': 21, 'cursos': ['Fis','Qui'], 'fone': '34126987'})

idade = aluno.pop('idade')

print(idade)

print(aluno.values())
print(aluno.items())