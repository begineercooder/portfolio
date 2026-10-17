
ct_alunos=0
ct_aprovados=0
ct_reprovados=0
notasAlunosTtl=0
while True:
    notasAlunos=float(input("Digite a nota de um aluno ou -1 para sair: "))

    if notasAlunos==-1:
        break
    if notasAlunos>=5:
        ct_aprovados=ct_aprovados+1
    if notasAlunos< 5:
            ct_reprovados = ct_reprovados + 1

    notasAlunosTtl = notasAlunosTtl + notasAlunos
    ct_alunos=ct_aprovados+ct_reprovados
    media_alunos=notasAlunosTtl/ct_alunos
print(ct_alunos,' alunos fizeram a prova, do qual ',ct_aprovados,'foram aprovados e ',ct_reprovados,'foram reprovados.\n A media da turma é ',media_alunos)