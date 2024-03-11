import pandas as pd

def explorer_corriger_nettoyer_csv(chemin_fichier_csv):
    # Charger le fichier CSV dans un DataFrame
    df = pd.read_csv(chemin_fichier_csv)

    # Explorer les premières lignes du DataFrame
    print("Aperçu des premières lignes du DataFrame:")
    print(df.head())

    # Explorer les informations sur le DataFrame
    print("\nInformations sur le DataFrame:")
    print(df.info())

    # Explorer les statistiques descriptives
    print("\nStatistiques descriptives:")
    print(df.describe())

    # Corriger les données si nécessaire
    # Remplacer les valeurs manquantes par la moyenne des colonnes numériques
    colonnes_numeriques = df.select_dtypes(include=['number']).columns
    df[colonnes_numeriques] = df[colonnes_numeriques].fillna(df[colonnes_numeriques].mean())

    # Nettoyer les données si nécessaire
    # Supprimer les lignes dupliquées
    df.drop_duplicates(inplace=True)

    # Enregistrer le DataFrame modifié dans un nouveau fichier CSV
    nouveau_chemin_fichier_csv = chemin_fichier_csv.replace('.csv', '_modifie.csv')
    df.to_csv(nouveau_chemin_fichier_csv, index=False)

    print(f"\nLes données ont été corrigées et nettoyées. Nouveau fichier CSV enregistré à : {nouveau_chemin_fichier_csv}")

explorer_corriger_nettoyer_csv('csv/Agents.csv')