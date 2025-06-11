import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('/content/data_penjualan.csv.xlsx', sheet_name='data_penjualan')

data_numerik = df[['Jumlah Order', 'Harga', 'Total']]

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_numerik)

inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_scaled)
    inertia.append(kmeans.inertia_)

plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method')
plt.xlabel('Jumlah Cluster')
plt.ylabel('Inertia')
plt.show()

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(data_scaled)

sns.pairplot(df, hue='Cluster', vars=['Jumlah Order', 'Harga', 'Total'], palette='Set2')
plt.suptitle("Visualisasi Cluster", y=1.02)
plt.show()

cluster_summary = df.groupby('Cluster')[['Jumlah Order', 'Harga', 'Total']].mean()
print(cluster_summary)
