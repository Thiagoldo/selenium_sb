numero_dias = 30
greens_ao_dia = 15
porcentagem = 0.79
banca_inicial = 1270
banca_final = 1270

valor_final = 0.0

for i in range(numero_dias):
    for j in range(greens_ao_dia):
        ganho = banca_final * porcentagem / 100
        #print('Ganho: ', ganho)
        banca_final += ganho

#print(banca_final)
print('Lucro: ', banca_final - banca_inicial)