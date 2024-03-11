import pandas as pd
import matplotlib.pyplot as plt

# Veri setini oku
df = pd.read_csv("C:\\Users\\yusuf\\OneDrive\\Masaüstü\\py_work\\Auto-Sales-data.csv")

# Boş satırları kaldır
df.dropna(inplace=True)

# Boşluk içeren sütun isimlerini düzenle
df.columns = [column.strip() for column in df.columns]

# Her bir satırdaki eksik verileri "Boş" ile doldur
df.fillna("Boş", inplace=True)

# Veri seti hakkında temel bilgileri gösterir
print(df.info())

# Sayısal sütunlar için temel istatistikleri gösterir
print(df.describe())

# En çok satış yapan ülkeleri gösterir
en_cok_satis_yapan_ulke = df.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False).head(10)

# Ülkeleri çubuk grafikle görselleştir
plt.figure(figsize=(10, 6))
plt.bar(en_cok_satis_yapan_ulke.index, en_cok_satis_yapan_ulke.values)
plt.xlabel('Ülke')
plt.ylabel('Toplam Satış')
plt.title('En Çok Satış Yapan Ülkeler')
plt.xticks(rotation=45)

# Ülkelere göre ortalama satışları çubuk grafikle görselleştir
plt.figure(figsize=(12, 6))
plt.bar(df['COUNTRY'], df['SALES'])
plt.xlabel('Ülke')
plt.ylabel('Ortalama Satış')
plt.title('Ülkelere Göre Ortalama Satışların Çubuk Grafiği')
plt.xticks(rotation=45)

# Ürün hatlarına göre satışların oranlarını pasta grafiği ile görselleştir
plt.figure(figsize=(8, 8))
df['PRODUCTLINE'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Ürün Hatlarına Göre Satışların Oranları')

# Deal Size'a göre satışların kutu grafiği ile görselleştir
plt.figure(figsize=(8, 6))
plt.boxplot([df[df['DEALSIZE'] == 'Small']['SALES'], df[df['DEALSIZE'] == 'Medium']['SALES'], df[df['DEALSIZE'] == 'Large']['SALES']], labels=['Small', 'Medium', 'Large'])
plt.xlabel('Deal Size')
plt.ylabel('Satış')
plt.title('Deal Size\'a Göre Satışların Kutu Grafiği')

# Müşteri ülkelerine göre satışları çubuk grafikle görselleştir
plt.figure(figsize=(12, 6))
plt.bar(df['COUNTRY'], df['SALES'])
plt.xlabel('Ülke')
plt.ylabel('Toplam Satış')
plt.title('Müşteri Ülkelerine Göre Satışlar')
plt.xticks(rotation=45)

# Ürün hatlarına göre satışları çubuk grafikle görselleştir
plt.figure(figsize=(12, 6))
plt.bar(df['PRODUCTLINE'], df['SALES'])
plt.xlabel('Ürün Hattı')
plt.ylabel('Toplam Satış')
plt.title('Ürün Hatlarına Göre Satışlar')
plt.xticks(rotation=45)

# MSRP ile satış arasındaki ilişkiyi saçılım grafiği ile görselleştir
plt.figure(figsize=(10, 6))
plt.scatter(df['MSRP'], df['SALES'])
plt.xlabel('MSRP')
plt.ylabel('Satış')
plt.title('Satış ve MSRP İlişkisi')

# En çok satış yapan müşterileri gösterir
en_cok_satis_yapan_musteri = df.groupby('CUSTOMERNAME')['SALES'].sum().sort_values(ascending=False).head(10)
print(en_cok_satis_yapan_musteri)

# Satış istatistiklerini gösterir
satis_istatistikleri = df['SALES'].describe()
print(satis_istatistikleri)

# İlk sipariş tarihi ve son sipariş tarihini gösterir
ilk_siparis_tarihi = df['ORDERDATE'].min()
son_siparis_tarihi = df['ORDERDATE'].max()
print(f"İlk sipariş tarihi: {ilk_siparis_tarihi}\nSon sipariş tarihi: {son_siparis_tarihi}")

# En fazla sipariş alan müşteriyi gösterir
en_fazla_siparis_alan_musteri = df.groupby('CUSTOMERNAME')['QUANTITYORDERED'].sum().idxmax()
print(f"En fazla sipariş alan müşteri: {en_fazla_siparis_alan_musteri}")

# Ürün başına ortalama satışı gösterir
df['SALES_PER_PRODUCT'] = df['SALES'] / df['QUANTITYORDERED']
ortalama_satis_urun_basi = df['SALES_PER_PRODUCT'].mean()
print(f"Ürün başına ortalama satış: {ortalama_satis_urun_basi}")

# Görselleştirmeleri göster
plt.show()
