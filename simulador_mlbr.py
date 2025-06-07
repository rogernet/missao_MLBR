import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# imagem da base (tem q ter essa pasta/imagem)
img_path = os.path.join("imagens", "F:\\Projetos_tecnicos\\Python\MLBR\\alcantara.jpg")

# trajetoria estimada
alt_km = [0, 40, 150, 300, 450]
vel_ms = [0, 2000, 5000, 4800, 7700]
fases = ["Lançamento", "1º Estágio", "2º Estágio", "Coasting", "Órbita"]

# contagem clássica
print("Contagem regressiva para o MLBR 🚀 - Ao infinito e Além!")
for t in range(5, 0, -1):
    print(f"{t}...")
    time.sleep(1)

print("\n🔥 Ignição! MLBR subindo!")
time.sleep(1.5)

# checa se tem imagem
if not os.path.exists(img_path):
    print(f"⚠️  Cadê a imagem? Esperava {img_path}")
    print("Coloca a imagem da base de Alcântara na pasta 'imagens' com nome 'alcantara.jpg'")
    exit()

# carrega o fundo
img = mpimg.imread(img_path)

# gráfico com fundo de Alcântara
plt.figure(figsize=(10, 6))
plt.imshow(img, extent=[min(alt_km), max(alt_km), min(vel_ms), max(vel_ms)],
           aspect='auto', alpha=0.25)

plt.plot(alt_km, vel_ms, 'ro-', linewidth=2)

plt.title("Simulação de voo - MLBR - Ao infinito e Além!")
plt.xlabel("Altitude (km)")
plt.ylabel("Velocidade (m/s)")
plt.grid(True)

# anotações das fases
for a, v, nome in zip(alt_km, vel_ms, fases):
    plt.annotate(f" {nome}", (a, v), textcoords="offset points", xytext=(0, 12), ha='center')
    print(f"{nome}: Alt {a} km | Vel {v} m/s")
    time.sleep(1)

plt.tight_layout()
plt.show()

print("\n✅ Satélite inserido! Brasil na órbita!")
