import pandas as pd
import matplotlib.pyplot as plt

# Définir les fichiers
fichiers = [
    'Agents_modifie.csv',
    'Criteria_modifie.csv',
    'LotBuyers_modifie.csv',
    'Lots_modifie.csv',
    'LotSuppliers_modifie.csv',
    'Names_modifie.csv',
]

n = 100  # Nombre de catégories les plus fréquentes à visualiser
interval = 25  # Intervalles pour regrouper les fréquences

# Boucle à travers chaque fichier
for chemin_fichier_csv in fichiers:
    # Charger les données
    df = pd.read_csv(chemin_fichier_csv)

    # Boucle à travers chaque colonne du fichier
    for nom_colonne in df.columns:
        # Sélectionner la colonne à analyser
        variable = df[nom_colonne]

        # Statistiques et graphiques pour les données catégorielles et numériques
        if variable.dtype == 'object' or nom_colonne in ['agentId', 'awardPrice']:  # Modifier selon les besoins spécifiques
            # Graphique des catégories ou valeurs les plus fréquentes
            plt.figure(figsize=(10, 6))
            top_categories = variable.value_counts().nlargest(n)
            top_categories.plot(kind='bar', logy=True)
            plt.title(f'Top {n} des valeurs les plus fréquentes dans {nom_colonne} de {chemin_fichier_csv}')
            plt.xlabel(nom_colonne)
            plt.ylabel('Log Fréquence')
            plt.xticks(rotation=90)
            plt.grid(True, which="both", ls="--")
            plt.tight_layout()
            plt.show()

            # Statistiques standards
            total_categories = variable.nunique()
            most_frequent_category = variable.mode()[0] if not variable.mode().empty else 'N/A'
            frequency_of_most_frequent = variable.value_counts().max()
            missing_values = variable.isnull().sum()

            print(f"Analyse de {chemin_fichier_csv} pour {nom_colonne}:")
            print(f"Nombre total de valeurs uniques : {total_categories}")
            print(f"Valeur la plus fréquente : {most_frequent_category}")
            print(f"Nombre d'occurrences de la valeur la plus fréquente : {frequency_of_most_frequent}")
            print(f'Valeurs manquantes dans {nom_colonne}: {missing_values}')
            print("\n")  # Espacement entre les analyses

            # Graphique de la fréquence des fréquences pour données catégorielles avec intervalles
            if variable.dtype == 'object':
                frequencies = variable.value_counts()
                rounded_frequencies = ((frequencies - 1) // interval) * interval + 1  # Arrondir à l'intervalle le plus proche
                freq_of_intervals = rounded_frequencies.value_counts().sort_index()

                if not freq_of_intervals.empty:
                    plt.figure(figsize=(12, 6))
                    freq_of_intervals.plot(kind='bar', logy=True)
                    plt.title(f'Nombre de {nom_colonne} par intervalles de {interval} d\'apparition dans {chemin_fichier_csv}')
                    plt.xlabel(f'Intervalle d\'apparitions')
                    plt.ylabel('Log Nombre de valeurs')
                    plt.xticks(rotation=90)
                    plt.grid(axis='y', linestyle='--')
                    plt.tight_layout()
                    plt.show()
        else:
            # Pour les autres données numériques, affichez simplement les statistiques de base
            print(f"Analyse de {chemin_fichier_csv} pour {nom_colonne} (Données Numériques):")
            print(variable.describe())
            print("\n")  # Espacement entre les analyses
