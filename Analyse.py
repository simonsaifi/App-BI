import pandas as pd
import matplotlib.pyplot as plt

# Définir les fichiers et les colonnes d'intérêt pour chaque fichier
fichiers_et_colonnes = {
    'csv/Agents_modifie.csv': 'city',
    'csv/Criteria_modifie.csv': 'type',
    'csv/LotBuyers_modifie.csv': 'agentId',
    'csv/Lots_modifie.csv': 'awardPrice',
    'csv/LotSuppliers_modifie.csv': 'agentId',
    'csv/Names_modifie.csv': 'name',
}
n = 100  # Nombre de catégories les plus fréquentes à visualiser
interval = 25  # Intervalles pour regrouper les fréquences

# Boucle à travers chaque fichier et colonne
for chemin_fichier_csv, nom_colonne in fichiers_et_colonnes.items():
    # Charger les données
    df = pd.read_csv(chemin_fichier_csv)

    # Vérifier si la colonne existe
    if nom_colonne in df.columns:
        # Sélectionner la colonne à analyser
        variable = df[nom_colonne]

        # Statistiques et graphiques pour les données catégorielles
        if variable.dtype == 'object':
            # Graphique des catégories les plus fréquentes
            plt.figure(figsize=(10, 6))
            top_categories = variable.value_counts().nlargest(n)
            top_categories.plot(kind='bar')
            plt.title(f'Top {n} des catégories les plus fréquentes dans {nom_colonne} de {chemin_fichier_csv}')
            plt.xlabel('Catégories')
            plt.ylabel('Fréquence')
            plt.xticks(rotation=90)
            plt.grid(True, which="both", ls="--")
            plt.tight_layout()
            plt.show()

            # Statistiques standards
            total_categories = variable.nunique()
            most_frequent_category = variable.mode()[0]
            frequency_of_most_frequent = variable.value_counts().max()
            missing_values = variable.isnull().sum()

            print(f"Analyse de {chemin_fichier_csv} pour {nom_colonne}:")
            print(f"Nombre total de catégories : {total_categories}")
            print(f"Catégorie la plus fréquente : {most_frequent_category}")
            print(f"Nombre d'occurrences de la catégorie la plus fréquente : {frequency_of_most_frequent}")
            print(f'Valeurs manquantes dans {nom_colonne}: {missing_values}')
            print("\n")  # Espacement entre les analyses

            # Graphique de la fréquence des fréquences pour données catégorielles avec intervalles
            frequences = variable.value_counts()
            rounded_frequencies = ((frequences - 1) // interval) * interval + 1  # Arrondir à l'intervalle de 25 le plus proche
            freq_des_intervals = rounded_frequencies.value_counts().sort_index()

            if not freq_des_intervals.empty:
                plt.figure(figsize=(12, 6))
                freq_des_intervals.plot(kind='bar', width=0.8, logy=True)
                plt.title(f'Nombre de {nom_colonne} par intervalles de {interval} d\'apparition dans {chemin_fichier_csv}')
                plt.xlabel(f'Intervalle d\'apparitions')
                plt.ylabel('Nombre de catégories')
                plt.xticks(rotation=90)
                plt.grid(axis='y', linestyle='--')
                plt.tight_layout()
                plt.show()
        
        # Pour les données numériques, affichez simplement les statistiques de base pour l'instant
        elif variable.dtype in ['int64', 'float64'] and nom_colonne in ['agentId', 'awardPrice']:
            # Pour 'agentId', considérez-le comme catégoriel pour cette analyse spécifique
            if nom_colonne == 'agentId':
                agent_counts = variable.value_counts()
                # Afficher seulement s'il y a des agents répétés
                if len(agent_counts) < len(variable):
                    plt.figure(figsize=(10, 6))
                    agent_counts.nlargest(n).plot(kind='bar')  # Top N agents les plus fréquents
                    plt.title(f'Top {n} agents les plus répétés dans {nom_colonne} de {chemin_fichier_csv}')
                    plt.xlabel('Agent ID')
                    plt.ylabel('Fréquence')
                    plt.xticks(rotation=90)
                    plt.grid(True, which="both", ls="--")
                    plt.tight_layout()
                    plt.show()
                else:
                    print(f"Chaque {nom_colonne} est unique dans {chemin_fichier_csv}.")

            # Pour 'awardPrice', tracer un histogramme pour visualiser la distribution
            if nom_colonne == 'awardPrice':
                plt.figure(figsize=(10, 6))
                variable.dropna().plot(kind='hist', bins=30)  # Supprime les NaN et définit le nombre de bins
                plt.title(f'Distribution de {nom_colonne} dans {chemin_fichier_csv}')
                plt.xlabel(nom_colonne)
                plt.ylabel('Fréquence')
                plt.grid(True)
                plt.tight_layout()
                plt.show()
    else:
        print(f'Le fichier {chemin_fichier_csv} ne contient pas la colonne {nom_colonne}.')
