
def porc(value, total):
    ans = (value * 100) / total
    return ans

invoice = {"SP": 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES": 27165.48, "Outros": 19849.53}

total = 0
for value in invoice.values():
    total += value

for key , value in invoice.items():
    print(f"A porcentagem que o estado de {key} representa no faturamento é: {porc(value, total):.2f}%")
