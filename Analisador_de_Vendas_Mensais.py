import numpy as np

print("=== Simulação de Vendas Anuais ===")
print(f"Dados gerados aleatoriamente para {12} meses.\n")

M = np.random.randint(1, 9999, 12)
months = (("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"))

print("=" * 40)
print("RESUMO ANUAL")
print("=" * 40)

total = np.sum(M)
print(f"O total em vendas nesse ano foi de R$ {total:.2f}")

med = np.mean(M)
print(f"A média de vendas mensal foi de R$ {med:.2f}")

high = np.argmax(M)
low = np.argmin(M)
print(f"O mês com o maior valor de vendas nesse ano foi: {months[high]}")
print(f"O mês com o menor valor de vendas nesse ano foi: {months[low]} ")

above_med = M[M > med]
months_above = len(M[M > med])
print(f"{months_above} mes(es) acima da média, sendo eles: ")

abovem_med = np.where(M > med,)
for i in range(len(abovem_med[0])):
    print(f"{months[abovem_med[0][i]]} R$ {above_med[i]:.2f}")

perc_dif = ((M[high] - M[low]) / M[low]) * 100
print(f"A diferença percentual entre o pior mês ({months[low]}) e o melhor mês ({months[high]}) foi de: {perc_dif:.2f}%")