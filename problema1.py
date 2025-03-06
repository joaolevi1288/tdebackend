N, H = map(int, input("Digite o número de brinquedos e a altura de Carlitos: ").split())

alturas_minimas = list(map(int, input("Digite as alturas mínimas de cada brinquedo: ").split()))

contagem = 0

for altura in alturas_minimas:
    if altura <= H:
        contagem += 1

print("Carlitos pode ir a", contagem, "brinquedos.")
