import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Charger les données depuis un fichier Excel
try:
    # Remplacez par le chemin vers votre fichier
    data = pd.read_excel("Donnees_Qualite_Vin.xlsx")  
    print("Données chargées avec succès !")
except FileNotFoundError:
    print("Erreur : fichier introuvable. Vérifiez le chemin et le nom du fichier.")
    exit()

# Afficher un aperçu des données
print("Aperçu des données :")
print(data.head())

# Vérification des colonnes disponibles
print("Colonnes disponibles :", data.columns)

# Suppression des colonnes non pertinentes si elles existent
colonnes_a_supprimer = ['Nom_vin', 'Producteur']
colonnes_existant_dans_df = [col for col in colonnes_a_supprimer if col in data.columns]
if colonnes_existant_dans_df:
    data = data.drop(columns=colonnes_existant_dans_df)
    print(f"Colonnes supprimées : {colonnes_existant_dans_df}")
else:
    print("Aucune colonne à supprimer parmi :", colonnes_a_supprimer)

# Gestion des valeurs manquantes
data = data.dropna()
print("Données après suppression des valeurs manquantes :", data.shape)

# Normalisation des données numériques
scaler = StandardScaler()
colonnes_numeriques = data.select_dtypes(include=['float64', 'int64']).columns
data_scaled = scaler.fit_transform(data[colonnes_numeriques])

# Application de l'algorithme K-Means
nombre_clusters = 3  # Modifiez selon vos besoins
kmeans = KMeans(n_clusters=nombre_clusters, random_state=42)
clusters = kmeans.fit_predict(data_scaled)

# Ajout des clusters au DataFrame
data['Cluster'] = clusters

# Visualisation des clusters
plt.figure(figsize=(10, 7))
sns.scatterplot(
    x=data_scaled[:, 0],
    y=data_scaled[:, 1],
    hue=clusters,
    palette="viridis",
    legend="full"
)
plt.title("Clustering des vins")
plt.xlabel(colonnes_numeriques[0])
plt.ylabel(colonnes_numeriques[1])
plt.show()

# Analyse des clusters
print("Répartition des clusters :")
print(data['Cluster'].value_counts())

# Exportation des résultats
data.to_csv("resultats_clustering_vins.csv", index=False)
print("Résultats exportés dans 'resultats_clustering_vins.csv'.")
