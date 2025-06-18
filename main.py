import numpy as np    # biblioteca de manipulação numérica do Python

# função a ser minimizada
def f(x):
    n = len(x)
    
    result = 0
    for i in range(n):
        for j in range(1,6):
            result = result + j * np.cos(((j + 1) * x[i]) + j)
    return result

# n = 4
x_exemplo = np.array([-10, -5, 5, 10])
valor_funcao = f(x_exemplo)
print(f"Valor da função para x_exemplo: {valor_funcao}")