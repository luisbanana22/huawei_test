import matplotlib.pyplot as plt
import numpy as np
import sys

a = float(input("Entre com o valor de A:\n "))
b = float(input("Entre com o valor de B:\n "))
c = float(input("Entre com o valor de C:\n "))

delt = (b ** 2) - (4 * a * c)

if a == 0:
    print("A equação não é quadrática.\n")
    sys.exit()

if delt < 0:
    print("Não existem raízes reais.\n")
    sys.exit()

root1 = (-b + delt ** 0.5) / (2 * a)
root2 = (-b - delt ** 0.5) / (2 * a)

x_values = np.linspace(-10, 10, 1000)
y_values = a * x_values ** 2 + b * x_values + c

fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth=2)

ax.scatter([root1, root2], [0, 0], color='red', label='Raízes')

ax.set_title('Gráfico de uma Parábola')
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.legend()

print(f"As raízes são {root1:.2f} e {root2:.2f}")

plt.show()
