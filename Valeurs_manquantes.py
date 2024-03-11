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
    
    # Vérifier les valeurs manquantes
    total_missing = df.isnull().sum().sum()
    print(f'Nombre total de valeurs manquantes: {total_missing}')
    
    # Chercher des valeurs aberrantes pour les colonnes numériques
    num_outliers = 0
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        num_outliers += ((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))).sum()
    print(f'Nombre estimé de valeurs aberrantes: {num_outliers}')
    
    # Vérifier les valeurs erronées potentielles (exemple : valeurs négatives pour les colonnes censées être positives)
    num_erroneous = 0
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        num_erroneous += (df[col] < 0).sum()  # Compter les valeurs négatives comme exemple
    print(f'Nombre estimé de valeurs erronées: {num_erroneous}')
    
    # Résumé simple pour l'espace entre les fichiers
    print("\n" + "-"*50 + "\n")
