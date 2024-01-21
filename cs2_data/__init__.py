import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#* map data analysis
map_data = pd.read_csv("../src/maps_statistics.csv")
map_data = map_data.replace(',','', regex=True)

#* mapas mais jogados
maps_played = map_data[["Map", "Play Rate"]].copy()
maps_played = maps_played.replace("%", "", regex=True)

plt.figure(figsize=(8,6))
patches, texts, autotexts = plt.pie(maps_played["Play Rate"], autopct='%1.1f%%', explode=[0.05,0.05,0.05,0.0,0.0,0.0,0.0,0.0,0.0,0])
plt.legend(map_data["Map"][0:6], bbox_to_anchor=(1.03, 1.0), loc='upper left')

for i in range(6, 10):
    patches[i].set_visible(False)
    texts[i].set_visible(False)
    autotexts[i].set_visible(False)

plt.title("Maps Played %")
plt.savefig("test.png")
plt.show()

# *lado que mais ganha em cada mapa  -> gráfico de pizza

#* número de partidas jogadas