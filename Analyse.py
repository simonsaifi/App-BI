import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Remplacez ces valeurs selon vos données
chemin_fichier_csv = 'csv/Agents_modifie.csv'
nom_colonne = 'city'
n = 100

# Charger les données
df = pd.read_csv(chemin_fichier_csv)  # Ajustez nrows selon la taille souhaitée pour le test

# Sélectionner la colonne à analyser
variable = df[nom_colonne]

# Calculer les fréquences des catégories et sélectionner les 100 plus fréquentes
top_categories = variable.value_counts().nlargest(n)

# Créer un graphique à barres pour les 100 catégories les plus fréquentes
plt.figure(figsize=(10, 6))  
top_categories.plot(kind='bar')

# Configurer le graphique
plt.title(f'Top {n} des catégories les plus fréquentes dans {nom_colonne}')
plt.xlabel('Catégories')
plt.ylabel('Fréquence')
plt.xticks(rotation=90)
plt.grid(True, which="both", ls="--")


# Calculer et afficher les statistiques standard
total_categories = variable.nunique()
most_frequent_category = variable.mode()[0]
frequency_of_most_frequent = variable.value_counts().max()

print(f"Nombre total de catégories : {total_categories}")
print(f"Catégorie la plus fréquente : {most_frequent_category}")
print(f"Nombre d'occurrences de la catégorie la plus fréquente : {frequency_of_most_frequent}")

# Cherchez d'éventuels problèmes
# Valeurs manquantes
missing_values = df[nom_colonne].isnull().sum()
print(f'Valeurs manquantes dans {nom_colonne}: {missing_values}')

# Afficher le graphique
plt.tight_layout()
plt.show()

# Calculer les fréquences des villes
frequences = df[nom_colonne].value_counts()

# Arrondir les fréquences à l'intervalle de 100 le plus proche
# Et calculer les nouvelles fréquences pour chaque intervalle
interval = 25
rounded_frequencies = (frequences // interval) * interval
freq_des_intervals = rounded_frequencies.value_counts().sort_index()

freq_des_intervals = freq_des_intervals[freq_des_intervals > 0]


# Créer le graphique
plt.figure(figsize=(12, 6))
freq_des_intervals.plot(kind='bar', width=0.8 , logy=True)

plt.title(f'Nombre de villes apparaissant par intervalles de {interval}')
plt.xlabel(f'Intervalle d\'apparitions (par {interval})')
plt.ylabel('Nombre de villes')
plt.xticks(rotation=90)

plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()


