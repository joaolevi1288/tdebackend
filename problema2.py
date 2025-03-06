C = int(input("Digite a capacidade da cabine: "))
A = int(input("Digite o número de alunos: "))

alunos_por_viagem = C - 1

viagens = (A + alunos_por_viagem - 1) // alunos_por_viagem

print("O número mínimo de viagens é:", viagens)
