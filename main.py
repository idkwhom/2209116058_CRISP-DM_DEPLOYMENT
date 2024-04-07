import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import numpy as np

df = pd.read_csv("Data_Cleaned.csv")
st.write(df.head(5))

df['Gender'] = df['Gender'].replace({1: 'Pria', 2: 'Wanita'})

# Count the number of respondents for each gender
gender_counts = df['Gender'].value_counts()
total_count = gender_counts.sum()

# Calculate percentages
male_percentage = (gender_counts['Pria'] / total_count) * 100
female_percentage = (gender_counts['Wanita'] / total_count) * 100

# Visualize using seaborn in Streamlit
st.write("### Jumlah Responden Berdasarkan gender")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=gender_counts.index, y=gender_counts.values, palette=['skyblue', 'lightcoral'], ax=ax)
ax.set_title('Jumlah Responden Berdasarkan gender')
ax.set_xlabel('Gender')
ax.set_ylabel('Count')

# Display percentages
st.write(f"Pria: {gender_counts['Pria']} ({male_percentage:.2f}%)")
st.write(f"Wanita: {gender_counts['Wanita']} ({female_percentage:.2f}%)")

st.pyplot(fig)

st.write('Terdapat total 114 pria dan 163 wanita dalam dataset. Wanita memiliki jumlah yang lebih banyak daripada pria, dengan proporsi sekitar 58.84% wanita dan 41.16% pria.')

average_age = df['Age'].mean()

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram Umur')
plt.xlabel('Umur')
plt.ylabel('Frekuensi')
plt.grid(True)
plt.tight_layout()

# Display the results
st.write("### Umur Rata-rata Responden")
st.pyplot(plt)
st.write('Rata-rata umur responden adalah 29.21 tahun, yang menunjukkan bahwa mayoritas responden cenderung berada dalam rentang usia muda hingga pertengahan. Hal ini mengindikasikan bahwa data yang digunakan dalam analisis ini mewakili populasi yang relatif muda.')
st.write('Berdasarkan rata-rata umur yang relatif muda, strategi pemasaran dan komunikasi dapat lebih difokuskan pada kelompok usia muda hingga pertengahan.')


food_counts = df['Food'].value_counts()
total_counts = food_counts.sum()

# Calculate percentages
traditional_percentage = (food_counts[1] / total_counts) * 100
western_percentage = (food_counts[2] / total_counts) * 100

# Plot the comparison of traditional and western food
st.write("### Perbandingan Makanan Tradisional dan Barat")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=['Traditional Food', 'Western Food'], y=[food_counts[1], food_counts[2]], palette=['skyblue', 'lightcoral'], ax=ax)
ax.set_title('Perbandingan Makanan Tradisional dan Barat:')
ax.set_ylabel('Count')

st.pyplot(fig)

st.write(f"Traditional Food: {food_counts[1]} ({traditional_percentage:.2f}%)")
st.write(f"Western Food: {food_counts[2]} ({western_percentage:.2f}%)")
st.write('Dari total responden, sebanyak 227 orang atau sekitar 81.95% lebih memilih makanan tradisional.Sementara itu, hanya sekitar 18.05% responden, atau sebanyak 50 orang, yang lebih memilih makanan barat.')
st.write('Berdasarkan preferensi yang dominan terhadap makanan tradisional, dapat diambil kesimpulan bahwa budaya lokal memainkan peran yang signifikan dalam preferensi makanan responden.Dalam konteks ini, peluang bisnis yang terkait dengan makanan tradisional dapat menjadi fokus utama untuk pengusaha restoran atau kafe yang ingin menarik lebih banyak pelanggan atau menyesuaikan menu mereka sesuai dengan preferensi lokal.')
juice_counts = df[['Juice_Carbonated drinks', 'Juice_Fresh Juice']].sum()

# Hitung jumlah preferensi makanan penutup
dessert_counts = df[['Dessert_Maybe', 'Dessert_No', 'Dessert_Yes']].sum()

# Hitung jumlah kategori usia
age_category_counts = df[['AgeCategory_Adult', 'AgeCategory_Child']].sum()

# Visualisasi preferensi minuman jus
st.write("### Preferensi Minuman")
fig1, ax1 = plt.subplots()
juice_counts.plot(kind='bar', ax=ax1, rot=0)  # Rotasi sumbu x menjadi horizontal
ax1.set_ylabel('Jumlah Responden')
st.pyplot(fig1)
st.write("Preferensi Minuman:")
st.write(f"- Carbonated drinks:\n    {juice_counts['Juice_Carbonated drinks']} ({(juice_counts['Juice_Carbonated drinks'] / df.shape[0]) * 100:.2f}%)")
st.write(f"- Fresh Juice:\n    {juice_counts['Juice_Fresh Juice']} ({(juice_counts['Juice_Fresh Juice'] / df.shape[0]) * 100:.2f}%)")
st.write("Mayoritas responden, sekitar 89.17%, lebih memilih minuman jus segar daripada minuman berkarbonasi, yang hanya dipilih oleh sekitar 10.83% dari total responden.")
st.write('Preferensi yang dominan terhadap minuman jus segar menunjukkan bahwa kesadaran akan kesehatan dan gaya hidup sehat mungkin menjadi faktor penting dalam keputusan konsumsi minuman.Untuk pelaku bisnis di industri minuman, fokus pada pengembangan dan pemasaran produk-produk minuman jus segar yang sehat dan alami dapat menjadi strategi yang efektif untuk menarik pelanggan dan memenuhi kebutuhan pasar yang berkembang.')
# Visualisasi preferensi makanan penutup
st.write("### Preferensi Makanan Penutup")
fig2, ax2 = plt.subplots()
dessert_counts.plot(kind='bar', ax=ax2, rot=0)  # Rotasi sumbu x menjadi horizontal
ax2.set_ylabel('Jumlah Responden')
st.pyplot(fig2)
st.write("Preferensi Makanan Penutup:")
st.write(f"- Mungkin:\n    {dessert_counts['Dessert_Maybe']} ({(dessert_counts['Dessert_Maybe'] / df.shape[0]) * 100:.2f}%)")
st.write(f"- Tidak:\n    {dessert_counts['Dessert_No']} ({(dessert_counts['Dessert_No'] / df.shape[0]) * 100:.2f}%)")
st.write(f"- Iya:\n    {dessert_counts['Dessert_Yes']} ({(dessert_counts['Dessert_Yes'] / df.shape[0]) * 100:.2f}%)")
st.write('Dari total responden, sekitar 43.68% tidak yakin apakah mereka ingin makanan penutup (Maybe), 16.97% menyatakan bahwa mereka tidak ingin makanan penutup (No), dan 39.35% menyatakan bahwa mereka ingin makanan penutup (Yes).')
st.write('Adanya persentase yang signifikan dari responden yang tidak yakin tentang keinginan mereka terhadap makanan penutup menunjukkan potensi untuk lebih banyak variasi dalam menu penutup atau opsi penawaran yang tidak terlalu membebani keputusan pembelian. Untuk pemilik restoran atau kafe, menyediakan pilihan makanan penutup yang menarik dan beragam, serta menawarkan opsi "Maybe" yang menarik, dapat meningkatkan daya tarik menu dan memenuhi kebutuhan pelanggan yang bervariasi.')
# Visualisasi kategori usia
st.write("### Age Category")
fig3, ax3 = plt.subplots()
age_category_counts.plot(kind='bar', ax=ax3, rot=0)  # Rotasi sumbu x menjadi horizontal
ax3.set_ylabel('Jumlah Responden')
st.pyplot(fig3)
st.write("Kategori Usia:")
st.write(f"- Dewasa:\n    {age_category_counts['AgeCategory_Adult']} ({(age_category_counts['AgeCategory_Adult'] / df.shape[0]) * 100:.2f}%)")
st.write(f"- Anak - Anak:\n    {age_category_counts['AgeCategory_Child']} ({(age_category_counts['AgeCategory_Child'] / df.shape[0]) * 100:.2f}%)")
st.write("Terdapat perbedaan yang signifikan antara kategori usia responden, dengan 95.31% berada dalam kategori Dewasa (Adult) dan hanya 4.69% berada dalam kategori Anak-anak (Child). Hal ini menunjukkan bahwa mayoritas responden adalah orang dewasa, yang mungkin memiliki preferensi dan kebutuhan yang berbeda dalam konteks makanan dan minuman.")
st.write("Untuk pemilik bisnis di industri makanan dan minuman, dapat menjadi strategi yang efektif untuk fokus pada penyediaan produk dan layanan yang menarik bagi khalayak dewasa. Namun demikian, juga penting untuk tidak mengabaikan kebutuhan dan preferensi konsumen yang lebih muda, terutama jika bisnis tersebut ingin menarik keluarga dan anak-anak sebagai bagian dari pelanggan mereka. Menyediakan opsi menu yang menghibur dan ramah anak serta menawarkan promosi atau paket khusus untuk keluarga dapat menjadi langkah strategis untuk meningkatkan daya tarik bisnis dan memperluas basis pelanggan.")

st.subheader('Prediksi Preferensi Makanan')

file_path = 'dtc.pkl'
clf = joblib.load(file_path)

def age_adult(umur):
    if umur > 18:
        return 1  # Beginner
    else:
        return 0  # Intermediate
    
def age_child(umur):
    if umur < 18:
        return 1  # Beginner
    else:
        return 0  # Intermediate

age = st.number_input('Umur', value=0)  # Default value is 0

Gender = st.selectbox('Victory Status', ["Pria", 'Wanita'])
genders = {"Pria":1, 'Wanita':2}
Gender = genders[Gender]

negara = st.selectbox('Pilih Negara:', df.columns[3:30])
input_negara = [0] * len(df.columns[3:30])  # Initialize all to 0
input_negara[df.columns[3:30].tolist().index(negara)] = 1

minum = st.selectbox('Pilih Preferensi Minuman:', df.columns[30:32])
input_minum = [0] * len(df.columns[30:32])  # Initialize all to 0
input_minum[df.columns[30:32].tolist().index(minum)] = 1

Dessert = st.selectbox('Pilih Preferensi Minuman:', df.columns[32:35])
input_Dessert = [0] * len(df.columns[32:35])  # Initialize all to 0
input_Dessert[df.columns[32:35].tolist().index(Dessert)] = 1

ageadult = age_adult(age)
agechild = age_child(age)


if st.button('Predict'):
    # Input data
    input_data = [Gender, age, ageadult, agechild] + input_negara + input_minum + input_Dessert


    # Perform prediction
    result = clf.predict([input_data])

    # Display prediction result
    if result[0] == 1:
        st.write('Preferensi Makanan nya adalah Tradisional.')
    else:
        st.write('Preferensi Makanan nya adalah Western')
