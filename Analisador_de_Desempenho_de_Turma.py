import numpy as np

try:
    students = int(input("Quantos estudantes realizaram a prova ?: "))
    exams = int(input("Quantas provas diferentes foram produzidas ?: "))
    while students <= 0:
        print("Número de estudantes inválido, apenas maiores que zero, digite novamente: ")
        students = int(input("Quantos estudantes realizaram a prova ?: "))
    while exams <= 0:
        print("Número de provas inválido, apenas maiores que zero, digite novamente: ")
        exams = int(input("Quantas provas diferentes foram produzidas ?: "))

    M = np.zeros((students,exams))

    for i in range(students):
        for j in range(exams):
            grade = int(input(f"Quais foram as notas do Aluno {i+1} ?: (Digite uma a uma)"))
            if grade >= 0:
                M[i][j] = grade
            else:
                print("Apenas valores maiores ou iguais a zero.")

    med = np.mean(M, axis = 1)

    for i in range(students):
        medS = med[i]

        if medS >= 7:
            situation = "Aprovado"
        elif 4 < medS < 7:
            situation = "Exame Final"
        else:
            situation = "Reprovado"

        print(f"Aluno {i+1} - Média = {medS:.1f} - Situação Acadêmica = {situation}")

    medG = np.mean(med)

    print(f"Média geral da turma = {medG:.1f}")
except ValueError:
    print("Estudantes ou provas em formato inválido, apenas números inteiros")