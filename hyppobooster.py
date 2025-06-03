import pandas as pd
import numpy as np

print("🐎 HippoBoost - Générateur Intelligent de Tirages PMU")
print("="*60)
print("Bienvenue dans l'application HippoBoost en mode console.")

# Chargement des données

def load_data():
    data = {
        "Numéro": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Nom": ["Alpha", "Bravo", "Celtic", "Delta", "Echo", "Fuego", "Goliath", "Hélios", "Iris", "Joker"],
        "Forme_Récente": [88, 92, 85, 90, 78, 94, 80, 87, 91, 89],
        "Terrain_Affinité": [85, 90, 80, 75, 82, 89, 76, 88, 91, 79],
        "Santé": [95, 87, 90, 88, 84, 93, 86, 92, 94, 89],
        "Météo_Sensibilité": [90, 86, 89, 87, 88, 85, 91, 86, 90, 92],
        "Cote_Parieurs": [3.5, 4.2, 6.0, 5.1, 8.5, 3.0, 10.0, 4.8, 3.8, 5.5]
    }
    df = pd.DataFrame(data)
    return df

df = load_data()

# Calcul du SGPP
df["SGPP"] = (
    0.30 * df["Forme_Récente"] +
    0.20 * df["Terrain_Affinité"] +
    0.20 * df["Santé"] +
    0.15 * df["Météo_Sensibilité"] +
    0.15 * (100 - df["Cote_Parieurs"] * 10)
)

sorted_df = df.sort_values(by="SGPP", ascending=False).reset_index(drop=True)

print("\n📊 Classement des chevaux par SGPP :\n")
print(sorted_df[["Numéro", "Nom", "SGPP"]])

# Tirages Quinté+
print("\n🎯 Tirages Quinté+ optimisés :\n")
tirages = [sorted_df.loc[i:i+4, ["Numéro", "Nom"]] for i in range(0, 5)]
for i, tirage in enumerate(tirages, 1):
    print(f"\nTirage {i} :")
    print(tirage.to_string(index=False))
