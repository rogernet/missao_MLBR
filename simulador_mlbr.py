import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

imagem_path = os.path.join("imagens", "alcantara.jpg")

# Dados da missão
altitudes = [0, 40, 150, 300, 450]  # km
velocidades = [0, 2000, 5000, 4800, 7700]  # m/s
estagios = [
    "Lançamento", 
    "1º Estágio", 
    "2º Estágio", 
    "Coasting Controlado", 
    "Injeção Orbital"
]

# Simulação
print("Iniciando contagem regressiva para o lançamento do MLBR...")
for i in range(5, 0, -1):
    print(f"{i}...")
    time.sleep(1)

print("\nIgnição! Decolagem do MLBR!")
time.sleep(2)

if not os.path.exists(imagem_path):
    print(f"⚠️  Imagem não encontrada: {imagem_path}")
    print("Por favor, adicione a imagem da base de Alcântara na pasta /imagens com o nome 'alcantara.jpg'")
    exit()

img = mpimg.imread(imagem_path)

# Plotando a trajetória
plt.figure(figsize=(10, 6))
plt.imshow(img, extent=[min(altitudes), max(altitudes), min(velocidades), max(velocidades)], aspect='auto', alpha=0.3)
plt.plot(altitudes, velocidades, marker='o', linestyle='-', color='red')

plt.title("Trajetória do MLBR (Microlançador Brasileiro) - Brasil no espaço!")
plt.xlabel("Altitude (km)")
plt.ylabel("Velocidade (m/s)")
plt.grid(True)

for alt, vel, est in zip(altitudes, velocidades, estagios):
    plt.annotate(f" {est}", (alt, vel), textcoords="offset points", xytext=(0,10), ha='center')
    print(f"\n {est}: Altitude = {alt} km | Velocidade = {vel} m/s")
    time.sleep(2)

plt.tight_layout()
plt.show()

print("\n Missão cumprida! Satélite em órbita! Brasil no espaço!")
