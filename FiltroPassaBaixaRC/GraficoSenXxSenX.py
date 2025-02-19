import numpy as np
import matplotlib.pyplot as plt

# Definição do sinal
frequencia = 1000  # 1 kHz
periodo = 1 / frequencia  # 1 ms
num_periodos = 3  # Número de períodos a serem plotados
fs = 100000  # Frequência de amostragem (100x maior que o sinal)

# Criando o eixo do tempo
t = np.linspace(0, num_periodos * periodo, int(fs * num_periodos * periodo))

# Sinais originais
y1 = np.sin(2 * np.pi * frequencia * t)  # sen(x)
y2 = y1 ** 2  # sen²(x)

# Sinais deslocados para excursão entre 0 e 1
y3 = (y1 + 1) / 2  # (sen(x) + 1) / 2
y4 = y3 ** 2  # ((sen(x) + 1) / 2)²

# Criando a figura
plt.figure(figsize=(10, 6))

# Gráfico 1: sen(x) e sen²(x)
plt.subplot(2, 1, 1)
plt.plot(t * 1000, y1, label='sen(2π1000t)', linestyle='-', color='b')
plt.plot(t * 1000, y2, label='sen²(2π1000t)', linestyle='--', color='r')
plt.axhline(0, color='black', linewidth=0.5)
plt.xlabel('Tempo (ms)')
plt.ylabel('Amplitude')
plt.title('Gráfico de sen(x) e sen²(x)')
plt.legend()
plt.grid()

# Gráfico 2: (sen(x) + 1) / 2 e ((sen(x) + 1) / 2)²
plt.subplot(2, 1, 2)
plt.plot(t * 1000, y3, label='(sen(2π1000t) + 1) / 2', linestyle='-', color='g')
plt.plot(t * 1000, y4, label='((sen(2π1000t) + 1) / 2)²', linestyle='--', color='m')
plt.axhline(0, color='black', linewidth=0.5)
plt.xlabel('Tempo (ms)')
plt.ylabel('Amplitude')
plt.title('Gráfico de (sen(x) + 1) / 2 e ((sen(x) + 1) / 2)²')
plt.legend()
plt.grid()

# Ajuste de layout e exibição do gráfico
plt.tight_layout()
plt.show()

