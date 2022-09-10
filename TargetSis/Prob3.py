import json

def minVal(arr):
    ans = arr[0]
    ''' Aqui eu estou assumindo que o menor valor de faturamento também não pode ser os zeros dos finais
        de semana e feriados.
    '''
    for i in range(len(arr)):
        if arr[i] != 0 and arr[i] < ans:
            ans = arr[i]

    return ans

def maxVal(arr):
    ans = arr[0]

    for i in range(len(arr)):
        ans = max(ans, arr[i])
    
    return ans


def average(arr):
    ans = 0
    unavailable = 0

    for i in range(len(arr)):
        ans += arr[i]
        if arr[i] == 0:
            unavailable += 1

    ans = ans/ (len(arr) - unavailable)
    return ans

def upAverage(arr):
    ans = 0
    aver = average(arr)

    for i in range(len(arr)):
        if arr[i] > aver:
            ans += 1
    
    return ans


faturamento = [0] * 30

f = open('dados.json',)
data = json.load(f)

for i, value in enumerate(data):
    faturamento[i] = value["valor"]


print(f"O menor valor de faturamento desse mes foi: R$ {minVal(faturamento)}")
print(f"O maior valor de faturamento desse mes foi: R$ {maxVal(faturamento)}")
print(f"Nesse mes {upAverage(faturamento)} dias o valor de faturamento diario foi superior a media mensal")



