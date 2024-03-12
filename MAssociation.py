
import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
data = pd.read_csv('csv/Agents_modifie.csv')

# Choisissez deux colonnes numériques parmi 'siret', 'zipcode', 'longitude', 'latitude'
variable_x = 'siret'
variable_y = 'latitude'

# Vérifiez et éliminez les valeurs manquantes
data = data.dropna(subset=[variable_x, variable_y])

# Sélectionner les colonnes pour l'analyse
variable_x_data = data[variable_x]
variable_y_data = data[variable_y]

# Convertir les données en nombres (assurez-vous qu'il n'y a pas de valeurs non numériques)
variable_x_data = pd.to_numeric(variable_x_data, errors='coerce')
variable_y_data = pd.to_numeric(variable_y_data, errors='coerce')

# Supprimer les valeurs manquantes après la conversion
data = data.dropna(subset=[variable_x, variable_y])

# Calcul du coefficient de corrélation de Pearson
correlation_coefficient = variable_x_data.corr(variable_y_data)

# Affichage du graphique
plt.scatter(variable_x_data, variable_y_data, label=f'Corrélation = {correlation_coefficient:.2f}')
plt.xlabel(variable_x)
plt.ylabel(variable_y)
plt.legend()
plt.show()

# Affichage du coefficient de corrélation
print(f'Coefficient de corrélation de Pearson entre {variable_x} et {variable_y} : {correlation_coefficient:.2f}')

