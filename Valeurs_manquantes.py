import pandas as pd

# Liste des fichiers CSV
fichiers = [
    'csv/Agents.csv',
    'csv/Criteria.csv',
    'csv/LotBuyers.csv',
    'csv/Lots.csv',
    'csv/LotSuppliers.csv',
    'csv/Names.csv',
]

# Boucle à travers chaque fichier
for chemin_fichier_csv in fichiers:
    # Charger les données
    df = pd.read_csv(chemin_fichier_csv)

    # Afficher des informations de base sur le fichier
    print(f'Analyse du fichier {chemin_fichier_csv}:')

    # Calculer le pourcentage de valeurs manquantes pour chaque variable
    missing_percentage = (df.isnull().sum() / len(df)) * 100

    # Filtrer les variables avec un pourcentage de valeurs manquantes inférieur à 50%
    variables_a_traiter = missing_percentage[missing_percentage < 50].index.tolist()

    # Filtrer les variables numériques
    variables_numeriques = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    # Sélectionner les variables à traiter qui sont numériques
    variables_a_traiter_numeriques = list(set(variables_a_traiter) & set(variables_numeriques))

    # Remplacer les valeurs manquantes par la médiane pour les variables sélectionnées
    df[variables_a_traiter_numeriques] = df[variables_a_traiter_numeriques].fillna(df[variables_a_traiter_numeriques].median())

    # Créer le nom de fichier modifié
    nom_fichier_modifie = chemin_fichier_csv.split('/')[-1].replace('.csv', '_modifie.csv')

    # Enregistrer le nouveau fichier CSV
    df.to_csv(nom_fichier_modifie, index=False)

    # Afficher un message indiquant que le fichier a été modifié et enregistré
    print(f'Le fichier a été modifié et enregistré sous le nom "{nom_fichier_modifie}".')

    # Résumé simple pour l'espace entre les fichiers
    print("\n" + "-"*50 + "\n")
